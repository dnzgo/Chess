
import chess
def test_is_in_check():
    # Create a GameState instance
    game_state = chess.GameState()

    # Test Case 1: Initial board state (no king in check)
    print("Test Case 1: Initial Board State")
    print("White in check:", game_state.is_in_check("w"))  # Expected: False
    print("Black in check:", game_state.is_in_check("b"))  # Expected: False

    # Test Case 2: Place a black rook to check the white king
    game_state.board = [
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "bR", "  ", "  ", "  "],  # Black rook
        ["  ", "  ", "  ", "  ", "wK", "  ", "  ", "  "],  # White king
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ]
    print("\nTest Case 2: Black rook attacking white king")
    print("White in check:", game_state.is_in_check("w"))  # Expected: True
    print("Black in check:", game_state.is_in_check("b"))  # Expected: False

    # Test Case 3: Place a white queen to check the black king
    game_state.board = [
        ["  ", "  ", "  ", "  ", "bK", "  ", "  ", "  "],  # Black king
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "wQ", "  ", "  ", "  "],  # White queen
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ]
    print("\nTest Case 3: White queen attacking black king")
    print("White in check:", game_state.is_in_check("w"))  # Expected: False
    print("Black in check:", game_state.is_in_check("b"))  # Expected: True

    # Test Case 4: No king on the board (edge case)
    game_state.board = [
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ]
    print("\nTest Case 4: No kings on the board")
    print("White in check:", game_state.is_in_check("w"))  # Expected: False
    print("Black in check:", game_state.is_in_check("b"))  # Expected: False
def test_get_valid_moves():
    game_state = chess.GameState()
    game_state.board = [
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "bR", "  ", "  ", "  "],  # Black rook
        ["  ", "  ", "  ", "  ", "wK", "  ", "  ", "  "],  # White king
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ]
    piece = game_state.create_piece("bR")

    print("Valid moves for bR:", piece.get_valid_moves((3,4), game_state.board))
    print("White in check:", game_state.is_in_check("w"))


# Run the tests
test_is_in_check()
#test_get_valid_moves()
