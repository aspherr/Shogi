from piece import Piece

class Pawn(Piece):
    id, promotion_id = 1, 1

    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)

    def __repr__(self) -> str:
        return "Pawn"

    def moves(self, board):
        moves = []
        captures = []

        self.boundaries(board)
        if self.player == "sente":
            self.generate_moves(
                board, moves, captures, self.top, (self.rank - 1, self.file)
            )

        elif self.player == "gote":
            self.generate_moves(
                board, moves, captures, self.bottom, (self.rank + 1, self.file)
            )

        return moves, captures

