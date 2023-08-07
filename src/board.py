from const import *
from piece import Pawn, Lance, Knight, SilverGeneral, GoldGeneral, Bishop, Rook, King


class Board:

    def __init__(self, ranks = 9, files = 9) -> None:
        self.ranks = ranks
        self.files = files
        self.board = [[0 for _ in range(ranks)] for _ in range(files)]
        self.init_board()


    def notation(self) -> str:

        ranks_dict = {'1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 1, '9': 0}
        rank_notation = {value: rank_key for rank_key, value in ranks_dict.items()}

        files_dict = {'一': 0, '二': 1, '三': 2, '四': 3, '五': 4, '六': 5, '七': 6, '八': 7, '九': 8}
        file_notation = {value: file_key for file_key, value in files_dict.items()}

        return rank_notation[self.ranks] + file_notation[self.files]


    def init_board(self) -> None:

        bottom_rank_pieces = [
            Lance, Knight, SilverGeneral, GoldGeneral, King, GoldGeneral, SilverGeneral, Knight, Lance
        ]

        for i in range(9):
            self.board[8][i] = bottom_rank_pieces[i](8, i, 'sente')

        for i in range(9):
            self.board[6][i] = Pawn(6, i, 'sente')
        
        self.board[7][1] = Bishop(7, 1, 'sente')
        self.board[7][7] = Rook(7, 7, 'sente') 


        for i in range(9):
            self.board[0][i] = bottom_rank_pieces[i](0, i, 'gote')

        for i in range(9):
            self.board[2][i] = Pawn(2, i, 'gote')
        
        self.board[1][7] = Bishop(1, 7, 'gote')
        self.board[1][1] = Rook(1, 1, 'gote') 


    def render_pieces(self) -> None:

        for x in range(self.ranks):
            for y in range(self.files):
                if self.board[x][y] != 0:
                    WINDOW.blit(self.board[x][y].get_piece(), (self.board[x][y].get_piece_pos()))
    
