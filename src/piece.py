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
    

    def boundaries(self, board) -> None:

        self.top = self.rank > TOP and (board[self.rank-1][self.file] == 0 or 
                                        board[self.rank-1][self.file] != 0)
        
        self.bottom = self.rank < BOTTOM and (board[self.rank+1][self.file] or
                                              board[self.rank+1][self.file])
        
        self.left = self.file > LEFT and (board[self.rank][self.file-1] or 
                                          board[self.rank][self.file-1])

        self.right = self.file < RIGHT and (board[self.rank][self.file+1] or
                                            board[self.rank][self.file+1])

        self.top_left = (self.rank > TOP and self.file > LEFT) and (board[self.rank-1][self.file-1] or
                                                                     board[self.rank-1][self.file-1])

        self.top_right = (self.rank > TOP and self.file < RIGHT) and (board[self.rank-1][self.file+1] or
                                                                      board[self.rank-1][self.file+1])
        
        self.bottom_left = (self.rank < BOTTOM and self.file > LEFT) and (board[self.rank+1][self.file-1] or
                                                                          board[self.rank+1][self.file-1])
        
        self.bottom_right = (self.rank < BOTTOM and self.file < RIGHT) and (board[self.rank+1][self.file+1] or
                                                                            board[self.rank+1][self.file+1])


    def generate_moves(self, board, moves, captures, condition, pos) -> None:

        if condition is True:
            if board[pos[0]][pos[1]] == 0:
                moves.append((pos[1], pos[0]))
            
            elif board[pos[0]][pos[1]].player != self.player:
                moves.append((pos[1], pos[0]))
                captures.append((pos[0], pos[1]))



class Pawn(Piece):
    id = 1
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Pawn'
    

    def moves(self, board):

        moves = []
        captures = []
        
        self.boundaries(board)
        if self.player == 'sente':
            self.generate_moves(board, moves, captures, self.top, (self.rank-1, self.file))
            
        elif self.player == 'gote':
            self.generate_moves(board, moves, captures, self.bottom, (self.rank+1, self.file))

        return moves, captures


class Lance(Piece):
    id = 2
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Lance'
    

    def moves(self, board):

        moves = []
        captures = []
        
        if self.player == 'sente':
            for i in range(self.rank, 0, -1):
                
                self.top = self.rank > TOP and (board[i-1][self.file] == 0 or
                                                board[i-1][self.file] != 0)

                self.generate_moves(board, moves, captures, self.top, (i-1, self.file))
                if board[i-1][self.file] != 0:
                    break
        
        elif self.player == 'gote':
            for i in range(self.rank, 8, +1):
                
                self.top = self.rank > TOP and (board[i+1][self.file] == 0 or
                                                board[i+1][self.file] != 0)

                self.generate_moves(board, moves, captures, self.top, (i+1, self.file))
                if board[i+1][self.file] != 0:
                    break

        return moves, captures
    

class Knight(Piece):
    id = 3
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Knight'


    def moves(self, board):

        moves = []
        captures = []

        self.top_right = self.rank > TOP and self.file < RIGHT and (board[self.rank-2][self.file+1] == 0 or
                                                                     board[self.rank-2][self.file+1] != 0)

        self.top_left = self.rank > TOP and self.file > LEFT and (board[self.rank - 2][self.file - 1] == 0 or 
                                                                    board[self.rank - 2][self.file - 1] != 0)
        
        self.bottom_right = self.rank < BOTTOM and self.file < RIGHT and (self.board[self.rank+2][self.file+1] == 0 or
                                                                          board[self.rank+2][self.file+1] != 0)

        self.bottom_left = self.rank < BOTTOM and self.file > LEFT and (board[self.rank+2][self.file-1] == 0 or 
                                                                        board[self.rank+2][self.file-1] != 0)
        
        if self.player == 'sente':
            conditions = [self.top_right, self.top_left]
            pos = [(self.rank-2, self.file+1), (self.rank-2, self.file-1)]
            
            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])

        
        elif self.player == 'gote':
            conditions = [self.bottom_right, self.bottom_left]
            pos = [(self.rank+2, self.file+1), (self.rank+2, self.file-1)]
            
            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])


        return moves, captures
    

