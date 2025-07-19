from constants import *
import pygame
from player import Player
from asteroidfield import *
import sys
from asteroid import Asteroid
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updateable, drawable)

    dt = 0
    
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.kill()

        screen.fill((0, 0, 0))
        
        for obj in drawable:
            obj.draw(screen)

        
        
        # player.update(dt)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
