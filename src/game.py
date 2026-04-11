from src.pipe import Pipe, generate_pipe
from src.player import Player, sort_players_by_color
from src.button import Button
from src.defaults import DEFAULT_PLAYER_RADIUS, DEFAULT_NUM_EFFECTS
from src.event import TRIGGER_LOOP, PAUSE, post_event
from src.effect import Effect, generate_effect

from src.parrallax import ParallaxLayer

import pygame


def loop_game(
    screen: pygame.Surface,
    clock: pygame.time.Clock,
    dt: float,
    pipes: list[Pipe],
    players: list[Player],
    effects: list[Effect],
    is_effects: bool,
    num_pipes: int,
    backgrounds: list[ParallaxLayer],
) -> None:

    # Generate pipes outside screen width
    generate_pipe(
        pipes=pipes,
        x=screen.get_width(),
        width=100,
        screen=screen,
        num_pipes=num_pipes,
        players=players,
    )

    if is_effects:
        generate_effect(screen, effects, DEFAULT_NUM_EFFECTS, 500)

    # fill the screen with a color to wipe away anything from last frame
    for bg in backgrounds:
        bg.update(dt)
        bg.draw(screen)

    keys = pygame.key.get_pressed()
    correct_keys = [pygame.K_1 + i for i in range(len(players))]
    dict_player = sort_players_by_color(players)
    for i, c_players in enumerate(dict_player.values()):
        for player in c_players:
            player.process(screen, dt, pipes)

            if keys[correct_keys[i]]:
                player.jump()

    if keys[pygame.K_j]:
        post_event(PAUSE)

    if keys[pygame.K_SPACE]:
        for player in players:
            player.jump()

    for pipe in pipes:
        pipe.process(screen, dt)

    for effect in effects:
        effect.process(screen, dt, effects, players)


def title_screen(screen: pygame.Surface, buttons: list[Button]) -> None:
    screen.fill("black")
    for button in buttons:
        button.process(screen)


def init_title_screen(font: pygame.font.Font | None) -> list[Button]:
    play_button: Button = Button(
        rect=pygame.Rect(100, 100, 100, 100),
        text="text",
        fun=post_event,
        arg=TRIGGER_LOOP,
        font=font,
        color="blue",
    )
    return [play_button]


def reset_game(players: list[Player], pipes: list[Pipe], effects: list[Effect]) -> None:
    players.clear()
    pipes.clear()
    effects.clear()


def init_game(players: list[Player], screen: pygame.Surface) -> None:
    rect = pygame.Rect(
        screen.get_width() * 0.3,
        screen.get_height() / 2,
        DEFAULT_PLAYER_RADIUS,
        DEFAULT_PLAYER_RADIUS,
    )

    player_sprite = pygame.image.load("src/sprites/quantumBird.png").convert_alpha()
    player_sprite = pygame.transform.scale(player_sprite, (100, 100))
    player1: Player = Player(
        rect, sprite=player_sprite, height_limit=screen.get_height(), fun=post_event
    )
    players.append(player1)