class SilverGeneral(Piece):
    id = 4
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Silver General'


    def moves(self, board):

        moves = []
        captures = []
        
        self.boundaries(board)
        if self.player == 'sente':
            conditions = [self.top, self.top_right, self.top_left, self.bottom_right, self.bottom_left]
            pos = [(self.rank-1, self.file), (self.rank-1, self.file+1), (self.rank-1, self.file-1), 
                   (self.rank+1, self.file+1), (self.rank+1, self.file-1)]
            
            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])

        
        elif self.player == 'gote':
            conditions = [self.bottom, self.bottom_left, self.bottom_right, self.top_left, self.top_right]
            pos = [(self.rank+1, self.file), (self.rank+1, self.file-1), (self.rank+1, self.file+1),
                   (self.rank-1, self.file-1), (self.rank-1, self.file+1)]
            
            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])

        return moves, captures


class GoldGeneral(Piece):
    id = 5
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Gold General'


    def moves(self, board):

        moves = []
        captures = []
        
        self.boundaries(board)
        if self.player == 'sente':
            conditions = [self.top, self.right, self.left, self.bottom, self.top_right, self.top_left]
            pos = [(self.rank-1, self.file), (self.rank, self.file+1), (self.rank, self.file-1),
                   (self.rank+1, self.file), (self.rank-1, self.file+1), (self.rank-1, self.file-1)]
            
            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])

        
        elif self.player == 'gote':
            conditions = [self.bottom, self.left, self.right, self.top, self.bottom_left, self.bottom_right]
            pos = [(self.rank+1, self.file), (self.rank, self.file-1), (self.rank, self.file+1),
                   (self.rank-1, self.file), (self.rank+1, self.file-1), (self.rank+1, self.file+1)]
            
            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])

        return moves, captures
    

class Bishop(Piece):
    id = 6
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Bishop'


    def moves(self, board):

        moves = []
        captures = []
        
        if self.player == 'sente':
            for i in range(self.rank, 0, -1):
                
                right_file = self.file
                self.top_right = (i > TOP and right_file < RIGHT) and (board[i-1][right_file+1] == 0 or
                                                                       board[i-1][right_file+1] != 0)

                self.generate_moves(board, moves, captures, self.top_right, (i-1, right_file+1))
                if self.top_right is False or board[i-1][right_file+1] != 0:
                    break

                right_file += 1
            
            for i in range(self.rank, 0, -1):
                
                left_file = self.file
                self.top_left = (i > TOP and left_file > LEFT) and (board[i-1][left_file-1] == 0 or
                                                                    board[i-1][left_file-1] != 0)

                self.generate_moves(board, moves, captures, self.top_left, (i-1, left_file-1))
                if self.top_left is False or board[i-1][left_file+1] != 0:
                    break

                left_file -= 1
            
            for i in range(self.file, 8, +1):
                
                right_file = self.file
                self.bottom_right = (i < BOTTOM and right_file < RIGHT) and (board[i+1][right_file+1] == 0 or
                                                                             board[i+1][right_file+1] != 0)

                self.generate_moves(board, moves, captures, self.bottom_right, (i-1, right_file-1))
                if self.bottom_right is False or board[i+1][right_file+1] != 0:
                    break

                right_file += 1
            
            for i in range(self.file, 8, +1):
                
                left_file = self.file
                self.bottom_left = (i < BOTTOM and left_file > LEFT) and (board[i+1][left_file-1] == 0 or 
                                                                          board[i+1][left_file-1] != 0)

                self.generate_moves(board, moves, captures, self.bottom_left, (i+1, left_file-1))
                if self.bottom_left is False or board[i+1][left_file-1] != 0:
                    break

                left_file -= 1

        
        elif self.player == 'gote':
            for i in range(self.file, 8, +1):
                
                right_file = self.file
                self.top_right = (i < BOTTOM and right_file > LEFT) and (board[i-1][right_file+1] == 0 or 
                                                                         board[i-1][right_file+1] != 0)

                self.generate_moves(board, moves, captures, self.top_right, (i-1, right_file+1))
                if self.top_right is False or board[i+1][right_file-1] != 0:
                    break

                right_file -= 1
            
            for i in range(self.file, 8, +1):
                
                left_file = self.file
                self.top_left = (i < BOTTOM and left_file < RIGHT) and (board[i-1][left_file-1] == 0 or 
                                                                        board[i-1][left_file-1] != 0)

                self.generate_moves(board, moves, captures, self.top_left, (i-1, right_file-1))
                if self.top_left is False or board[i+1][left_file+1] != 0:
                    break

                left_file += 1

            for i in range(self.rank, 0, -1):

                right_file = self.file
                self.bottom_right = (i > TOP and right_file > LEFT) and (board[i+1][right_file+1] == 0 or 
                                                                         board[i+1][right_file+1] != 0)

                self.generate_moves(board, moves, captures, self.bottom_right, (i+1, right_file+1))
                if self.bottom_right is False or board[i+1][right_file+1] != 0:
                    break

                right_file -= 1

            for i in range(self.rank, 0, -1):
                
                left_file = self.file
                self.bottom_left = (i > TOP and left_file < RIGHT) and (board[i+1][left_file-1] == 0 or 
                                                                        board[i+1][left_file-1] != 0)

                self.generate_moves(board, moves, captures, self.bottom_left, (i+1, left_file-1))
                if self.bottom_left is False or board[i+1][left_file-1] != 0:
                    break

                left_file += 1

        return moves, captures

    
