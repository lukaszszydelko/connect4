from connect4.wsgi import *
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/game/current/", consumers.GameConsumer.as_asgi()),
]
