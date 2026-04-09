from src.button import Button
from src.player import Player
from src.pipe import Pipe
from src.game import loop_game, title_screen, init_title_screen, init_game, \
        reset_game
from src.event import TRIGGER_LOOP, RESET, INCREMENT_SCORE, PAUSE
from src.effect import Effect

import pygame


pygame.init()
screen: pygame.Surface = pygame.display.set_mode((1280, 720))
clock: pygame.time.Clock = pygame.time.Clock()
running: bool = True
dt: float = 0
players: list[Player] = []
pipes: list[Pipe] = []
effects: list[Effect] = []
score: int = 0
font: None = None #pygame.font.SysFont('IBM Plex', 20)
loop: bool = False
pause: bool = False
title_buttons: list[Button] = init_title_screen(font)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == TRIGGER_LOOP:
            loop = True
            init_game(players, screen)
        if event.type == RESET:
            loop = False
            reset_game(players, pipes)
        if event.type == INCREMENT_SCORE:
            score += 1
            print(f"Score : {score}")
        if event.type == PAUSE:
            pause = True if not pause else False
    
    if loop:
        if pause:
            dt = 0
        loop_game(screen, clock, dt, pipes, players, effects)
    else:
        title_screen(screen, title_buttons)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
