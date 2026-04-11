from src.button import Button
from src.player import Player
from src.pipe import Pipe
from src.game import loop_game, title_screen, init_title_screen, init_game, reset_game
from src.event import TRIGGER_LOOP, RESET, INCREMENT_SCORE, PAUSE
from src.effect import Effect
from src.defaults import (
    DEFAULT_MAX_NUM_PIPES,
    DEFAULT_NUM_PIPES,
    DEFAULT_EFFECTS_THRESHOLD,
)

import pygame
from src.parrallax import ParallaxLayer

pygame.init()
screen: pygame.Surface = pygame.display.set_mode((1280, 720))
clock: pygame.time.Clock = pygame.time.Clock()
running: bool = True
dt: float = 0
players: list[Player] = []
pipes: list[Pipe] = []
effects: list[Effect] = []
score: int = 0
font = pygame.font.SysFont("IBM Plex", 100)
loop: bool = False
pause: bool = False
is_effects: bool = False
num_pipes: int = DEFAULT_NUM_PIPES
title_buttons: list[Button] = init_title_screen(font, screen)
exp: list[int] = [i**2 for i in range(3, 10)]
backgrounds = [
    ParallaxLayer(
        "src/sprites/blue-back.png", 60, screen.get_width(), screen.get_height()
    ),
    ParallaxLayer(
        "src/sprites/blue-stars.png", 40, screen.get_width(), screen.get_height()
    ),
]
time_since_start = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == TRIGGER_LOOP:
            loop = True
            init_game(players, screen, backgrounds)
        if event.type == RESET:
            loop = False
            reset_game(players, pipes, effects)
            score = 0
            num_pipes = DEFAULT_NUM_PIPES
            is_effects = False
        if event.type == INCREMENT_SCORE:
            score += 1
            if score == DEFAULT_EFFECTS_THRESHOLD:
                is_effects = True
            if score in exp and num_pipes < DEFAULT_MAX_NUM_PIPES:
                num_pipes += 1
            print(f"Score : {score}")
        if event.type == PAUSE:
            pause = True if not pause else False

    if loop:
        time_since_start += 1
        if pause:
            dt = 0
        loop_game(
            screen,
            clock,
            dt,
            pipes,
            players,
            effects,
            is_effects,
            num_pipes,
            backgrounds,
            font,
            score=score,
            time_since_start=time_since_start,
        )
    else:
        title_screen(screen, title_buttons)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
