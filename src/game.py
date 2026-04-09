from src.pipe import Pipe, generate_pipe, generate_info
from src.player import Player
from src.button import Button
from src.defaults import DEFAULT_NUM_PIPES, DEFAULT_JUMP_FORCE
from src.event import TRIGGER_LOOP, RESET

import pygame

def loop_game(screen: pygame.Surface, clock: pygame.time.Clock, dt: float,
              pipes: list[Pipe], players:list[Player]) -> None:
    center, pipe_gap = generate_info(pipes[-1] if len(pipes) > 0 else None, 0.1)
    player = players[-1] if len(players) > 0 else None

    # Generate pipes outside screen width
    generate_pipe(pipes = pipes, velocity = 500, x = screen.get_width(),
                  width = 100, center = center, pipe_gap = pipe_gap, color = "white",
                  screen = screen, gap = 500, num_pipes = DEFAULT_NUM_PIPES)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    if player != None:
        player.process(screen, pipes)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.jump(DEFAULT_JUMP_FORCE)
    
    for pipe in pipes:
        pipe.process(screen, dt)

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
    player: Player = Player(x = screen.get_width() * 0.3, y = screen.get_height() / 2,
                            height_limit = screen.get_height(), fun = post_event)
    players.append(player)
