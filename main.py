import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from states import State

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Fonts
    title_font = pygame.font.SysFont(None, 74)
    small_font = pygame.font.SysFont(None, 28)

    # Game state
    state = State.MENU
    score = 0

    # Sprites / Groups
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    asteroid_field = AsteroidField()

    Shot.containers = (shots_group, updatable_group, drawable_group)

    while True:
        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if state == State.MENU and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = 0
                    state = State.PLAYING
                    player.position.update(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    shots_group.empty()
                    asteroids_group.empty()
                    asteroid_field = AsteroidField()  # fresh field

            if state == State.GAME_OVER and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    score = 0
                    state = State.PLAYING
                    player.position.update(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    shots_group.empty()
                    asteroids_group.empty()
                    asteroid_field = AsteroidField()

        # --- Draw / Update ---
        screen.fill((0, 0, 0))

        if state == State.MENU:
            title_surf = title_font.render("ASTEROIDS", True, (0, 0, 255))
            start_surf = small_font.render("Press SPACE to start", True, (255, 255, 255))
            screen.blit(title_surf, (SCREEN_WIDTH//2 - title_surf.get_width()//2, 200))
            screen.blit(start_surf, (SCREEN_WIDTH//2 - start_surf.get_width()//2, 300))

        elif state == State.PLAYING:
            updatable_group.update(dt)

            # Player collision → game over
            for ast in list(asteroids_group):
                if ast.collision(player):
                    state = State.GAME_OVER

            # Shots vs asteroids + scoring
            for ast in list(asteroids_group):
                for bullet in list(shots_group):
                    if ast.collision(bullet):
                        ast.split()
                        bullet.kill()
                        if ast.radius >= 35:
                            score += 1
                        elif ast.radius >= 22:
                            score += 2
                        else:
                            score += 5
                        break  # this bullet is gone

            # Draw all
            for obj in drawable_group:
                obj.draw(screen)

            # Score (blue)
            score_surf = small_font.render(f"Score: {score}", True, (0, 0, 255))
            screen.blit(score_surf, (16, 12))

        elif state == State.GAME_OVER:
            over_surf = title_font.render("GAME OVER", True, (255, 0, 0))
            retry_surf = small_font.render("Press R to restart", True, (255, 255, 255))
            final_score_surf = small_font.render(f"Final Score: {score}", True, (0, 0, 255))
            screen.blit(over_surf, (SCREEN_WIDTH//2 - over_surf.get_width()//2, 200))
            screen.blit(final_score_surf, (SCREEN_WIDTH//2 - final_score_surf.get_width()//2, 300))
            screen.blit(retry_surf, (SCREEN_WIDTH//2 - retry_surf.get_width()//2, 400))

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
