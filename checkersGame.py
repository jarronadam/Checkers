import pygame
import sys

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SQUARE_SIZE = SCREEN_WIDTH // 8
WHITE_PIECE = 1
BLACK_PIECE = 2

# Colors
WHITE = "#ffffff"
TAN = "#ffdc7c"
BLUE = "#e1f8fb"
BLACK = (0, 0, 0)


class Game:
    def __init__(self):
        self.board = [
            [0, BLACK_PIECE, 0, BLACK_PIECE, 0, BLACK_PIECE, 0, BLACK_PIECE],
            [BLACK_PIECE, 0, BLACK_PIECE, 0, BLACK_PIECE, 0, BLACK_PIECE, 0],
            [0, BLACK_PIECE, 0, BLACK_PIECE, 0, BLACK_PIECE, 0, BLACK_PIECE],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [WHITE_PIECE, 0, WHITE_PIECE, 0, WHITE_PIECE, 0, WHITE_PIECE, 0],
            [0, WHITE_PIECE, 0, WHITE_PIECE, 0, WHITE_PIECE, 0, WHITE_PIECE],
            [WHITE_PIECE, 0, WHITE_PIECE, 0, WHITE_PIECE, 0, WHITE_PIECE, 0],
        ]
        self.current_player = WHITE_PIECE
        self.selected_piece = None
        self.valid_moves = []

    def switch_player(self):
        self.current_player = (
            WHITE_PIECE if self.current_player == BLACK_PIECE else BLACK_PIECE
        )

    def select_piece(self, row, col):
        if self.current_player == WHITE_PIECE:
            if self.board[row][col] == WHITE_PIECE:
                self.select_piece = self.board[row][col]
        pass


    def move_piece(self, row, col):
        pass

    def update_board(self, screen):
        for row in range(8):
            for col in range(8):
                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE
                color = BLUE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

                piece = self.board[row][col]
                if piece != 0:
                    piece_color = TAN if piece == WHITE_PIECE else WHITE
                    pygame.draw.circle(
                        screen,
                        piece_color,
                        (x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2),
                        15,
                    )


# Initialize the game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Checkers Game")
game = Game()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
            game.select_piece(row, col)

        if event.type == pygame.QUIT:
            running = False

    game.update_board(screen)
    pygame.display.flip()

pygame.quit()
