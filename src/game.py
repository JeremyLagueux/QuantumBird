from src.pipe import Pipe, generate_pipe
from src.pipe_generation import generate_info
from src.player import Player
from src.button import Button
from src.defaults import DEFAULT_NUM_PIPES, DEFAULT_GRAVITY, DEFAULT_JUMP_FORCE, DEFAULT_PLAYER_RADIUS
from src.event import TRIGGER_LOOP

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
        player.draw(screen)

        player.apply_gravity(DEFAULT_GRAVITY)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.jump(DEFAULT_JUMP_FORCE)
    
    for pipe in pipes:
        pipe.draw(screen)
        pipe.move(dt)

def title_screen(screen: pygame.Surface, buttons: list[Button]) -> None:
    screen.fill("black")
    for button in buttons:
        button.process(screen)
    
def init_title_screen(font: pygame.font.Font | None) -> list[Button]:
    play_button: Button = Button(pygame.Rect(100, 100, 100, 100), "text", play, font, "blue")
    return [play_button]

def play() -> None:
    event = pygame.event.Event(TRIGGER_LOOP)
    pygame.event.post(event)
    
def init_game(players: list[Player], screen: pygame.Surface) -> None:
    player: Player = Player(screen.get_width() * 0.3, screen.get_height() / 2, 0, "white")
    players.append(player)
