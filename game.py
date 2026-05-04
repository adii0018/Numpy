import pygame
import random
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Bird
bird_x = 60
bird_y = HEIGHT // 2
velocity = 0
gravity = 0.5
jump = -8

# Pipes
pipe_width = 60
gap = 150
pipe_x = WIDTH
pipe_height = random.randint(100, 400)

# Score
score = 0
passed = False

def reset_game():
    global bird_y, velocity, pipe_x, pipe_height, score, passed
    bird_y = HEIGHT // 2
    velocity = 0
    pipe_x = WIDTH
    pipe_height = random.randint(100, 400)
    score = 0
    passed = False

def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

running = True
game_over = False

while running:
    clock.tick(60)
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_SPACE:
                    velocity = jump
            else:
                if event.key == pygame.K_r:
                    reset_game()
                    game_over = False

    if not game_over:
        # Bird physics
        velocity += gravity
        bird_y += velocity

        # Pipes movement
        pipe_x -= 4

        # Reset pipes
        if pipe_x < -pipe_width:
            pipe_x = WIDTH
            pipe_height = random.randint(100, 400)
            passed = False

        # Score increase
        if pipe_x + pipe_width < bird_x and not passed:
            score += 1
            passed = True

        # Draw bird
        bird_rect = pygame.Rect(bird_x-15, bird_y-15, 30, 30)
        pygame.draw.circle(screen, YELLOW, (bird_x, int(bird_y)), 15)

        # Draw pipes
        top_pipe = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
        bottom_pipe = pygame.Rect(pipe_x, pipe_height + gap, pipe_width, HEIGHT)

        pygame.draw.rect(screen, GREEN, top_pipe)
        pygame.draw.rect(screen, GREEN, bottom_pipe)

        # Collision
        if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe) or bird_y > HEIGHT or bird_y < 0:
            game_over = True

        # Draw score
        draw_text(f"Score: {score}", 10, 10)

    else:
        draw_text("GAME OVER", 110, 250, RED)
        draw_text("Press R to Restart", 70, 300)

    pygame.display.update()