import pygame
from constants import *
from player import Player

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

    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))

        for obj in drawable_group:
            obj.draw(screen)

        for obj in updatable_group:
            obj.update(dt)

        pygame.display.flip() # refresh display once per frame
        dt = clock.tick(60) / 1000 # converting milliseconds to seconds (represents how much time passed between frames at 60 fps)
    
        

if __name__ == "__main__":
    main()
