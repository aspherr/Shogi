from piece import Piece
from const import TOP, BOTTOM, LEFT, RIGHT

class Knight(Piece):
    id, promotion_id = 3, 3

    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)

    def __repr__(self) -> str:
        return "Knight"

    def moves(self, board):
        moves = []
        captures = []

        self.top_right = (self.rank > TOP + 1 and self.file < RIGHT) and (
            board[self.rank - 2][self.file + 1] == 0
            or board[self.rank - 2][self.file + 1] != 0
        )

        self.top_left = (self.rank > TOP + 1 and self.file > LEFT) and (
            board[self.rank - 2][self.file - 1] == 0
            or board[self.rank - 2][self.file - 1] != 0
        )

        self.bottom_right = (self.rank < BOTTOM - 1 and self.file < RIGHT) and (
            board[self.rank + 2][self.file + 1] == 0
            or board[self.rank + 2][self.file + 1] != 0
        )

        self.bottom_left = (self.rank < BOTTOM - 1 and self.file > LEFT) and (
            board[self.rank + 2][self.file - 1] == 0
            or board[self.rank + 2][self.file - 1] != 0
        )

        if self.player == "sente":
            conditions = [self.top_right, self.top_left]
            pos = [(self.rank - 2, self.file + 1), (self.rank - 2, self.file - 1)]

            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])

        elif self.player == "gote":
            conditions = [self.bottom_right, self.bottom_left]
            pos = [(self.rank + 2, self.file + 1), (self.rank + 2, self.file - 1)]

            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])

        return moves, captures

