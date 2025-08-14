import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init() # initializes all Pygame modules (display, sound, keyboard, etc.)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group

    asteroid_field = AsteroidField()

    Shot.containers = (shots_group, updatable_group, drawable_group)
    
    while True:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable_group.update(dt) # dont need to call update on each objects since update() automatially calls on all sprites in the group
        screen.fill((0,0,0))

        for ast in asteroids_group:
            if ast.collision(player):
                print("Game over!")
                sys.exit(0)

        for ast in asteroids_group:
            for bullet in shots_group:
                if ast.collision(bullet):
                    ast.kill()
                    bullet.kill()

        for obj in drawable_group:
            obj.draw(screen)

        pygame.display.flip() # refresh display once per frame
        dt = clock.tick(60) / 1000 # converting milliseconds to seconds (represents how much time passed between frames at 60 fps)
    
        

if __name__ == "__main__":
    main()
