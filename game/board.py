import pygame
from typing import Tuple


class Board:
    empty_block_color = (100, 100, 100)

    def __init__(self, surface: pygame.Surface, blocks_per_side: int):
        self.surface = surface
        self.blocks_per_side = blocks_per_side

        self.__draw_board()

    def __draw_board(self):
        for x in range(self.blocks_per_side):
            for y in range(self.blocks_per_side):
                self.draw_block(x, y, self.empty_block_color)

    def draw_block(self, x: int, y: int, color: Tuple[int, int, int]):
        border_thickness = 1
        pixels_per_block = self.surface.get_width() // self.blocks_per_side

        fromX = x * pixels_per_block + border_thickness
        fromY = y * pixels_per_block + border_thickness
        side_length = pixels_per_block - 2*border_thickness

        rectangle = pygame.Rect(fromX, fromY, side_length, side_length)
        pygame.draw.rect(self.surface, color, rectangle)

    def clear_block(self, x: int, y: int):
        self.draw_block(x, y, self.empty_block_color)
