import random
import time

import pygame

WINDOW_WIDTH: int = 1000  # 960
WINDOW_HEIGHT: int = 750  # 540

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rain Dodge")

BG = pygame.transform.scale(
    pygame.image.load("bg.jpeg"),
    (WINDOW_WIDTH, WINDOW_HEIGHT),
)

PLAYER_WIDTH: int = 40
PLAYER_HEIGHT: int = 60

PLAYER_VELOCITY: int = 5


def draw(player) -> None:
    WINDOW.blit(BG, (0, 0))

    pygame.draw.rect(WINDOW, "red", player)
    pygame.display.update()


def main() -> None:
    run = True

    player = pygame.Rect(
        200, WINDOW_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT
    )

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if (
            keys[pygame.K_d]
            and player.x + PLAYER_VELOCITY <= WINDOW_WIDTH - PLAYER_WIDTH
        ):
            player.x += PLAYER_VELOCITY

        draw(player)

    pygame.quit()


if __name__ == "__main__":
    main()
