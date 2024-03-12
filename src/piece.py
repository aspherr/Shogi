import pygame
from const import (
    WINDOW,
    BOARD_X,
    BOARD_Y,
    BOARD_TILE_SIZE,
    SENTE_PIECES,
    GOTE_PIECES,
    TOP,
    BOTTOM,
    LEFT,
    RIGHT,
    GREY2,
    GREEN,
    RED,
)


class Piece:
    def __init__(self, rank, file, player) -> None:
        self.rank = rank
        self.file = file
        self.player = player

        self.selected = False
        self.is_king = False
        self.in_check = False

    def get_piece(self, board) -> pygame.Surface:
        if self.player == "sente":
            piece = SENTE_PIECES[self.id - 1]  # pyright: ignore

        else:
            piece = GOTE_PIECES[self.id - 1]  # pyright: ignore

        self.render_selection(board)
        return piece

    def get_piece_pos(self) -> tuple:
        x = int(BOARD_X + (self.file * BOARD_TILE_SIZE)) + 5
        y = int(BOARD_Y + (self.rank * BOARD_TILE_SIZE)) + 2

        return x, y

    def update_img(self, pos) -> None:
        self.rank = pos[0]
        self.file = pos[1]

    def boundaries(self, board) -> None:
        self.top = self.rank > TOP and (
            board[self.rank - 1][self.file] == 0 or board[self.rank - 1][self.file] != 0
        )

        self.bottom = self.rank < BOTTOM and (
            board[self.rank + 1][self.file] == 0 or board[self.rank + 1][self.file] != 0
        )

        self.left = self.file > LEFT and (
            board[self.rank][self.file - 1] == 0 or board[self.rank][self.file - 1] != 0
        )

        self.right = self.file < RIGHT and (
            board[self.rank][self.file + 1] == 0 or board[self.rank][self.file + 1] != 0
        )

        self.top_left = (self.rank > TOP and self.file > LEFT) and (
            board[self.rank - 1][self.file - 1] == 0
            or board[self.rank - 1][self.file - 1] != 0
        )

        self.top_right = (self.rank > TOP and self.file < RIGHT) and (
            board[self.rank - 1][self.file + 1] == 0
            or board[self.rank - 1][self.file + 1] != 0
        )

        self.bottom_left = (self.rank < BOTTOM and self.file > LEFT) and (
            board[self.rank + 1][self.file - 1] == 0
            or board[self.rank + 1][self.file - 1] != 0
        )

        self.bottom_right = (self.rank < BOTTOM and self.file < RIGHT) and (
            board[self.rank + 1][self.file + 1] == 0
            or board[self.rank + 1][self.file + 1] != 0
        )

    def generate_moves(self, board, moves, captures, condition, pos) -> None:
        if condition is True:
            if board[pos[0]][pos[1]] == 0:
                moves.append((pos[1], pos[0]))

            elif board[pos[0]][pos[1]].player != self.player:
                moves.append((pos[1], pos[0]))
                captures.append((pos[0], pos[1]))

    def moveset(self, board) -> list:
        moveset, _ = self.moves(board)  # pyright: ignore
        return moveset

    def render_moves(self, board) -> None:
        moves, captures = self.moves(board)  # pyright: ignore
        moves, captures = list(moves), list(captures)

        for i in captures:
            rank = i[0]
            file = i[1]

            if (
                board[rank][file] != 0
                and (file, rank) in moves
                and board[rank][file].player != self.player
            ):
                x1 = int(BOARD_X + (file * BOARD_TILE_SIZE)) + 1
                y1 = int(BOARD_Y + (rank * BOARD_TILE_SIZE)) + 1

                moves.remove((file, rank))
                pygame.draw.rect(WINDOW, GREEN, (x1, y1, 60, 60), 1)

        for j in moves:
            x2 = int(BOARD_X + (j[0] * BOARD_TILE_SIZE)) + 1
            y2 = int(BOARD_Y + (j[1] * BOARD_TILE_SIZE)) + 1
            pygame.draw.rect(WINDOW, GREY2, (int(x2), int(y2), 60, 60), 0)

    def render_selection(self, board) -> None:
        if self.selected:
            pygame.draw.rect(
                WINDOW,
                GREY2,
                (self.get_piece_pos()[0] - 4, self.get_piece_pos()[1] - 1, 60, 60),
                0,
            )
            self.render_moves(board)

        if self.in_check:
            pygame.draw.rect(
                WINDOW,
                RED,
                (self.get_piece_pos()[0] - 4, self.get_piece_pos()[1] - 1, 60, 60),
                1,
            )