class Rook(Piece):
    id = 7
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'Rook'


    def moves(self, board):

        moves = []
        captures = []
        
        if self.player == 'sente':
            for i in range(self.rank, 0, -1):
                
                self.top = self.rank > TOP and (board[i-1][self.file] == 0 or
                                                board[i-1][self.file] != 0)

                self.generate_moves(board, moves, captures, self.top, (i-1, self.file))
                if board[i-1][self.file] != 0:
                    break
            
            for i in range(self.rank, 8, +1):
                
                self.bottom = self.rank < BOTTOM and (board[i+1][self.file] == 0 or 
                                                      board[i+1][self.file] != 0)

                self.generate_moves(board, moves, captures, self.bottom, (i+1, self.file))
                if board[i+1][self.file] != 0:
                    break
            
            for i in range(self.file, 0, -1):
                
                self.left = self.file > LEFT and (board[self.rank][i-1] == 0 or
                                                  board[self.rank][i-1] != 0)

                self.generate_moves(board, moves, captures, self.left, (self.rank, i-1))
                if board[self.rank][i-1] != 0:
                    break
            
            for i in range(self.file, 8, +1):
                
                self.right = self.rank > TOP and (board[self.rank][i+1] == 0 or
                                                  board[self.rank][i+1] != 0)

                self.generate_moves(board, moves, captures, self.right, (self.rank, i+1))
                if board[self.rank][i+1] != 0:
                    break

        
        elif self.player == 'gote':
            for i in range(self.rank, 0, -1):

                self.top = self.rank < BOTTOM and (board[i+1][self.file] == 0 or 
                                                      board[i+1][self.file] != 0)

                self.generate_moves(board, moves, captures, self.top, (i+1, self.file))
                if board[i+1][self.file] != 0:
                    break
                
            for i in range(self.rank, 8, +1):
                
                self.bottom = self.rank > TOP and (board[i-1][self.file] == 0 or
                                                board[i-1][self.file] != 0)

                self.generate_moves(board, moves, captures, self.bottom, (i-1, self.file))
                if board[i-1][self.file] != 0:
                    break
            
            for i in range(self.file, 0, -1):

                self.left = self.rank > TOP and (board[self.rank][i+1] == 0 or
                                                  board[self.rank][i+1] != 0)

                self.generate_moves(board, moves, captures, self.left, (self.rank, i+1))
                if board[self.rank][i+1] != 0:
                    break
                            
            for i in range(self.file, 8, +1):
                
                self.right = self.file > LEFT and (board[self.rank][i-1] == 0 or
                                                  board[self.rank][i-1] != 0)

                self.generate_moves(board, moves, captures, self.right, (self.rank, i-1))
                if board[self.rank][i-1] != 0:
                    break

        return moves, captures


class King(Piece):
    id = 8
    def __init__(self, rank, file, player) -> None:
        super().__init__(rank, file, player)
    

    def __repr__(self) -> str:
        return 'King'

