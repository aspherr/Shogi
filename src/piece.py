from const import *


class Piece:

    def __init__(self, rank, file, player) -> None:
        self.rank = rank
        self.file = file
        self.player = player

        self.selected = False


    def get_piece(self, board) -> pygame.image:
        
        if self.player == "sente":
            piece = SENTE_PIECES[self.id-1]
        
        else:
            piece = GOTE_PIECES[self.id-1]
        
        self.render_selection(board)
        return piece


    def get_piece_pos(self) -> int:
        
        x = int(BOARD_X + (self.file * BOARD_TILE_SIZE)) + 5
        y = int(BOARD_Y + (self.rank * BOARD_TILE_SIZE)) + 2

        return x, y


    def update_img(self, pos) -> None:
        
        self.rank = pos[0]
        self.file = pos[1]
    

    def boundaries(self, board) -> None:

        self.top = self.rank > TOP and (board[self.rank-1][self.file] == 0 or 
                                        board[self.rank-1][self.file] != 0)
        
        self.bottom = self.rank < BOTTOM and (board[self.rank+1][self.file] == 0 or
                                              board[self.rank+1][self.file] != 0)
        
        self.left = self.file > LEFT and (board[self.rank][self.file-1] == 0 or 
                                          board[self.rank][self.file-1] != 0)

        self.right = self.file < RIGHT and (board[self.rank][self.file+1] == 0 or
                                            board[self.rank][self.file+1] != 0)

        self.top_left = (self.rank > TOP and self.file > LEFT) and (board[self.rank-1][self.file-1] == 0 or
                                                                     board[self.rank-1][self.file-1] != 0)

        self.top_right = (self.rank > TOP and self.file < RIGHT) and (board[self.rank-1][self.file+1] == 0 or
                                                                      board[self.rank-1][self.file+1] != 0)
        
        self.bottom_left = (self.rank < BOTTOM and self.file > LEFT) and (board[self.rank+1][self.file-1] == 0 or
                                                                          board[self.rank+1][self.file-1] != 0)
        
        self.bottom_right = (self.rank < BOTTOM and self.file < RIGHT) and (board[self.rank+1][self.file+1] == 0 or
                                                                            board[self.rank+1][self.file+1] != 0)


    def generate_moves(self, board, moves, captures, condition, pos) -> None:

        print(condition)
        if condition is True:
            if board[pos[0]][pos[1]] == 0:
                moves.append((pos[1], pos[0]))
            
            elif board[pos[0]][pos[1]].player != self.player:
                moves.append((pos[1], pos[0]))
                captures.append((pos[0], pos[1]))
            

    def render_moves(self, board) -> None:

        moves, captures = self.moves(board)
        moves, captures =  list(moves), list(captures)

        for i in captures:
    
            if board[i[1]][i[0]] != 0 and (i[0], i[1]) in moves and board[i[1]][i[0]].player != self.player:
                x1 = int(BOARD_X + (i[1] * BOARD_TILE_SIZE)) + 1
                y1 = int(BOARD_Y + (i[0] * BOARD_TILE_SIZE)) + 1

                moves.remove((i[0] , i[1]))
                pygame.draw.rect(WINDOW, GREEN, (x1, y1, 60, 60), 1)
            
        for j in moves:
            x2 = int(BOARD_X + (j[0] * BOARD_TILE_SIZE)) + 1
            y2 = int(BOARD_Y + (j[1] * BOARD_TILE_SIZE)) + 1
            pygame.draw.rect(WINDOW, GREY2, (int(x2), int(y2), 60, 60), 0)


    def render_selection(self, board) -> None:

        if self.selected:
            pygame.draw.rect(
                WINDOW, GREY2, (self.get_piece_pos()[0]-4, self.get_piece_pos()[1]-1, 60, 60), 0
                )
            
            self.render_moves(board)
        

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
            tr_file, tl_file = self.file, self.file
            br_file, bl_file = self.file, self.file

            for a in range(self.rank, 0, -1):
                self.top_right = (a > TOP and tr_file < RIGHT) and (board[a-1][tr_file+1] == 0 or
                                                                    board[a-1][tr_file+1] != 0)
                
                self.generate_moves(board, moves, captures, self.top_right, (a-1, tr_file+1))
                if self.top_right is False or board[a-1][tr_file+1] != 0:
                    break

                tr_file += 1

            for b in range(self.rank, 0, -1):
                self.top_left = (b > TOP and tl_file > LEFT) and (board[b-1][tl_file-1] == 0 or
                                                                  board[b-1][tl_file-1] != 0)
                
                self.generate_moves(board, moves, captures, self.top_left, (b-1, tl_file-1))
                if self.top_left is False or board[b-1][tl_file-1] != 0:
                    break

                tl_file -= 1


            for c in range(self.rank, 8, +1):
                self.bottom_right = (c < BOTTOM and br_file < RIGHT) and (board[c+1][br_file+1] == 0 or
                                                                          board[c+1][br_file+1] != 0)
                
                self.generate_moves(board, moves, captures, self.bottom_right, (c+1, br_file+1))
                if self.bottom_right is False or board[c+1][br_file+1] != 0:
                    break

                br_file += 1

            for d in range(self.rank, 8, +1):
                self.bottom_left = (c < BOTTOM and bl_file > LEFT) and (board[d+1][bl_file-1] == 0 or
                                                                        board[d+1][bl_file-1] != 0)
                
                self.generate_moves(board, moves, captures, self.bottom_left, (d+1, bl_file-1))
                if self.bottom_left is False or board[d+1][bl_file-1] != 0:
                    break

                bl_file -= 1


        elif self.player == 'gote':
            tr_file, tl_file = self.file, self.file
            br_file, bl_file = self.file, self.file

            for a in range(self.rank, 0, -1):
                self.bottom_left = (a > TOP and bl_file < RIGHT) and (board[a-1][bl_file+1] == 0 or
                                                                      board[a-1][bl_file+1] != 0)
                
                self.generate_moves(board, moves, captures, self.bottom_left, (a-1, bl_file+1))
                if self.bottom_left is False or board[a-1][bl_file+1] != 0:
                    break

                bl_file += 1

            for b in range(self.rank, 0, -1):
                self.bottom_right = (b > TOP and br_file > LEFT) and (board[b-1][br_file-1] == 0 or
                                                                      board[b-1][br_file-1] != 0)
                
                self.generate_moves(board, moves, captures, self.bottom_right, (b-1, br_file-1))
                if self.bottom_right is False or board[b-1][br_file-1] != 0:
                    break

                br_file -= 1

            for c in range(self.rank, 8, +1):
                self.top_left = (c < BOTTOM and tl_file < RIGHT) and (board[c+1][tl_file+1] == 0 or
                                                                      board[c+1][tl_file+1] != 0)
                
                self.generate_moves(board, moves, captures, self.top_left, (c+1, tl_file+1))
                if self.top_left is False or board[c+1][tl_file+1] != 0:
                    break

                tl_file += 1

            for d in range(self.rank, 8, +1):
                self.top_right = (c < BOTTOM and tr_file > LEFT) and (board[d+1][tr_file-1] == 0 or
                                                                      board[d+1][tr_file-1] != 0)
                
                self.generate_moves(board, moves, captures, self.top_right, (d+1, tr_file-1))
                if self.top_right is False or board[d+1][tr_file-1] != 0:
                    break

                tr_file -= 1


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


    def moves(self, board):

        moves = []
        captures = []
        
        self.boundaries(board)
        if self.player == 'sente':
            conditions = [self.top, self.right, self.left, self.bottom,
                          self.top_right, self.top_left, self.bottom_right, self.bottom_left]

            pos = [(self.rank-1, self.file), (self.rank, self.file+1),
                   (self.rank, self.file-1), (self.rank+1, self.file),
                   (self.rank-1, self.file+1), (self.rank-1, self.file-1),
                   (self.rank+1, self.file+1), (self.rank+1, self.file-1)]

            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])
        
        elif self.player == 'gote':

            conditions = [self.top, self.right, self.left, self.bottom,
                          self.top_right, self.top_left, self.bottom_right, self.bottom_left]

            pos = [(self.rank-1, self.file), (self.rank, self.file+1),
                   (self.rank, self.file-1), (self.rank+1, self.file),
                   (self.rank-1, self.file+1), (self.rank-1, self.file-1),
                   (self.rank+1, self.file+1), (self.rank+1, self.file-1)]

            for i in range(len(conditions)):
                self.generate_moves(board, moves, captures, conditions[i], pos[i])
            
        return moves, captures
