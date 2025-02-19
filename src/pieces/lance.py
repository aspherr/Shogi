from piece import Piece
from const import TOP, BOTTOM

class Lance(Piece):
    id, promotion_id = 2, 2

    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)

    def __repr__(self) -> str:
        return "Lance"

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

        elif self.player == "gote":
            for i in range(self.rank, 8, +1):
                self.top = self.rank < BOTTOM and (
                    board[i + 1][self.file] == 0 or board[i + 1][self.file] != 0
                )

                self.generate_moves(
                    board, moves, captures, self.top, (i + 1, self.file)
                )
                if board[i + 1][self.file] != 0:
                    break

        return moves, captures

