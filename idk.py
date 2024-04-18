import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake attributes
block_size = 20
snake_speed = 10

# Fonts
font = pygame.font.SysFont(None, 25)

# Draw snake
def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block_size, block_size])

# Display message
def message(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [width / 6, height / 3])

# Game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial snake position and movement
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Initial food position
    foodx = round(random.randrange(0, width - block_size) / 20) * 20
    foody = round(random.randrange(0, height - block_size) / 20) * 20

    # Main game loop
    while not game_over:

        # Game over screen
        while game_close:
            screen.fill(white)
            message("You lost! Press C to play again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check for boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        screen.fill(white)

        # Draw food
        pygame.draw.rect(screen, red, [foodx, foody, block_size, block_size])

        # Update snake body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for snake collision with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw snake
        draw_snake(snake_list)

        # Update display
        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 20) * 20
            foody = round(random.randrange(0, height - block_size) / 20) * 20
            length_of_snake += 1

        # Set snake speed
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
