import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont("comicsansms", 35)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock for controlling game speed
clock = pygame.time.Clock()

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], CELL_SIZE, CELL_SIZE])

def message(msg, color, y_offset=0):
    text = font.render(msg, True, color)
    rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + y_offset))
    screen.blit(text, rect)

def game_loop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2
    dx = CELL_SIZE
    dy = 0

    snake = []
    length = 1

    # Initial food
    food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
    food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press Q-Quit or R-Restart", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -CELL_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = CELL_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -CELL_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = CELL_SIZE
                    dx = 0

        x += dx
        y += dy

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, CELL_SIZE, CELL_SIZE])

        snake.append([x, y])
        if len(snake) > length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == [x, y]:
                game_close = True

        draw_snake(snake)
        score_text = font.render(f"Score: {length - 1}", True, WHITE)
        screen.blit(score_text, [10, 10])

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            length += 1

        clock.tick(10)

    pygame.quit()
    quit()

# Run the game
game_loop()