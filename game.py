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
        images[piece] = pygame.image.load("images/" + piece +".png")


# handling user input and updating graphics
def main():
    pygame.init()
    screen = pygame.display.set_mode((width, heigth))
    pygame.display.set_caption("Chess by null")
    game_state = chess.GameState()
    load_images()
    runnig = True
    while runnig:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnig = False
        draw_game_state(screen, game_state)
        pygame.display.flip()

# responsible for all the graphic changes
def draw_game_state(screen, game_state):
    draw_board(screen)                      # drawing squares on the board 
    draw_pieces(screen, game_state.board)   # add the pieces on the board with current game state

def draw_board(screen):
    screen.blit(board_image, (0, 0))

def draw_pieces(screen, board):
    for row in range(dimension):
        for column in range(dimension):
            piece = board[row][column]
            if piece != "  ":
                screen.blit(images[piece], pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size))


main()