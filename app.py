import pygame


def main():
    pygame.init()
    pygame.display.set_caption("PySnake")
    screen = pygame.display.set_mode((800, 800))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()