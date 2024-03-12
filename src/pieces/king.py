from piece import Piece

class King(Piece):
    id = 8

    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
        self.is_king = True

    def __repr__(self) -> str:
        return "King"

    def moves(self, board):
        moves = []
        captures = []

        self.boundaries(board)
        if self.player == "sente":
            conditions = [
                self.top,
                self.right,
                self.left,
                self.bottom,
                self.top_right,
                self.top_left,
                self.bottom_right,
                self.bottom_left,
            ]

            pos = [
                (self.rank - 1, self.file),
                (self.rank, self.file + 1),
                (self.rank, self.file - 1),
                (self.rank + 1, self.file),
                (self.rank - 1, self.file + 1),
                (self.rank - 1, self.file - 1),
                (self.rank + 1, self.file + 1),
                (self.rank + 1, self.file - 1),
            ]

            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])

        elif self.player == "gote":
            conditions = [
                self.top,
                self.right,
                self.left,
                self.bottom,
                self.top_right,
                self.top_left,
                self.bottom_right,
                self.bottom_left,
            ]

            pos = [
                (self.rank - 1, self.file),
                (self.rank, self.file + 1),
                (self.rank, self.file - 1),
                (self.rank + 1, self.file),
                (self.rank - 1, self.file + 1),
                (self.rank - 1, self.file - 1),
                (self.rank + 1, self.file + 1),
                (self.rank + 1, self.file - 1),
            ]

            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])

        return moves, captures

