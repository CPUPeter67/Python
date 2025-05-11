import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball properties
BALL_SIZE = 20
BALL_SPEED = [4, 4]

# Paddle properties
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 6

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Ball position
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Paddle positions
player1 = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball direction
ball_dx, ball_dy = BALL_SPEED


def reset_ball():
    global ball_dx, ball_dy
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_dx, ball_dy = BALL_SPEED


def handle_collision():
    global ball_dx, ball_dy

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_dx = -ball_dx


# Main game loop
def main():
    global ball_dx, ball_dy

    player1_speed = 0
    player2_speed = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Player 1 controls (W/S)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_speed = -PADDLE_SPEED
                elif event.key == pygame.K_s:
                    player1_speed = PADDLE_SPEED
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    player1_speed = 0

            # Player 2 controls (Up/Down arrows)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player2_speed = -PADDLE_SPEED
                elif event.key == pygame.K_DOWN:
                    player2_speed = PADDLE_SPEED
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    player2_speed = 0

        # Move paddles
        player1.y += player1_speed
        player2.y += player2_speed

        # Prevent paddles from going out of bounds
        player1.y = max(0, min(HEIGHT - PADDLE_HEIGHT, player1.y))
        player2.y = max(0, min(HEIGHT - PADDLE_HEIGHT, player2.y))

        # Move ball
        ball.x += ball_dx
        ball.y += ball_dy

        # Handle collisions
        handle_collision()

        # Ball out of bounds
        if ball.left <= 0 or ball.right >= WIDTH:
            reset_ball()

        # Drawing everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player1)
        pygame.draw.rect(screen, WHITE, player2)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()