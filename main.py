from constants import *
import pygame
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt=0
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    Player.containers =(updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers =(shots,updatable,drawable)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((10,10,10))
        for i in updatable:
            i.update(dt)
        for i in asteroids:
            if i.is_collide(player):
                print("Game over!")
                return
            for shot in shots:
                if i.is_collide(shot):
                    shot.kill()
                    i.split()
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)/1000
        

if __name__ == "__main__":
    main()