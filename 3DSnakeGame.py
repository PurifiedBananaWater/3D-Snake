import pygame
import random
import sys

pygame.init()

width, height = 800, 600
grid_size = 20
background_color = (0, 0, 0)
snake_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255),
                (0, 255, 255), (128, 56, 0), (0, 128, 56), (56, 0, 128)]

score = 0

food = (random.randint(0, width - grid_size) // grid_size * grid_size,
                random.randint(0, height - grid_size) // grid_size * grid_size)
food_layer = random.randint(0, len(snake_colors) - 1)
food_color = (snake_colors[food_layer])

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

snake_plane = 0
snake = [(200, 200, snake_plane)]

direction = 'right'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'
            elif event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
            elif event.key == pygame.K_w:
                direction = 'in'
            elif event.key == pygame.K_s:
                direction = 'out'

    if direction == 'up':
        head = (snake[-1][0], snake[-1][1] - grid_size, snake_plane)
    elif direction == 'down':
        head = (snake[-1][0], snake[-1][1] + grid_size, snake_plane)
    elif direction == 'left':
        head = (snake[-1][0] - grid_size, snake[-1][1], snake_plane)
    elif direction == 'right':
        head = (snake[-1][0] + grid_size, snake[-1][1], snake_plane)
    elif direction == 'in':
        snake_plane = snake_plane - 1
        if snake_plane < 0:
            snake_plane = 8
        head = (snake[-1][0],  snake[-1][1], snake_plane)
    elif direction == 'out':
        snake_plane = snake_plane + 1
        if snake_plane > 8:
            snake_plane = 0
        head = (snake[-1][0],  snake[-1][1], snake_plane)

    if head in snake or head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
        print("Game Over! Your score is: ", score)
        pygame.quit()
        sys.exit()

    snake.append(head)

    food_posx, food_posy = food[0], food[1]

    if (food_posx, food_posy, food_layer) == snake[-1]:
        score += 1
        food_layer = random.randint(0, len(snake_colors) - 1)
        food_color = snake_colors[food_layer]
        food = (random.randint(0, width - grid_size) // grid_size * grid_size,
                random.randint(0, height - grid_size) // grid_size * grid_size)
        print('Score:', score)
    else:
        snake.pop(0)

    screen.fill(background_color)

    for pos in snake:
        pygame.draw.rect(screen, snake_colors[pos[2]], pygame.Rect(pos[0], pos[1], grid_size, grid_size))

    if food_layer == snake_plane:
        pygame.draw.rect(screen, food_color, pygame.Rect(food[0], food[1], grid_size, grid_size))

    pygame.display.flip()
    clock.tick(10)