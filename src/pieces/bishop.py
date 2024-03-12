from piece import Piece
from const import TOP, BOTTOM, LEFT, RIGHT

class Bishop(Piece):
    id = 6

    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)

    def __repr__(self) -> str:
        return "Bishop"

    def moves(self, board):
        moves = []
        captures = []

        if self.player == "sente":
            tr_file, tl_file = self.file, self.file
            br_file, bl_file = self.file, self.file

            for a in range(self.rank, 0, -1):
                self.top_right = (a > TOP and tr_file < RIGHT) and (
                    board[a - 1][tr_file + 1] == 0 or board[a - 1][tr_file + 1] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.top_right, (a - 1, tr_file + 1)
                )
                if self.top_right is False or board[a - 1][tr_file + 1] != 0:
                    break

                tr_file += 1

            for b in range(self.rank, 0, -1):
                self.top_left = (b > TOP and tl_file > LEFT) and (
                    board[b - 1][tl_file - 1] == 0 or board[b - 1][tl_file - 1] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.top_left, (b - 1, tl_file - 1)
                )
                if self.top_left is False or board[b - 1][tl_file - 1] != 0:
                    break

                tl_file -= 1

            for c in range(self.rank, 8, +1):
                self.bottom_right = (c < BOTTOM and br_file < RIGHT) and (
                    board[c + 1][br_file + 1] == 0 or board[c + 1][br_file + 1] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.bottom_right, (c + 1, br_file + 1)
                )
                if self.bottom_right is False or board[c + 1][br_file + 1] != 0:
                    break

                br_file += 1

            for d in range(self.rank, 8, +1):
                self.bottom_left = (d < BOTTOM and bl_file > LEFT) and (
                    board[d + 1][bl_file - 1] == 0 or board[d + 1][bl_file - 1] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.bottom_left, (d + 1, bl_file - 1)
                )
                if self.bottom_left is False or board[d + 1][bl_file - 1] != 0:
                    break

                bl_file -= 1

        elif self.player == "gote":
            tr_file, tl_file = self.file, self.file
            br_file, bl_file = self.file, self.file

            for a in range(self.rank, 0, -1):
                self.bottom_left = (a > TOP and bl_file < RIGHT) and (
                    board[a - 1][bl_file + 1] == 0 or board[a - 1][bl_file + 1] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.bottom_left, (a - 1, bl_file + 1)
                )
                if self.bottom_left is False or board[a - 1][bl_file + 1] != 0:
                    break

                bl_file += 1

            for b in range(self.rank, 0, -1):
                self.bottom_right = (b > TOP and br_file > LEFT) and (
                    board[b - 1][br_file - 1] == 0 or board[b - 1][br_file - 1] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.bottom_right, (b - 1, br_file - 1)
                )
                if self.bottom_right is False or board[b - 1][br_file - 1] != 0:
                    break

                br_file -= 1

            for c in range(self.rank, 8, +1):
                self.top_left = (c < BOTTOM and tl_file < RIGHT) and (
                    board[c + 1][tl_file + 1] == 0 or board[c + 1][tl_file + 1] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.top_left, (c + 1, tl_file + 1)
                )
                if self.top_left is False or board[c + 1][tl_file + 1] != 0:
                    break

                tl_file += 1

            for d in range(self.rank, 8, +1):
                self.top_right = (d < BOTTOM and tr_file > LEFT) and (
                    board[d + 1][tr_file - 1] == 0 or board[d + 1][tr_file - 1] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.top_right, (d + 1, tr_file - 1)
                )
                if self.top_right is False or board[d + 1][tr_file - 1] != 0:
                    break

                tr_file -= 1

        return moves, captures

