import pygame

from enum import Enum, auto

class SnakeDirection(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

pygame.init()
surface = pygame.display.set_mode((500, 500))

is_game_running = True
SNAKE_WIDTH = 20
SNAKE_HEIGHT = 20

WINDOW_WIDTH = surface.get_width()
WINDOW_HEIGHT = surface.get_height()

snake_location_x = WINDOW_WIDTH // 2 - SNAKE_WIDTH // 2
snake_location_y = WINDOW_HEIGHT // 2 - SNAKE_HEIGHT // 2
snake_direction = SnakeDirection.DOWN

clock = pygame.time.Clock()


while is_game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            is_game_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            snake_direction = SnakeDirection.UP
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            snake_direction = SnakeDirection.DOWN
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            snake_direction = SnakeDirection.LEFT
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            snake_direction = SnakeDirection.RIGHT
    
    surface.fill((0, 0, 0))
    surface.fill((255, 0, 0), (snake_location_x, snake_location_y, SNAKE_HEIGHT, SNAKE_WIDTH))

    if snake_direction == SnakeDirection.DOWN:
        snake_location_y = (snake_location_y + 2) % WINDOW_HEIGHT
    elif snake_direction == SnakeDirection.UP:
        snake_location_y = (snake_location_y -2 ) % WINDOW_HEIGHT
    elif snake_direction == SnakeDirection.LEFT:
        snake_location_x = (snake_location_x - 2) % WINDOW_WIDTH
    elif snake_direction == SnakeDirection.RIGHT:
        snake_location_x = (snake_location_x + 2) % WINDOW_WIDTH

    pygame.display.flip()

    clock.tick(60)

pygame.quit()