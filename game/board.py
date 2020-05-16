import pygame


class Board:
    def __init__(self, surface, blocks_per_side):

        self.surface = surface
        self.blocks_per_side = blocks_per_side

        pixels_per_block = surface.get_width() // blocks_per_side

        for x in range(blocks_per_side):
            for y in range(blocks_per_side):

                border_thickness = 1
                fromX = x * pixels_per_block + border_thickness
                fromY = y * pixels_per_block + border_thickness
                side_length = pixels_per_block - 2*border_thickness

                rectangle = pygame.Rect(fromX, fromY, side_length, side_length)
                pygame.draw.rect(surface, (100, 100, 100), rectangle)

        pygame.display.update()
