from piece import Piece

class GoldGeneral(Piece):
    id = 5

    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)

    def __repr__(self) -> str:
        return "Gold General"

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
            ]
            pos = [
                (self.rank - 1, self.file),
                (self.rank, self.file + 1),
                (self.rank, self.file - 1),
                (self.rank + 1, self.file),
                (self.rank - 1, self.file + 1),
                (self.rank - 1, self.file - 1),
            ]

            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])

        elif self.player == "gote":
            conditions = [
                self.bottom,
                self.left,
                self.right,
                self.top,
                self.bottom_left,
                self.bottom_right,
            ]
            pos = [
                (self.rank + 1, self.file),
                (self.rank, self.file - 1),
                (self.rank, self.file + 1),
                (self.rank - 1, self.file),
                (self.rank + 1, self.file - 1),
                (self.rank + 1, self.file + 1),
            ]

            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])

        return moves, captures

