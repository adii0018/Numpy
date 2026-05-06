import pygame
import random

pygame.init()

# Screen
WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Player Car
car_width = 50
car_height = 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - 120
car_speed = 7

# Enemy Car
enemy_width = 50
enemy_height = 100
enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -120
enemy_speed = 6

# Score
score = 0
font = pygame.font.SysFont(None, 40)

# Game loop
running = True

while running:
    clock.tick(60)

    # Background
    screen.fill(BLACK)

    # Road lines
    for i in range(0, HEIGHT, 80):
        pygame.draw.rect(screen, WHITE, (240, i, 20, 50))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed

    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # Enemy movement
    enemy_y += enemy_speed

    if enemy_y > HEIGHT:
        enemy_y = -120
        enemy_x = random.randint(50, WIDTH - 100)
        score += 1
        enemy_speed += 0.2

    # Draw player
    pygame.draw.rect(screen, BLUE, (car_x, car_y, car_width, car_height))

    # Draw enemy
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))

    # Collision
    if (
        car_x < enemy_x + enemy_width
        and car_x + car_width > enemy_x
        and car_y < enemy_y + enemy_height
        and car_y + car_height > enemy_y
    ):
        print("GAME OVER")
        print("Score:", score)
        running = False

    # Score text
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()