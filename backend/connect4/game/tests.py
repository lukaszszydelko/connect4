from django.test import TestCase
from .models import Connect4Game, Player
from .services import check_diagonal_left, check_draw
from .common import BOARD_SIZE


class CheckIfFinishedTestCase(TestCase):
    def testDiagonalLeft(self):
        board = [["_" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        board[0][0] = board[1][1] = board[2][2] = Player.FIRST
        game = Connect4Game.objects.create(current_player=Player.FIRST, board=board)
        self.assertFalse(check_diagonal_left(game, 2, 2))
        game.board[3][3] = Player.FIRST
        self.assertTrue(check_diagonal_left(game, 2, 2))

    def testDraw(self):
        board = []
        for i in range(BOARD_SIZE):
            board.append([])
            for j in range(BOARD_SIZE):
                if (i + j) % 2:
                    board[i].append(Player.FIRST)
                else:
                    board[i].append(Player.SECOND)

        game = Connect4Game.objects.create(current_player=Player.FIRST, board=board)
        self.assertTrue(check_draw(game))
