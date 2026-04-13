from src.pipe import Pipe, generate_pipe
from src.player import Player, sort_players_by_color
from src.button import Button
from src.defaults import (
        DEFAULT_PLAYER_RADIUS,
        DEFAULT_NUM_EFFECTS,
        )
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
    font: pygame.font.Font,
    score,
    time_since_start,
    pipe_sprite: pygame.Surface
) -> None:

    # Generate pipes outside screen width
    if time_since_start > 20:
        generate_pipe(
            pipes=pipes,
            x=screen.get_width(),
            width=100,
            screen=screen,
            num_pipes=num_pipes,
            players=players,
            sprite = pipe_sprite
        )

    if is_effects:
        generate_effect(screen, effects, DEFAULT_NUM_EFFECTS, 500, players)

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

    score_text = font.render(f"Score : {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))


def title_screen(screen: pygame.Surface, buttons: list[Button]) -> None:
    screen.fill("black")
    bg = ParallaxLayer(
        "src/sprites/blue-back.png", 60, screen.get_width(), screen.get_height()
    )
    bg2 = ParallaxLayer(
        "src/sprites/blue-stars.png", 40, screen.get_width(), screen.get_height()
    )

    bg.draw(screen)
    bg2.draw(screen)
    for button in buttons:
        button.process(screen)


def init_title_screen(
    font: pygame.font.Font | None, screen: pygame.Surface
) -> list[Button]:
    play_button: Button = Button(
        rect=pygame.Rect(
            (screen.get_width() - 250) / 2,
            (screen.get_height() - 50) / 2,
            250,
            100,
        ),
        text="START",
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


def init_game(
    players: list[Player], screen: pygame.Surface, backgrounds: list[ParallaxLayer]
) -> None:
    rect = pygame.Rect(
        screen.get_width() * 0.3,
        screen.get_height() / 2,
        DEFAULT_PLAYER_RADIUS,
        DEFAULT_PLAYER_RADIUS,
    )

    sprite = pygame.image.load("src/sprites/quantumBirdWhite.png").convert_alpha()
    sprite = pygame.transform.scale(sprite, (100, 100))
    animate_sprite_entry(sprite, screen, rect, backgrounds)
    player1: Player = Player(
        rect, sprite=sprite, height_limit=screen.get_height(), fun=post_event
    )
    players.append(player1)


def animate_sprite_entry(
    sprite: pygame.Surface,
    screen: pygame.Surface,
    target_rect: pygame.Rect,
    backgrounds: list[ParallaxLayer],
) -> None:
    clock = pygame.time.Clock()

    temp_rect = sprite.get_rect()
    temp_rect.y = target_rect.y

    x = float(-temp_rect.width)
    speed = 600.0

    while x < target_rect.x:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        x += speed * dt
        if x > target_rect.x:
            x = float(target_rect.x)

        temp_rect.x = round(x)

        for bg in backgrounds:
            bg.update(dt)
            bg.draw(screen)

        screen.blit(sprite, temp_rect)
        pygame.display.flip()
