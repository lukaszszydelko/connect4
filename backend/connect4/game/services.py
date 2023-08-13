from .common import BOARD_SIZE, CONNECT_2_WIN
from .models import Connect4Game, Player


def is_save(coordinate: int):
    return coordinate >= 0 and coordinate < BOARD_SIZE


def check_default(
    game: Connect4Game, row: int, column: int, dir_row: int, dir_column: int
) -> bool:
    if all(
        [
            is_save(row),
            is_save(row + (CONNECT_2_WIN - 1) * dir_row),
            is_save(column),
            is_save(column + (CONNECT_2_WIN - 1) * dir_column),
        ]
    ):
        return [
            game.board[row + i * dir_row][column + i * dir_column]
            for i in range(CONNECT_2_WIN)
        ].count(game.current_player) == CONNECT_2_WIN

    return False


def check_row(game: Connect4Game, row: int, column: int) -> bool:
    return any(
        [check_default(game, row, column - i, 0, 1) for i in range(CONNECT_2_WIN)]
    )


def check_column(game: Connect4Game, row: int, column: int) -> bool:
    return any(
        [check_default(game, row - i, column, 1, 0) for i in range(CONNECT_2_WIN)]
    )


def check_diagonal_left(game: Connect4Game, row: int, column: int) -> bool:
    return any(
        [check_default(game, row - i, column - i, 1, 1) for i in range(CONNECT_2_WIN)]
    )


def check_diagonal_right(game: Connect4Game, row: int, column: int) -> bool:
    return any(
        [check_default(game, row + i, column - i, -1, 1) for i in range(CONNECT_2_WIN)]
    )


def check_finish_game(game: Connect4Game, row: int, column: int) -> bool:
    return any(
        [
            check_row(game, row, column),
            check_column(game, row, column),
            check_diagonal_left(game, row, column),
            check_diagonal_right(game, row, column),
        ]
    )


def check_draw(game: Connect4Game) -> bool:
    for i in game.board:
        for j in i:
            if j == "_":
                return False

    return True


def handle_move(game: Connect4Game, data: dict) -> bool:
    if game.current_player != data["player"]:
        raise ValueError(f"Wrong player move, current player {game.current_player}")
    if game.game_end:
        raise ValueError("Game already finished!")
    field = -1
    if data["side"] == "L":
        field = "".join(game.board[data["line"]]).find("_")
    elif data["side"] == "R":
        field = "".join(game.board[data["line"]]).rfind("_")

    if game.current_player == data["player"] and field > -1:
        game.board[data["line"]][field] = game.current_player

        if check_finish_game(game, data["line"], field):
            game.game_end = True
            players_mapping = {Player.FIRST: "1", Player.SECOND: "2"}
            game.message = f" player {players_mapping[game.current_player]} win!"
        elif check_draw(game):
            game.game_end = True
            game.message = "Game finished with draw!"
        else:
            game.current_player = game.change_players()
        game.save()
    else:
        raise ValueError
