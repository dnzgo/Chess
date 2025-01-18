
from Piece import Pawn, Rook, Bishop, Knight, Queen, King
class GameState:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.current_player = "w"
        self.is_game_over = False
    
    def make_move(self, move):

        if self.is_game_over:                                               # after game over no moves allowed
            return
        
        piece_symbol = self.board[move.start_row][move.start_column]        # Get the piece being moved

        if self.current_player != piece_symbol[0]:                          #if current player is not equal piece color then can not be moved
            print("its not your piece")
            return
        if piece_symbol == "  ":                                            #if there is no piece in selected cell
            print("No piece at the starting square!")
            return
        
        piece = self.create_piece(piece_symbol)                             # creating an instance of the selected piece

        print(piece.symbol)

        if piece.is_valid_move(move.start_cell, move.end_cell, self.board): # Check if the move is valid
            self.board[move.start_row][move.start_column] = "  "            # Clear old position
            self.board[move.end_row][move.end_column] = move.piece_moved    # Update new position

            if self.is_in_check(piece_symbol[0]):                           # Check if the move leaves the king in check
                print("Move leaves your king in check! Invalid move.")
                
                self.undo_move(move)                                        # Undo the move
                return
            
            self.change_player()                                            # Change turn
            if self.is_checkmate(self.current_player):
                self.is_game_over = True
            if self.is_in_check(self.current_player):
                print(f"{self.current_player} is in check!")
        else:
            print("Invalid move!")

    def undo_move(self, move):
        self.board[move.start_row][move.start_column] = move.piece_moved
        self.board[move.end_row][move.end_column] = move.piece_captured

    def create_piece(self, symbol):
        
        piece_type = symbol[1]
        match piece_type:                                                   # create an object of the piece based on symbol
            case "P":
                return Pawn(symbol[0])
            case "R":
                return Rook(symbol[0])
            case "B":
                return Bishop(symbol[0])
            case "N":
                return Knight(symbol[0])
            case "Q":
                return Queen(symbol[0])
            case "K":
                return King(symbol[0])
            case _:
                return None 

    def is_in_check(self, color, board):
        # checks if the current players king is under attack
        # Find the king's position
        king = color + "K"
        king_position = None
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column] == king:
                    king_position = (row, column)
                    break
            if king_position:
                break

        opponent = "w" if color == "b" else "b"
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                piece_symbol = self.board[row][column]
                valid_moves = []
                if piece_symbol[0] == opponent:
                    piece = self.create_piece(piece_symbol)
                    valid_moves = piece.get_valid_moves((row, column), self.board)
                if king_position in valid_moves:
                    return True                                             # King is under attack
                    
        return False
    
    def is_checkmate(self, color):
        """
        Checks if the player of the given color is in checkmate.
        """
        if not self.is_in_check(color):                                     # If the king is not in check it is not checkmate.
            return False

        # Iterate through all the pieces of the given color
        for row in range(8):
            for column in range(8):
                piece_symbol = self.board[row][column]
                if piece_symbol[0] == color:                                # Check pieces of the given color
                    piece = self.create_piece(piece_symbol)
                    valid_moves = piece.get_valid_moves((row, column), self.board)
                    
                    # Simulate every move to see if the king can escape check
                    for move in valid_moves:
                        temp_board = [row.copy() for row in self.board]     # Create a temporary board
                        temp_board[move[0]][move[1]] = piece_symbol         # Simulate the move
                        temp_board[row][column] = "  "                      # Clear the original cell

                        if not self.is_in_check(color):                     # If this move gets the king out of check
                            return False

        # If no moves can get the king out of check it is checkmate
        return True


    def change_player(self):                                                # checking the current player and change it to other
        if self.current_player == "w":
            self.current_player = "b"
        else: self.current_player = "w"


class Move:
    def __init__(self, start_cell, end_cell, board):
        self.start_cell      = start_cell                                   # first cells location as x,y
        self.end_cell        = end_cell                                     # second cells location as x,y
        self.start_row       = start_cell[0]
        self.start_column    = start_cell[1]
        self.end_row         = end_cell[0]
        self.end_column      = end_cell[1]
        self.piece_moved     = board[self.start_cell[0]][self.start_cell[1]]# the symbol of piece that moved
        self.piece_captured  = board[self.end_cell[0]][self.end_cell[1]]    # the symbol of piece that captured