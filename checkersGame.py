import pygame
import math
import sys

PLAYER_1 = True
PLAYER_2 = False
FC = True

CURRENT_PIECE = 0
NEXT_PIECE = 0
X_CLICKS = 0
Y_CLICKS = 0
X1_CLICKS = 0
Y1_CLICKS = 0

CHOICES_SET = [[]]
TAKES_SET = [[]]

BOARD_STATE = [
    [0, 1, 0, 1, 0, 1, 0, 1],  # 0 represents an empty box, 1 represents a black piece
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 2, 0, 2, 0, 2, 0],  # 2 represents a white piece
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
]

def first_click(pos):
    global CURRENT_PIECE
    global X_CLICKS
    global Y_CLICKS
    mouse_x, mouse_y = pos
    X_CLICKS = mouse_y // SQUARE_SIZE
    Y_CLICKS = mouse_x // SQUARE_SIZE
    CURRENT_PIECE = BOARD_STATE[X_CLICKS][Y_CLICKS]

    if CURRENT_PIECE == 2 and PLAYER_1 == True:
        print(X_CLICKS, Y_CLICKS)
        return True
    elif CURRENT_PIECE == 1 and PLAYER_2 == True:
        return True
    else:
        return False

def second_click(pos):
    global NEXT_PIECE
    global FC
    global X1_CLICKS
    global Y1_CLICKS
    mouse_x, mouse_y = pos
    X1_CLICKS = mouse_y // SQUARE_SIZE
    Y1_CLICKS = mouse_x // SQUARE_SIZE
    NEXT_PIECE = (X1_CLICKS, Y1_CLICKS)

    if calculate_moves() == True:
        if NEXT_PIECE in CHOICES_SET:
            FC = True
            return True
    else:
        return False
            

def calculate_moves():
    global CHOICES_SET

    # Bottom-corners of the screen
    if (X_CLICKS == 0 or X_CLICKS == 7) and Y_CLICKS == 0: 
        if X_CLICKS == 0:
            print ("Move set 1 ")
            CHOICES_SET = [

                (X_CLICKS + 1, Y_CLICKS + 1)
            ]
            return True  

        elif X_CLICKS == 7:
            print ("Move set 2")
            CHOICES_SET = [

                (X_CLICKS - 1, Y_CLICKS + 1)
            ]   
            return True

    # Top-corners of the screen    
    elif (X_CLICKS == 0 or X_CLICKS == 7) and Y_CLICKS == 7: 
        if X_CLICKS == 0:
            print ("Move set 3")
            CHOICES_SET = [

                (X_CLICKS + 1, Y_CLICKS - 1)

            ]   
            return True
            
        elif X_CLICKS == 7:
            print ("Move set 4")
            CHOICES_SET = [

                (X_CLICKS - 1, Y_CLICKS - 1)

            ] 
            return True

    # Left of the screen    
    elif (X_CLICKS != 0 or X_CLICKS != 7) and Y_CLICKS == 0:
        print ("Move set 5")
        if (PLAYER_1 == True):
            CHOICES_SET = [

                (X_CLICKS - 1, Y_CLICKS + 1),

            ]
        elif (PLAYER_2 == True):
            CHOICES_SET = [

                (X_CLICKS + 1, Y_CLICKS + 1),

            ]
        return True

    # Right of the screen
    elif (X_CLICKS != 0 and X_CLICKS != 7) and Y_CLICKS == 7: 
        print ("Move set 6")

        if (PLAYER_1 == True and PLAYER_2 == False):
            CHOICES_SET = [

                (X_CLICKS - 1, Y_CLICKS - 1),

            ]
            return True
        elif (PLAYER_2 == True):
            CHOICES_SET = [

                (X_CLICKS + 1, Y_CLICKS - 1),

            ]
            return True
    
    #Top of the screen
    elif (0 < Y_CLICKS < 7) and X_CLICKS == 0: 
        print ("Move set 7")
        CHOICES_SET = [

            (X_CLICKS + 1, Y_CLICKS - 1),
            (X_CLICKS + 1, Y_CLICKS + 1)

        ]
        return True

    #Bottom of the screen
    elif (0 < Y_CLICKS < 7) and X_CLICKS == 7:
        print ("Move set 8") 
        CHOICES_SET = [

            (X_CLICKS - 1, Y_CLICKS - 1),
            (X_CLICKS - 1, Y_CLICKS + 1)

        ] 
        return True   

    else:
        print ("Move set 9 - ALL")
        if PLAYER_1 == True:
            CHOICES_SET = [

            (X_CLICKS - 1, Y_CLICKS - 1),
            (X_CLICKS - 1, Y_CLICKS + 1),
        ]
            return True
    
        elif PLAYER_2 == True:
            CHOICES_SET = [

            (X_CLICKS + 1, Y_CLICKS - 1),
            (X_CLICKS + 1, Y_CLICKS + 1)
        ]
        return True
        
def update_turns():
    global PLAYER_1
    global PLAYER_2

    Temp = PLAYER_1
    PLAYER_1 = PLAYER_2
    PLAYER_2 = Temp


def update_array():
    global CURRENT_PIECE
    global NEXT_PIECE
    global BOARD_STATE

    next = CURRENT_PIECE
    CURRENT_PIECE = 0

    BOARD_STATE[X_CLICKS][Y_CLICKS] = CURRENT_PIECE
    BOARD_STATE[X1_CLICKS][Y1_CLICKS] = next


# 3 Create the checkered board layout
def update_board():
    global BOARD_STATE
    for row in range(8):
        for col in range(8):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, BLUE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, BLACK, (x, y, SQUARE_SIZE, SQUARE_SIZE))

            if BOARD_STATE[row][col] == 1:
                piece_color = TAN
                pygame.draw.circle(
                    screen,
                    piece_color,
                    (x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2),
                    15,
                )
            elif BOARD_STATE[row][col] == 2:
                piece_color = WHITE
                pygame.draw.circle(
                    screen,
                    piece_color,
                    (x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2),
                    15,
                )
    pygame.display.flip()


# N We are going to update the game board through logic


# 1 We are going to initialize the game

pygame.init()
TWO_PLAYER_MODE = False
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SQUARE_SIZE = SCREEN_WIDTH // 8
CIRCLE_RADIUS = 20

WHITE = "#ffffff"
TAN = "#ffdc7c"
BLUE = "#e1f8fb"
BLACK = (0, 0, 0)

# N Defining the virtual board so we can update the actual board the user can see

rows = 8
col = 8


# 2 Create the game window and the main game loop

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Drodex's Checkerboard Game")
update_board()

# 4 Implement game logic functions -> Manage position of each piece; Validate each position move; Handle captures

Running = True
while Running:
    for event in pygame.event.get():
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and PLAYER_1 == True
            and FC == True
        ):
            if first_click(event.pos) == True:
                FC = False

        elif (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and PLAYER_1 == True
            and FC == False
        ):
            if second_click(event.pos) == True:
                FC = True

                update_array()
                update_board()
                update_turns()

        elif (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and PLAYER_2 == True
            and FC == True
        ):
            if first_click(event.pos) == True:
                FC = False
                
        elif (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and PLAYER_2 == True
            and FC == False
        ):
            if second_click(event.pos) == True:
                FC = True
                update_array()
                update_board()
                update_turns()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# 5 Handle user interaction -> detect mouse clicks and map them to  board positions; Validate moves; update game state; update the game board accordingly
