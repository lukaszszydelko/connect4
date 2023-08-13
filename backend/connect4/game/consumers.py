import json
from game.serializers import GameSerializer

from game.services import handle_move

from .models import Connect4Game

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.game = Connect4Game.objects.filter(game_end=False).order_by("-id").first()
        self.room_group_name = f"game_{self.game.id}"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        self.game = Connect4Game.objects.filter(game_end=False).order_by("-id").first()
        text_data_json = json.loads(text_data)
        message = text_data_json["text"]
        sender = text_data_json["sender"]
        type = message.pop("type")
        if type == "create":
            board = [["_" for _ in range(7)] for _ in range(7)]
            message["board"] = board
            self.game = Connect4Game.objects.create(**message)
            return_serializer = GameSerializer(self.game)
            message = return_serializer.data
        elif type == "update":
            try:
                handle_move(self.game, message)
                return_serializer = GameSerializer(self.game)
                message = return_serializer.data
            except ValueError as e:
                message = str(e)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {"type": "game_message", "message": message, "sender": sender},
        )

    def game_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"message": message}))
