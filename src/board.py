import itertools
from typing import Tuple
from const import WINDOW, MOVE_SFX, CAPTURE_SFX, CHECK_SFX, SENTE_PIECES, GOTE_PIECES, KOMA1_X, KOMA2_X

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
        
        self.sente_captures = {"Pawn":[],'Lance':[],'Knight':[],'Silver General':[],'Gold General':[],'Bishop':[],'Rook':[]}

        for i in range(9):
            self.board[0][i] = bottom_rank_pieces[i](0, i, "gote")

        for i in range(9):
            self.board[2][i] = Pawn(2, i, "gote")  

        self.board[1][7] = Bishop(1, 7, "gote")  
        self.board[1][1] = Rook(1, 1, "gote")
        
        self.gote_captures = {"Pawn":[],'Lance':[],'Knight':[],'Silver General':[],'Gold General':[],'Bishop':[],'Rook':[]}
        
        
        self.captured_pieces = {"sente": self.sente_captures, "gote": self.gote_captures}
        self.captured_select = [[0],[0],[0],[0],[0],[0],[0]]
        
    def render_pieces(self, moves) -> None:
        for x, y in itertools.product(range(self.ranks), range(self.files)):
            if self.board[x][y] != 0:
                WINDOW.blit(
                    self.board[x][y].get_piece(self.board),  
                    (self.board[x][y].get_piece_pos()),  
                )
                
        players = ["sente", "gote"]
        for player in players:
            for capture in self.captured_pieces.get(player):
                if len(self.captured_pieces.get(player).get(capture)) > 0:
                    
                    if player == 'sente':
                        piece, position = self.get_sente(88, capture, 61)
                        
                    else:
                        piece, position = self.get_gote(220, capture, 61) 
                    
                    self.captured_pieces.get(player).get(capture)[0].render_koma_pieces(piece, position, moves)
                    
    def get_sente(self, base, capture, offset) -> Tuple[str, int]:
        match capture:
            case 'Pawn':
                piece = SENTE_PIECES[0]
                base += (6*offset)
            
            case 'Lance':
                piece = SENTE_PIECES[1]
                base += (5*offset)
            
            case 'Silver General':
                piece = SENTE_PIECES[3]
                base += (3*offset)
            
            case 'Gold General':
                piece = SENTE_PIECES[4]
                base += (2*offset)
            
            case 'Rook':
                piece = SENTE_PIECES[6]
            
            case 'Knight':
                piece = SENTE_PIECES[2]
                base += (4*offset)
            
            case 'Bishop':
                piece = SENTE_PIECES[5]
                base += (1*offset)
        
        return piece, (int(KOMA1_X) + 5, base)
                
                
    def get_gote(self, base, capture, offset) -> Tuple[str, int]:
        match capture:
            case 'Pawn':
                piece = GOTE_PIECES[0]
                
            case 'Lance':
                piece = GOTE_PIECES[1]
                base += (1*offset)
            
            case 'Silver General':
                piece = GOTE_PIECES[3]
                base += (3*offset)
            
            case 'Gold General':
                piece = GOTE_PIECES[4]
                base += (4*offset)
            
            case 'Rook':
                piece = GOTE_PIECES[6]
                base += (6*offset)
            
            case 'Knight':
                piece = GOTE_PIECES[2]
                base += (2*offset)
            
            case 'Bishop':
                piece = GOTE_PIECES[5]
                base += (5*offset)
                
        return piece, (int(KOMA2_X) + 5, base)
                
    def reset_selection(self) -> None:
        for x, y in itertools.product(range(self.ranks), range(self.files)):
            if self.board[x][y] != 0:
                self.board[x][y].selected = False
        
        self.captured_select = [False, False, False, False, False, False, False] 

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
        
        self.captured_select = [False, False, False, False, False, False, False]
        
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
            new_capture = target_pos          
            new_capture.player = self.current_player
            self.captured_pieces.get(self.current_player).get(str(new_capture)).append(new_capture)
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
          
            
    def in_koma(self, koma, piece) -> bool:
        return piece in koma
        
    def valid_drop(self) -> bool:
        return [(x, y) for x, y in itertools.product(range(self.ranks), range(self.files)) if self.board[x][y] == 0]

    def reset_koma_selection(self, rank, pieces) -> None:
        for i in range(len(self.captured_select)-1):
            if i == rank:
                continue    
            
            if self.captured_select[i]:
                character = pieces[i]
                self.captured_pieces[self.current_player][character][0].koma_selected = False
                break
        
    def komadai_selection(self, index, players, pieces, rank) -> None:
            
        if (self.current_player == players["sente"] and index == 0):
            
            piece = pieces[rank]
                        
            if len(self.captured_pieces[self.current_player][piece]) > 0:
                if self.captured_select[rank]:
                    self.captured_pieces[self.current_player][piece][0].koma_selected = False

                else: 
                    self.captured_pieces[self.current_player][piece][0].koma_selected = True    
                    self.reset_koma_selection(rank, pieces) 
                    self.reset_selection()

                self.captured_select[rank] = not self.captured_select[rank]


        elif self.current_player == players["gote"] and index == 1:
            piece = pieces[-(rank-6)]            

            if len(self.captured_pieces[self.current_player][piece]) > 0:
                if self.captured_select[-(rank-6)]:
                    self.captured_pieces[self.current_player][piece][0].koma_selected = False

                else:
                    self.captured_pieces[self.current_player][piece][0].koma_selected = True
                    self.reset_koma_selection(-(rank-6), pieces)  
                    self.reset_selection()

                self.captured_select[-(rank-6)] = not self.captured_select[-(rank-6)]

    def reinstate_piece(self, index, rank, file) -> None:
        players = {"sente": "gote", "gote": "sente"}
        pieces = ('Pawn', 'Lance', 'Knight', 'Silver General', 'Gold General', 'Bishop', 'Rook')

        if self.in_koma(self.captured_select, True) and file != 7 and index == 10:
            select = self.captured_select.index(True)
            piece = pieces[select]
                                
            if (rank, file) in self.valid_drop():
                self.captured_pieces[self.current_player][piece][0].koma_selected = False                    
                piece_draw = self.captured_pieces[self.current_player][piece].pop()

                self.board[rank][file] = piece_draw
                piece_draw.rank, piece_draw.file = rank, file
                MOVE_SFX.play()
                
                self.checkmate()

                self.captured_select[select] = False
                self.change_turn() 
                return

        self.komadai_selection(index, players, pieces, rank)
        
    def play_move(self, rank, file) -> None:
        self.selected(rank, file, self.get_current_pos(rank, file))
        self.reinstate_piece(10, rank, file)
