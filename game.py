import pygame
import chess

width       = 640
heigth      = 640
dimension   = 8
cell_size   = width // dimension
images      = {}
board_image = pygame.image.load("images/board.png")

def load_images():
    pieces = ["wP", "wB",  "wK", "wN", "wR", "wQ", "bP", "bB",  "bK", "bN", "bR", "bQ"]
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load("images/" + piece +".png"), (cell_size, cell_size))    # a dictionary for piece and piece image


# handling user input and updating graphics
def main():
    pygame.init()
    screen = pygame.display.set_mode((width, heigth))       #arranging the screen size
    pygame.display.set_caption("Chess by null")             #title of the screen
    game_state = chess.GameState()
    load_images()
    runnig = True
    selected_cell = ()                                      # last click of user (row, col)
    player_clicks = []                                      # players first and last click
    while runnig:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                   # if user close the screen
                runnig = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()           # getting the location of the click
                column = location[0] // cell_size
                row    = location[1] // cell_size
                if selected_cell == (row, column):
                    selected_cell = ()                      #if player clicks same cell twice  undo the selection
                    player_clicks = []
                else:
                    selected_cell = (row, column)
                    player_clicks.append(selected_cell)

                if len(player_clicks) == 2:
                    move = chess.Move(player_clicks[0], player_clicks[1], game_state.board)
                    game_state.make_move(move)
                    selected_cell = ()                      # after move clear the selection
                    player_clicks = []                      # after move clear the clicks
        draw_game_state(screen, game_state)
        pygame.display.flip()

# responsible for all the graphic changes
def draw_game_state(screen, game_state):
    draw_board(screen)                                      # drawing squares on the board 
    draw_pieces(screen, game_state.board)                   # add the pieces on the board with current game state

def draw_board(screen):
    screen.blit(board_image, (0, 0))                        # adding the background image to the game

def draw_pieces(screen, board):
    for row in range(dimension):
        for column in range(dimension):
            piece = board[row][column]
            if piece != "  ":                               # checking if there is a piece on the cell and show its image
                screen.blit(images[piece], pygame.Rect(column * cell_size,
                                                        row * cell_size, 
                                                        cell_size, cell_size))


main()