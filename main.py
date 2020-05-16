import pygame
from game.board import *

# size of the screen (px, square field)
size = 800

# number of blocks per side (should evenly divide the overall size)
blocks_per_side = 50


def main():
    pygame.init()
    pygame.display.set_caption("PySnake")

    board = Board(pygame.display.set_mode((size, size)), blocks_per_side)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()
