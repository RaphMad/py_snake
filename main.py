import pygame

from game.board import *
from game.snake import *
from game.info_screen import *

# size of the header (used for displaying info)
header_size = 50

# size of the game area (px, square field)
size = 800

# number of blocks per side (should evenly divide the overall size)
blocks_per_side = 50

# controls the main loop
is_running = True

pygame.init()
pygame.display.set_caption("PySnake")

window = pygame.display.set_mode((size, header_size + size))
board = Board(window.subsurface(pygame.Rect(0, header_size, size, size)), blocks_per_side)
info_screen = InfoScreen(window.subsurface(pygame.Rect(0, 0, size, header_size)))
snake = Snake(board, 10, 10, Direction.RIGHT)


def game_loop():

    eventHandlers = {
        pygame.QUIT: quitGame,
        pygame.KEYDOWN: change_snake_facing
    }

    global snake
    global info_screen
    clock = pygame.time.Clock()

    while is_running:
        pygame.display.update()
        events = pygame.event.get()

        if (events):
            events.reverse()
            for eventType in eventHandlers:
                # only process the last event of a given type (e.g. only the last keypress in case of multiple ones)
                last_event_of_type = next(
                    (x for x in events if x.type == eventType),
                    None
                )

                if (last_event_of_type):
                    eventHandlers[eventType](last_event_of_type)

        clock.tick(20)

        snake.advance()

        info_screen.print(f'X: {snake.head_x}, Y: {snake.head_y}')

        if (snake.check_game_over()):
            quitGame(None)

    pygame.quit()


def quitGame(_):
    global is_running
    is_running = False


def change_snake_facing(keydown_Event: pygame.event):
    global snake

    if (keydown_Event.key == pygame.K_UP):
        snake.face(Direction.UP)
    elif (keydown_Event.key == pygame.K_DOWN):
        snake.face(Direction.DOWN)
    elif (keydown_Event.key == pygame.K_LEFT):
        snake.face(Direction.LEFT)
    elif (keydown_Event.key == pygame.K_RIGHT):
        snake.face(Direction.RIGHT)


game_loop()
