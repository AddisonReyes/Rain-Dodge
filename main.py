import random
import time

import pygame

WINDOW_WIDTH: int = 1000  # 960
WINDOW_HEIGHT: int = 750  # 540
pygame.font.init()

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rain Dodge")

BG = pygame.transform.scale(
    pygame.image.load("bg.jpeg"),
    (WINDOW_WIDTH, WINDOW_HEIGHT),
)

PLAYER_WIDTH: int = 40
PLAYER_HEIGHT: int = 60
PLAYER_VELOCITY: int = 5

STAR_WIDTH: int = 10
STAR_HEIGHT: int = 20
STAR_VELOCITY: int = 3

FONT = pygame.font.SysFont("alagard", 30)


def draw(player, elapsed_time, stars) -> None:
    WINDOW.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WINDOW.blit(time_text, (10, 10))

    pygame.draw.rect(WINDOW, "red", player)

    for star in stars:
        pygame.draw.rect(WINDOW, "white", star)

    pygame.display.update()


def main() -> None:
    run = True

    player = pygame.Rect(
        200, WINDOW_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT
    )

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time: float = 0

    star_add_increment: int = 2000
    star_count: int = 0

    stars: list = []
    hit: bool = False

    while run:
        star_count += clock.tick(60)
        elapsed_time: float = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WINDOW_WIDTH - STAR_WIDTH)
                star = pygame.Rect(
                    star_x,
                    -STAR_HEIGHT,
                    STAR_WIDTH,
                    STAR_HEIGHT,
                )

                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if (
            keys[pygame.K_d]
            and player.x + PLAYER_VELOCITY + player.width <= WINDOW_WIDTH
        ):
            player.x += PLAYER_VELOCITY

        for star in stars[:]:
            star.y += STAR_VELOCITY
            if star.y > WINDOW_HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You lost!", 1, "white")
            WINDOW.blit(
                lost_text,
                (
                    WINDOW_WIDTH / 2 - lost_text.get_width() / 2,
                    WINDOW_HEIGHT / 2 - lost_text.get_height() / 2,
                ),
            )

            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()


if __name__ == "__main__":
    main()
