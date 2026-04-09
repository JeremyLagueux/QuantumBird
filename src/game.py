from src.pipe import Pipe, generate_pipe, generate_pipe_info
from src.player import Player
from src.button import Button
from src.defaults import DEFAULT_NUM_PIPES, DEFAULT_PLAYER_RADIUS, DEFAULT_NUM_EFFECTS
from src.event import TRIGGER_LOOP, PAUSE
from src.effect import Effect, generate_effect

import pygame

def loop_game(screen: pygame.Surface, clock: pygame.time.Clock, dt: float,
              pipes: list[Pipe], players:list[Player], effects: list[Effect]) -> None:
    center, pipe_gap = generate_pipe_info(pipes[-1] if len(pipes) > 0 else None, 0.1)

    # Generate pipes outside screen width
    generate_pipe(pipes = pipes, velocity = 500, x = screen.get_width(),
                  width = 100, center = center, pipe_gap = pipe_gap, color = "white",
                  screen = screen, gap = 500, num_pipes = DEFAULT_NUM_PIPES)

    generate_effect(screen, effects, DEFAULT_NUM_EFFECTS, 500)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    keys = pygame.key.get_pressed()
    correct_keys = [pygame.K_1 + i for i in range(len(players))]
    for i in range(len(players)):
        players[i].process(screen, dt, pipes)

        if keys[correct_keys[i]]:
            players[i].jump()
    
    if keys[pygame.K_j]:
        post_event(PAUSE)

    for pipe in pipes:
        pipe.process(screen, dt)
        
    for effect in effects:
        effect.process(screen, dt, players)

def title_screen(screen: pygame.Surface, buttons: list[Button]) -> None:
    screen.fill("black")
    for button in buttons:
        button.process(screen)
    
def init_title_screen(font: pygame.font.Font | None) -> list[Button]:
    play_button: Button = Button(rect = pygame.Rect(100, 100, 100, 100), text = "text",
                                 fun = post_event, arg = TRIGGER_LOOP, font = font,
                                 color = "blue")
    return [play_button]

def post_event(evt: int) -> None:
    event = pygame.event.Event(evt)
    pygame.event.post(event)

def reset_game(players: list[Player], pipes: list[Pipe]) -> None:
    players.clear()
    pipes.clear()
    
def init_game(players: list[Player], screen: pygame.Surface) -> None:
    rect1 = pygame.Rect(screen.get_width() * 0.3, screen.get_height() / 2,
                       DEFAULT_PLAYER_RADIUS, DEFAULT_PLAYER_RADIUS)
    rect2 = pygame.Rect(screen.get_width() * 0.3, screen.get_height() / 8,
                       DEFAULT_PLAYER_RADIUS, DEFAULT_PLAYER_RADIUS)
    player1: Player = Player(rect1, height_limit = screen.get_height(), fun = post_event)
    player2: Player = Player(rect2, height_limit = screen.get_height(), fun = post_event)
    players.append(player1)
    # players.append(player2)
