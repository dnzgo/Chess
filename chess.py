class GameState:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP","bP","bP","bP","bP","bP","bP"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["wP", "wP", "wP","wP","wP","wP","wP","wP","wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.current_player = "w"
    

    def make_move(self, move):
        self.board[move.start_row][move.start_column] = "  "                    #clear the old location of piece
        self.board[move.end_row][move.end_column]     = move.piece_moved        # put it to the new location
        self.change_player()                                                    #swapping player after move

    def change_player(self):
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
        self.start_row       = start_cell[0]
        self.start_column    = start_cell[1]
        self.end_row         = end_cell[0]
        self.end_column      = end_cell[1]
        self.piece_moved     = board[self.start_row][self.start_column]
        self.piece_captured  = board[self.end_row][self.end_column]


    def get_chess_notation(self):                   #pieces old cell and new cells locations as 'a2b3'
        return self.get_rank_file(self.start_row, self.start_column) + self.get_rank_file(self.end_row, self.end_column)
    
    def get_rank_file(self, row, column):
        return self.columns_to_files[column] + self.rows_to_ranks[row]