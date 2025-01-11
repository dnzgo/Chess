class Piece:
    def __init__(self, color, symbol):
        self.color = color                      # w / b
        self.symbol = symbol                    #  B K N P Q R

    def is_valid_move(self, start, end, board): # Override in subclasses
        raise
    def is_friendly_piece(self, board, row, column):
        if board[row][column][0] != self.color:
            return False
        return True

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, 'P')
    
    def is_valid_move(self, start, end, board):
        start_row, start_column = start
        end_row, end_column = end
        
        if self.color == "w":
            step = -1
        else: step = 1
        
        if start_column == end_column:                                                              # Moving forward
            if (end_row - start_row) == step and board[end_row][end_column] == "  ":
                return True                                                                         # Move forward one square
            elif (start_row == 6 and self.color == 'w') or (start_row == 1 and self.color == 'b'):
                if (end_row - start_row) == 2 * step and board[end_row][end_column] == "  ":
                    return True                                                                     # moving two squares forward for just first move
        elif abs(start_column - end_column) == 1 and (end_row - start_row) == step:                 # Capturing diagonally
            if board[end_row][end_column] != "  " and not self.is_friendly_piece(board, end_row, end_column):
                return True

        return False



class Rook(Piece):
    def __init__(self, color):
        super().__init__(color, 'R')

    def is_valid_move(self, start, end, board):
        start_row, start_column = start
        end_row, end_column = end
        if self.is_friendly_piece(board, end_row, end_column):
            return False
        if start_row == end_row :                       # Horizontal move
            if start_column < end_column :              # direction of the piece
                step = 1
            else: step = -1
            for column in range(start_column + step, end_column, step):
                if board[start_row][column] != "  ":    # if there is a piece between end pos and start pos it is an invalid move
                    return False 
            return True
        elif start_column == end_column:                # Vertical move
            if start_row < end_row:                     # direction of the piece
                step = 1
            else: step = -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_column] != "  ":    # checking if there is a piece in between positions
                    return False
            return True
        return False

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, 'N')

    def is_valid_move(self, start, end, board):
        start_row, start_column = start
        end_row, end_column = end
        if self.is_friendly_piece(board, end_row, end_column):
            return False
        if (abs(start_row - end_row) == 2 and abs(start_column - end_column) == 1) or \
           (abs(start_row - end_row) == 1 and abs(start_column - end_column) == 2):     # move L shape either 2 row 1 col or 1row 2 col
            return True
        return False
    
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color, 'B')
    
    def is_valid_move(self, start, end, board):
        start_row, start_column = start
        end_row, end_column = end
        if self.is_friendly_piece(board, end_row, end_column):
            return False
        if abs(start_row - end_row) == abs(start_column - end_column):
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_column > start_column else -1
            row, col = start_row + row_step, start_column + col_step
            while row != end_row and col != end_column:
                if board[row][col] != "  ":
                    return False                        # check if there is a piece between positions
                row += row_step
                col += col_step
            return True
        return False

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, 'Q')
    
    def is_valid_move(self, start, end, board):
        return Rook(self.color).is_valid_move(start, end, board) or \
               Bishop(self.color).is_valid_move(start, end, board)

class King(Piece):
    def __init__(self, color):
        super().__init__(color, 'K')
    
    def is_valid_move(self, start, end, board):
        start_row, start_column = start
        end_row, end_column = end
        if self.is_friendly_piece(board, end_row, end_column):
            return False
        if abs(start_row - end_row) <= 1 and abs(start_column - end_column) <= 1:
            return True
        return False

