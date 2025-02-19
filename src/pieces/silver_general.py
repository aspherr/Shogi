from piece import Piece

class SilverGeneral(Piece):
    id, promotion_id = 4, 4

    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)

    def __repr__(self) -> str:
        return "Silver General"

    def moves(self, board):
        moves = []
        captures = []

        self.boundaries(board)
        if self.player == "sente":
            conditions = [
                self.top,
                self.top_right,
                self.top_left,
                self.bottom_right,
                self.bottom_left,
            ]
            pos = [
                (self.rank - 1, self.file),
                (self.rank - 1, self.file + 1),
                (self.rank - 1, self.file - 1),
                (self.rank + 1, self.file + 1),
                (self.rank + 1, self.file - 1),
            ]

            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])

        elif self.player == "gote":
            conditions = [
                self.bottom,
                self.bottom_left,
                self.bottom_right,
                self.top_left,
                self.top_right,
            ]
            pos = [
                (self.rank + 1, self.file),
                (self.rank + 1, self.file - 1),
                (self.rank + 1, self.file + 1),
                (self.rank - 1, self.file - 1),
                (self.rank - 1, self.file + 1),
            ]

            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])

        return moves, captures

