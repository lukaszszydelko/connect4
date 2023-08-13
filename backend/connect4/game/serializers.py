from .models import Connect4Game
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    board = serializers.ListField(
        child=serializers.ListField(child=serializers.CharField()), required=False
    )

    class Meta:
        model = Connect4Game
        fields = ["id", "current_player", "board", "game_end", "message"]
