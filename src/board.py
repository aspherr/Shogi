import itertools
from const import WINDOW, MOVE_SFX, CAPTURE_SFX, CHECK_SFX

from pieces.pawn import Pawn
from pieces.lance import Lance
from pieces.knight import Knight
from pieces.silver_general import SilverGeneral
from pieces.gold_general import GoldGeneral
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.king import King

class Board:
    def __init__(self, ranks=9, files=9) -> None:
        self.ranks = ranks
        self.files = files
        self.board = [[0 for _ in range(ranks)] for _ in range(files)]
        self.init_board()

        self.current_player = "sente"
        self.game_over = False
        self.winner = ''
        self.reason_for_win = ''
        self.clicks = 0

    def notation(self, rank, file) -> str:
        ranks_dict = {
            "1": 8,
            "2": 7,
            "3": 6,
            "4": 5,
            "5": 4,
            "6": 3,
            "7": 2,
            "8": 1,
            "9": 0,
        }
        rank_notation = {value: rank_key for rank_key, value in ranks_dict.items()}

        files_dict = {
            "一": 0,
            "二": 1,
            "三": 2,
            "四": 3,
            "五": 4,
            "六": 5,
            "七": 6,
            "八": 7,
            "九": 8,
        }
        file_notation = {value: file_key for file_key, value in files_dict.items()}

        return rank_notation[rank] + file_notation[file]

    def init_board(self) -> None:
        bottom_rank_pieces = [
            Lance,
            Knight,
            SilverGeneral,
            GoldGeneral,
            King,
            GoldGeneral,
            SilverGeneral,
            Knight,
            Lance,
        ]
        
        for i in range(9):
            self.board[8][i] = bottom_rank_pieces[i](8, i, "sente")

        for i in range(9):
            self.board[6][i] = Pawn(6, i, "sente")  

        self.board[7][1] = Bishop(7, 1, "sente")  
        self.board[7][7] = Rook(7, 7, "sente")  

        for i in range(9):
            self.board[0][i] = bottom_rank_pieces[i](0, i, "gote")

        for i in range(9):
            self.board[2][i] = Pawn(2, i, "gote")  

        self.board[1][7] = Bishop(1, 7, "gote")  
        self.board[1][1] = Rook(1, 1, "gote")  

    def render_pieces(self) -> None:
        for x, y in itertools.product(range(self.ranks), range(self.files)):
            if self.board[x][y] != 0:
                WINDOW.blit(
                    self.board[x][y].get_piece(self.board),  
                    (self.board[x][y].get_piece_pos()),  
                )

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
        if self.current_player == "sente":
            self.current_player = "gote"

        else:
            self.current_player = "sente"

    def generate_moveset(self) -> list:
        moveset = []
        for x, y in itertools.product(range(self.ranks), range(self.files)):
            if self.board[x][y] != 0 and self.board[x][y].selected:  
                moveset.extend(iter(self.board[x][y].moveset(self.board)))  

        return moveset

    def generate_opp_moveset(self) -> list:
        moveset = []
        for x, y in itertools.product(range(self.ranks), range(self.files)):
            if self.board[x][y] != 0 and self.board[x][y].player != self.current_player:  
                moveset.extend(iter(self.board[x][y].moveset(self.board)))  

        return moveset

    def find_king(self) -> tuple:
        pos = (4, 8) if self.current_player == "sente" else (4, 0)
        for x, y in itertools.product(range(self.ranks), range(self.files)):
            if (
                self.board[x][y] != 0
                and self.board[x][y].player == self.current_player  
                and self.board[x][y].is_king is True  
            ):
                pos = (y, x)

        return pos

    def king_in_check(self) -> bool:
        king_pos = self.find_king()

        if king_pos in self.generate_opp_moveset():
            self.board[king_pos[1]][king_pos[0]].in_check = True
            return True

        elif (
            self.current_player != self.current_player
            or self.board[king_pos[1]][king_pos[0]].in_check
        ):
            self.board[king_pos[1]][king_pos[0]].in_check = False
            return False

        return False

    def check_restrictions(self, start_pos, end_pos, king_pos) -> bool:
        prev_check = self.king_in_check()
        self.generate_moveset()

        if self.king_in_check() or (prev_check is True and self.king_in_check()):
            pos = self.board[end_pos[0]][end_pos[1]]
            reset_pos = 0
            
            pos.update_img(start_pos)
            MOVE_SFX.stop()

            self.board[start_pos[0]][start_pos[1]] = pos
            self.board[end_pos[0]][end_pos[1]] = reset_pos
            
            if self.king_in_check():
                self.board[king_pos[1]][king_pos[0]].in_check = True
                    
            else:
                self.board[king_pos[1]][king_pos[0]].in_check = False

            return False
 
        return True
    
    def checkmate(self) -> bool:
        king_position = self.find_king()
        kings_moves = []

        for x, y in itertools.product(range(self.ranks), range(self.files)):
            if (
                self.board[x][y] != 0 and 
                str(self.board[x][y]) == 'king' and
                self.board[x][y].player == self.current_player):  
                kings_moves.extend(iter(self.board[x][y].moveset(self.board)))
                        
        safe_moves = []
        for move in self.generate_opp_moveset():
            if move not in kings_moves:
                safe_moves.append(move)

        if len(safe_moves) == 0:
            return True

        return False
    
    def move(self, start_pos, end_pos) -> bool:
        king_pos = self.find_king()
        pos = self.board[start_pos[0]][start_pos[1]]
        target_pos = self.board[end_pos[0]][end_pos[1]]
        reset_pos = 0

        pos.rank, pos.file = end_pos[0], end_pos[1]
        self.board[end_pos[0]][end_pos[1]] = pos
        self.board[start_pos[0]][start_pos[1]] = reset_pos

        valid_move = self.check_restrictions(start_pos, end_pos, king_pos)
        if not valid_move:            
            self.board[start_pos[0]][start_pos[1]] = pos
            self.board[end_pos[0]][end_pos[1]] = target_pos
            return False

        if (
            target_pos != 0
            and target_pos.player != self.current_player
            and str(target_pos) != "king"
        ):
            CAPTURE_SFX.play()
        
        else:
            MOVE_SFX.play()

        pos.update_img(end_pos)
        return True  

    def validate_move(self, rank, file, pos) -> None:
        self.generate_moveset()
        move_made = False

        moves = self.board[pos[0]][pos[1]].moveset(self.board)

        if (file, rank) in moves:
            move_made = self.move(pos, (rank, file))
            self.reset_selection()

        if move_made:
            self.change_turn()
            
            if self.checkmate():
                print(f"checkmate! {self.current_player} wins!")
                        
            elif self.king_in_check():
                MOVE_SFX.stop()
                CAPTURE_SFX.stop()
                CHECK_SFX.play()
                                        
        self.clicks = 0

    def selected(self, rank, file, pos) -> None:
        if (
            self.board[rank][file] != 0
            and self.board[rank][file].player == self.current_player
        ):
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
            self.validate_move(rank, file, pos)
            self.reset_selection()

    def play_move(self, rank, file) -> None:
        self.selected(rank, file, self.get_current_pos(rank, file))
