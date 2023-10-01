from const import *


class Piece:

    def __init__(self, rank, file, player) -> None:
        self.rank = rank
        self.file = file
        self.player = player

        self.selected = False


    def get_piece(self) -> pygame.image:
        
        if self.player == "sente":
            piece = SENTE_PIECES[self.id-1]
        
        else:
            piece = GOTE_PIECES[self.id-1]
        
        self.render_selection()
        return piece


    def get_piece_pos(self) -> int:
        
        x = int(BOARD_X + (self.file * BOARD_TILE_SIZE)) + 5
        y = int(BOARD_Y + (self.rank * BOARD_TILE_SIZE)) + 2

        return x, y


    def render_selection(self) -> None:

        if self.selected:
            pygame.draw.rect(
                WINDOW, GREY2, (self.get_piece_pos()[0]-4, self.get_piece_pos()[1]-1, 60, 60), 0
                )


    def update_img(self, pos) -> None:
        
        self.rank = pos[0]
        self.file = pos[1]


class Pawn(Piece):
    id = 1
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Pawn'


class Lance(Piece):
    id = 2
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Lance'
    

class Knight(Piece):
    id = 3
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Knight'
    

class SilverGeneral(Piece):
    id = 4
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Silver General'


class GoldGeneral(Piece):
    id = 5
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Gold General'
    

class Bishop(Piece):
    id = 6
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Bishop'
    

class Rook(Piece):
    id = 7
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Rook'


class King(Piece):
    id = 8
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'King'

