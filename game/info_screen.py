import pygame


class InfoScreen:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface

    def print(self, text: str):
        # clear old text
        self.surface.fill((0, 0, 0))

        # print new text
        font = pygame.font.Font('freesansbold.ttf', 32)
        renderedText = font.render(text, True, (0, 255, 0))
        rectangle = renderedText.get_rect()
        rectangle.center = (self.surface.get_width() // 2,
                            self.surface.get_height() // 2)

        self.surface.blit(renderedText, rectangle)
