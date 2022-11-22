import pygame

from enum import Enum, auto
from random import randint


def snap(value, snap_value):
    return (value // snap_value) * snap_value

class SnakeDirection(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

SNAKE_WIDTH = 50
SNAKE_HEIGHT = 50

pygame.init()
surface = pygame.display.set_mode((2 * 16 * SNAKE_WIDTH, 2 * 9 * SNAKE_HEIGHT), flags=pygame.FULLSCREEN | pygame.SCALED)

is_game_main_loop_running = True
is_game_over = False # Game can still restart after game over

WINDOW_WIDTH = surface.get_width()
WINDOW_HEIGHT = surface.get_height()


SNAKE_COLOR = (255, 255, 0)
snake_location_x = WINDOW_WIDTH // 2 
snake_location_y = WINDOW_HEIGHT // 2
snake_direction = SnakeDirection.DOWN
snake_length = 1
snake_history = []

FOOD_COLOR = (255, 0, 0)
food_location_x = snap(randint(0, WINDOW_WIDTH - SNAKE_WIDTH), SNAKE_WIDTH)
food_location_y = snap(randint(0, WINDOW_HEIGHT - SNAKE_HEIGHT), SNAKE_HEIGHT)

clock = pygame.time.Clock()


while is_game_main_loop_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_main_loop_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            is_game_main_loop_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP and (snake_direction != SnakeDirection.DOWN or snake_length == 1):
            snake_direction = SnakeDirection.UP
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and (snake_direction != SnakeDirection.UP or snake_length == 1):
            snake_direction = SnakeDirection.DOWN
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and (snake_direction != SnakeDirection.RIGHT or snake_length == 1):
            snake_direction = SnakeDirection.LEFT
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and (snake_direction != SnakeDirection.LEFT or snake_length == 1):
            snake_direction = SnakeDirection.RIGHT
    
    surface.fill((0, 0, 0))
    surface.fill(FOOD_COLOR, (food_location_x, food_location_y, SNAKE_HEIGHT, SNAKE_WIDTH))
    snake_history.append((snake_location_x, snake_location_y, SNAKE_HEIGHT, SNAKE_WIDTH))

    if len(snake_history) > snake_length:
        snake_history.pop(0)
    
    snake_history_collision: dict[tuple[int, int], bool] = dict()
    
    for rect in snake_history:
        if snake_history_collision.get((rect[0], rect[1]), False):
            is_game_over = True
        snake_history_collision[(rect[0], rect[1])] = True
        surface.fill(SNAKE_COLOR, rect)
    
    if is_game_over:
        snake_length = 1
        snake_history.clear()
        snake_location_x = WINDOW_WIDTH // 2 
        snake_location_y = WINDOW_HEIGHT // 2
        is_game_over = False

    if snake_direction == SnakeDirection.DOWN:
        snake_location_y = snap((snake_location_y + SNAKE_HEIGHT) % WINDOW_HEIGHT, SNAKE_HEIGHT)
    elif snake_direction == SnakeDirection.UP:
        snake_location_y = snap((snake_location_y - SNAKE_HEIGHT) % WINDOW_HEIGHT, SNAKE_HEIGHT)
    elif snake_direction == SnakeDirection.LEFT:
        snake_location_x = snap((snake_location_x - SNAKE_WIDTH) % WINDOW_WIDTH, SNAKE_WIDTH)
    elif snake_direction == SnakeDirection.RIGHT:
        snake_location_x = snap((snake_location_x + SNAKE_WIDTH) % WINDOW_WIDTH, SNAKE_WIDTH)
    
    if snake_location_x == food_location_x and snake_location_y == food_location_y:
        food_location_x = snap(randint(0, WINDOW_WIDTH - SNAKE_WIDTH), SNAKE_WIDTH)
        food_location_y = snap(randint(0, WINDOW_HEIGHT - SNAKE_HEIGHT), SNAKE_HEIGHT)
        snake_length += 1

    pygame.display.flip()

    clock.tick(10)

pygame.quit()