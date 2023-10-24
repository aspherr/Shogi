import itertools
from const import *
from piece import Pawn, Lance, Knight, SilverGeneral, GoldGeneral, Bishop, Rook, King


class Board:

    def __init__(self, ranks = 9, files = 9) -> None:
        self.ranks = ranks
        self.files = files
        self.board = [[0 for _ in range(ranks)] for _ in range(files)]
        self.init_board()

        self.current_player = 'sente'
        self.clicks = 0


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

        for x, y in itertools.product(range(self.ranks), range(self.files)):
            if self.board[x][y] != 0:
                    WINDOW.blit(self.board[x][y].get_piece(self.board), (self.board[x][y].get_piece_pos()))
    

    def selected(self, rank, file, pos) -> None:

        if (self.board[rank][file] != 0 
                and self.board[rank][file].player == self.current_player):
            
            self.reset_selection()
            self.board[rank][file].selected = True

            if self.board[pos[0]][pos[1]] != self.board[rank][file]:
                self.clicks = 1
            
            else:
                self.clicks += 1
            
            if self.clicks == 2:
                self.clicks = 0
                self.reset_selection()
        
        elif pos != (rank, file):
            self.clicks += 1
            self.move(pos, (rank, file))
            self.reset_selection()
        
    
    def reset_selection(self) -> None:

        for x, y in itertools.product(range(self.ranks), range(self.files)):
            if self.board[x][y] != 0:
                self.board[x][y].selected = False
    

    def get_current_pos(self, rank, file) -> tuple:

        pos = rank, file
        for x, y in itertools.product(range(self.ranks), range(self.files)):
            if self.board[x][y] != 0 and self.board[x][y].selected is True:
                pos = x, y
            
        return pos


    def change_turn(self) -> None:

        if self.current_player == 'sente':
            self.current_player = 'gote'
        
        else:
            self.current_player = 'sente'


    def move(self, start_pos, end_pos) -> None:
        
        pos = self.board[start_pos[0]][start_pos[1]]
        reset_pos = 0

        pos.rank, pos.file = end_pos[0], end_pos[1]
        
        self.board[end_pos[0]][end_pos[1]] = pos
        self.board[start_pos[0]][start_pos[1]] = reset_pos

        pos.update_img(end_pos)


    def play_move(self, rank, file) -> None:
        
        self.selected(rank, file, self.get_current_pos(rank, file))

