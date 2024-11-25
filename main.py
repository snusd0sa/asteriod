import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main ():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()


    Player.containers = (updatable, drawable)
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for a in asteroids:
            if a.collision_check(player):
                print("Game over!!!")
                sys.exit()

        #player.update(dt)
        screen.fill((0,0,0))
        for obj in drawable:
            obj.draw(screen)
        #player.draw(screen)       
       

        # Update the screen with what we've drawn
        pygame.display.flip() 
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
