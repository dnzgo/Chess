
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
    
    def make_move(self, move):
        
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
            self.change_player()                                            # Change turn
        else:
            print("Invalid move!")

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


    def change_player(self):                                                # checking the current player and change it to other
        if self.current_player == "w":
            self.current_player = "b"
        else: self.current_player = "w"


class Move:

    ranks_to_rows     = {"1" : 7, "2" : 6, "3" : 5, "4" : 4,
                         "5" : 3, "6" : 2, "7" : 1, "8": 0}
    rows_to_ranks     = {v : k for k, v in ranks_to_rows.items()}
    files_to_columns  = {"a" : 0, "b" : 1, "c" : 2, "d" : 3,
                         "e" : 4, "f" : 5, "g" : 6, "h": 7}
    columns_to_files  = {v : k for k, v in files_to_columns.items()}

    def __init__(self, start_cell, end_cell, board):
        self.start_cell      = start_cell                                   # first cells location as x,y
        self.end_cell        = end_cell                                     # second cells location as x,y
        self.start_row       = start_cell[0]
        self.start_column    = start_cell[1]
        self.end_row         = end_cell[0]
        self.end_column      = end_cell[1]
        self.piece_moved     = board[self.start_cell[0]][self.start_cell[1]]# the symbol of piece that moved
        self.piece_captured  = board[self.end_cell[0]][self.end_cell[1]]    # the symbol of piece that captured


    def get_chess_notation(self):                                           # pieces move notation as 'a2b3'
        return self.get_rank_file(self.start_row, self.start_column) + self.get_rank_file(self.end_row, self.end_column)
    
    def get_rank_file(self, row, column):
        return self.columns_to_files[column] + self.rows_to_ranks[row]