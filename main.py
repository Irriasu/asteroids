from constants import *
import pygame
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    dt=0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((10,10,10))
        player.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)/1000

if __name__ == "__main__":
    main()