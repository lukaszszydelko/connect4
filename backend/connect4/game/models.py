from django.db import models
from django.contrib.postgres.fields import ArrayField

from .common import BOARD_SIZE


class Player(models.TextChoices):
    FIRST = "o", "o"
    SECOND = "x", "x"
    NOT_KNOWN = "_", "_"


class Connect4Game(models.Model):
    current_player = models.CharField(
        max_length=1, choices=Player.choices, default=Player.FIRST
    )
    board = ArrayField(
        ArrayField(
            models.CharField(
                max_length=1, choices=Player.choices, default=Player.NOT_KNOWN
            ),
            size=BOARD_SIZE,
        ),
        size=BOARD_SIZE,
    )
    game_end = models.BooleanField(default=False)
    message = models.CharField(max_length=100, default="")

    def change_players(self) -> str:
        return self.current_player == Player.FIRST and Player.SECOND or Player.FIRST
