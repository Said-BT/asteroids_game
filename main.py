import pygame
from constants import *
from player import *

black_color = (0, 0, 0)

def main():
    print("Starting asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Creating groups:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(black_color)

        for item in drawable:
            item.draw(screen)

        for item in updatable:
            item.update(dt)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
