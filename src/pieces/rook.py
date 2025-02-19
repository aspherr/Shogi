from piece import Piece
from const import TOP, BOTTOM, LEFT, RIGHT

class Rook(Piece):
    id, promoted_id = 7, 6

    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)

    def __repr__(self) -> str:
        return "Rook"

    def moves(self, board):
        moves = []
        captures = []

        if self.player == "sente":
            for i in range(self.rank, 0, -1):
                self.top = self.rank > TOP and (
                    board[i - 1][self.file] == 0 or board[i - 1][self.file] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.top, (i - 1, self.file)
                )
                if board[i - 1][self.file] != 0:
                    break

            for i in range(self.rank, 8, +1):
                self.bottom = self.rank < BOTTOM and (
                    board[i + 1][self.file] == 0 or board[i + 1][self.file] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.bottom, (i + 1, self.file)
                )
                if board[i + 1][self.file] != 0:
                    break

            for i in range(self.file, 0, -1):
                self.left = self.file > LEFT and (
                    board[self.rank][i - 1] == 0 or board[self.rank][i - 1] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.left, (self.rank, i - 1)
                )
                if board[self.rank][i - 1] != 0:
                    break

            for i in range(self.file, 8, +1):
                self.right = self.rank < RIGHT and (
                    board[self.rank][i + 1] == 0 or board[self.rank][i + 1] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.right, (self.rank, i + 1)
                )
                if board[self.rank][i + 1] != 0:
                    break

        elif self.player == "gote":
            for i in range(self.rank, 0, -1):
                self.bottom = self.rank > TOP and (
                    board[i - 1][self.file] == 0 or board[i - 1][self.file] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.bottom, (i - 1, self.file)
                )
                if board[i - 1][self.file] != 0:
                    break

            for i in range(self.rank, 8, +1):
                self.top = self.rank < BOTTOM and (
                    board[i + 1][self.file] == 0 or board[i + 1][self.file] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.top, (i + 1, self.file)
                )
                if board[i + 1][self.file] != 0:
                    break

            for i in range(self.file, 0, -1):
                self.right = self.file > LEFT and (
                    board[self.rank][i - 1] == 0 or board[self.rank][i - 1] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.right, (self.rank, i - 1)
                )
                if board[self.rank][i - 1] != 0:
                    break

            for i in range(self.file, 8, +1):
                self.left = self.rank < RIGHT and (
                    board[self.rank][i + 1] == 0 or board[self.rank][i + 1] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.left, (self.rank, i + 1)
                )
                if board[self.rank][i + 1] != 0:
                    break

        return moves, captures

