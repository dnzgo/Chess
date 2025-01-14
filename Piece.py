class Piece:
    def __init__(self, color, symbol):
        self.color = color                      # w / b
        self.symbol = symbol                    #  B K N P Q R
        self.valid_moves = []
    def get_valid_moves(self, start, board):
        raise
    def is_valid_move(self, start, end, board): # Override in subclasses
        raise
    def is_friendly_piece(self, board, row, column):
        if board[row][column][0] != self.color:
            return False
        return True

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, 'P')
        self.valid_moves = []
    
    def get_valid_moves(self, start, board):
        start_row, start_column = start
        if self.color == "w":
            step = -1
        else: step = 1
        # Forward moves
        if 0 <= start_row + step < 8 and board[start_row + step][start_column] == "  ":             # check if forward first cell is empty
            self.valid_moves.append((start_row + step, start_column))
            if (self.color == "w" and start_row == 6) or (self.color == "b" and start_row == 1):    # check if pawn did not move before and can move 2 cell forward
                if board[start_row + 2* step][start_column] == "  ":
                    self.valid_moves.append((start_row + 2* step, start_column))
        # Captures
        for offset in [-1, 1]:
            new_column = start_column + offset
            if 0 <= start_row + step < 8 and 0 <= new_column < 8:
                if board[start_row + step][new_column] != "  ":                                     # if diagonal cell is not empty
                    opponent = board[start_row + step][new_column]
                    if self.color != opponent[0]:                                                   #if diogonal cell is not contains opponent
                        self.valid_moves.append((start_row + step, new_column))
        return self.valid_moves
    
    def is_valid_move(self, start, end, board):
        end_row, end_column = end
        
        if (end_row, end_column) in self.get_valid_moves(start, board):                             # if move is in valid moves list
            return True
        return False



class Rook(Piece):
    def __init__(self, color):
        super().__init__(color, 'R')
        self.valid_moves = []                                   # empty the list

    def get_valid_moves(self, start, board):
        start_row, start_column = start

        # Horizontal and vertical moves
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right left down up
        for dir_row, dir_column in directions:
            row, column = start_row, start_column
            while 0 <= row + dir_row < 8 and 0 <= column + dir_column < 8:
                row += dir_row
                column += dir_column
                if board[row][column] == "  ":
                    self.valid_moves.append((row, column))
                else:
                    if self.color != board[row][column][0]:  # Opponent piece
                        self.valid_moves.append((row, column))
                    break
        return self.valid_moves


    def is_valid_move(self, start, end, board):
        end_row, end_column = end
        
        if (end_row, end_column) in self.get_valid_moves(start, board):                             # if move is in valid moves list
            return True
        return False

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, 'N')
        self.valid_moves = []
    
    def get_valid_moves(self, start, board):
        
        start_row, start_column = start
        # All possible L-shaped moves
        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        for dir_row, dir_column in moves:
            row, column = start_row + dir_row, start_column + dir_column
            if 0 <= row < 8 and 0 <= column < 8:
                if board[row][column] == "  " or self.color != board[row][column][0]:
                    self.valid_moves.append((row, column))
        return self.valid_moves

    def is_valid_move(self, start, end, board):
        end_row, end_column = end
        
        if (end_row, end_column) in self.get_valid_moves(start, board):                             # if move is in valid moves list
            return True
        return False
    
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color, 'B')
        self.valid_moves = []

    def get_valid_moves(self, start, board):
        
        start_row, start_column = start

        # Diagonal moves
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Bottom-right, Bottom-left, Top-right, Top-left
        for dir_row, dir_column in directions:
            row, column = start_row, start_column
            while 0 <= row + dir_row < 8 and 0 <= column + dir_column < 8:
                row += dir_row
                column += dir_column
                if board[row][column] == "  ":
                    self.valid_moves.append((row, column))
                else:
                    if self.color != board[row][column][0]:  # Opponent piece
                        self.valid_moves.append((row, column))
                    break
        return self.valid_moves
    
    def is_valid_move(self, start, end, board):
        end_row, end_column = end
        
        if (end_row, end_column) in self.get_valid_moves(start, board):                             # if move is in valid moves list
            return True
        return False

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, 'Q')
        self.valid_moves = []

    def get_valid_moves(self, start, board):
        # Queen combines Rook and Bishop moves
        rook_moves = Rook(self.color).get_valid_moves(start, board)
        bishop_moves = Bishop(self.color).get_valid_moves(start, board)
        self.valid_moves = rook_moves + bishop_moves
        return self.valid_moves
    
    def is_valid_move(self, start, end, board):
        end_row, end_column = end
        
        if (end_row, end_column) in self.get_valid_moves(start, board):                             # if move is in valid moves list
            return True
        return False

class King(Piece):
    def __init__(self, color):
        super().__init__(color, 'K')
        self.valid_moves = []

    def get_valid_moves(self, start, board):
        start_row, start_column = start
        # All possible one-step moves
        moves = [
            (1, 0), (-1, 0), (0, 1), (0, -1), 
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        for dir_row, dir_column in moves:
            row, column = start_row + dir_row, start_column + dir_column
            if 0 <= row < 8 and 0 <= column < 8:
                if board[row][column] == "  " or self.color != board[row][column][0]:
                    self.valid_moves.append((row, column))
        return self.valid_moves
    
    def is_valid_move(self, start, end, board):
        end_row, end_column = end
        
        if (end_row, end_column) in self.get_valid_moves(start, board):                             # if move is in valid moves list
            return True
        return False
