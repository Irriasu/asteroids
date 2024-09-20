from constants import *
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((10,10,10))
        pygame.display.flip()


if __name__ == "__main__":
    main()