import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from bullet import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = updatables, drawables
    Asteroid.containers = updatables, drawables, asteroids
    AsteroidField.containers = updatables
    Shot.containers = updatables, drawables, shots

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        updatables.update(dt)
        
        for asteroid in asteroids:
            if player.collides_with(asteroid): 
                print("Game over!")
                pygame.quit()
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        dt = clock.tick() / 1000

if __name__ == "__main__":
    main()
    