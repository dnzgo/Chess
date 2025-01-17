def test_checkmate_scenario():
    from Piece import Pawn, Rook, Bishop, Knight, Queen, King
    from chess import GameState, Move

    # Create game state
    game_state = GameState()

    # Set up a checkmate scenario
    game_state.board = [
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["wK", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["bQ", "  ", "  ", "  ", "  ", "  ", "  ", "bK"]
    ]

    # Check for black's checkmate
    if game_state.is_checkmate("b"):
        print("Checkmate confirmed!")
    else:
        print("Not checkmate!")

# Call the test function
test_checkmate_scenario()
