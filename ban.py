import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)


# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2), (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2),
                     (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)

    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction
        new_head = ((x + dx) % GRID_WIDTH, (y + dy) % GRID_HEIGHT)
        if new_head in self.body[1:]:
            return False  # Game over: snake hits itself
        self.body.insert(0, new_head)
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:  # Avoid moving directly opposite
            self.direction = direction

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Apple class
class Apple:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self):
        pygame.draw.rect(screen, RED,
                         (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Button class
class Button:
    def __init__(self, text, position):
        self.text = text
        self.position = position

    def draw(self):
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.position)
        pygame.draw.rect(screen, GREEN, text_rect, 2)
        screen.blit(text_surface, text_rect)


# Main function
def main():
    snake = Snake()
    apple = Apple()
    clock = pygame.time.Clock()
    running = True
    play_again_button = Button("Play Again", (WIDTH // 2, HEIGHT // 2 + 50))

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.position[0] - 100 <= event.pos[0] <= play_again_button.position[0] + 100 \
                        and play_again_button.position[1] - 25 <= event.pos[1] <= play_again_button.position[1] + 25:
                    main()  # Restart the game

        if snake.move():
            if snake.body[0] == apple.position:
                snake.grow()
                apple.position = apple.randomize_position()

            snake.draw()
            apple.draw()
            pygame.display.flip()
            clock.tick(10)  # Adjust snake speed here
        else:
            running = False  # Game over: snake hits itself

    # Display final score and "Play Again" button
    final_score = len(snake.body) - 3
    game_over_text = font.render(f"Game Over! Your Score: {final_score}", True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_text, game_over_rect)
    play_again_button.draw()
    pygame.display.flip()

    while True:  # Keep the window open until the player clicks "Play Again"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.position[0] - 100 <= event.pos[0] <= play_again_button.position[0] + 100 \
                        and play_again_button.position[1] - 25 <= event.pos[1] <= play_again_button.position[1] + 25:
                    main()  # Restart the game


if __name__ == "__main__":
    main()
