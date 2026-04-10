from __future__ import annotations
from pygame import Surface, draw, Rect
from .player import Player
from .defaults import (
    DEFAULT_EFFECT_RADIUS,
    DEFAULT_EFFECT_VELOCITY,
    DEFAULT_EFFECT_MAX_VELOCITY,
    DEFAULT_EFFECT_MIN_VELOCITY,
)
from . import effect_functions as e_fun

from typing import Callable
from dataclasses import dataclass
from random import choice, uniform


class Effect:
    def __init__(
        self,
        rect,
        shape: str,
        velocity: tuple[int, int],
        fun: Callable | None,
        args: tuple | None,
        color: str = "white",
    ) -> None:
        self.rect = rect
        self.shape = shape
        self.velocity = velocity
        self.color = color
        self.fun = fun
        self.args = args
        self.collided = False

    def process(
        self, screen: Surface, dt: float, effects: list[Effect], players: list[Player]
    ) -> None:
        self._draw(screen)
        self._move(dt)
        self._collide(effects, players)

    def _draw(self, screen: Surface) -> None:
        match self.shape:
            case "circle":
                draw.circle(
                    screen, self.color, (self.rect.x, self.rect.y), self.rect.width
                )
            case "rect":
                draw.rect(screen, self.color, self.rect)

    def _move(self, dt: float) -> None:
        x, y, width, height = self.rect
        dx, dy = self.velocity
        y -= int(dt * dy)
        x -= int(dt * dx)
        self.rect = Rect(x, y, width, height)

    def _collide(self, effects: list[Effect], players: list[Player]) -> None:
        rects = [player.rect for player in players]
        res = self.rect.collidelist(rects)

        if res != -1 and not self.collided:
            # Collision
            self.collided = True
            if self.fun != None and self.args != None:
                self.fun(self, players, res, *self.args)
                effects.remove(self)
        elif res == -1:
            self.collided = False


def generate_effect(
    screen: Surface, effects: list[Effect], num_effects: int, effect_gap: float
) -> None:
    info = generate_info(0.3)
    # Remove effects that are outside the view
    if len(effects) > 0:
        if (
            effects[-1].rect.x + effects[-1].rect.width < 0
            and effects[-1].shape == "circle"
            or effects[-1].rect.x < 0
        ):
            effects.pop()

    if (
        len(effects) < num_effects
        and (len(effects) > 0 and effects[-1].rect.x < screen.get_width() - effect_gap)
        or len(effects) == 0
    ):
        rect = Rect(
            screen.get_width() + info.width,
            screen.get_height() / 2,
            info.width,
            info.width,
        )
        effect = Effect(
            rect, info.shape, info.velocity, info.fun, info.args, info.color
        )
        effects.append(effect)


@dataclass
class EffectInfo:
    width: int
    shape: str
    color: str
    velocity: tuple[int, int]
    fun: Callable | None
    args: tuple | None


def generate_info(around: float) -> EffectInfo:
    width: int = int(
        uniform(
            DEFAULT_EFFECT_RADIUS - around * DEFAULT_EFFECT_RADIUS,
            DEFAULT_EFFECT_RADIUS + around * DEFAULT_EFFECT_RADIUS,
        )
    )
    velocity: tuple[int, int] = (
        int(
            uniform(
                DEFAULT_EFFECT_VELOCITY - around * DEFAULT_EFFECT_VELOCITY,
                DEFAULT_EFFECT_VELOCITY + around * DEFAULT_EFFECT_VELOCITY,
            )
        ),
        0,
    )
    fun_num = choice(range(len(e_fun.EFFECT_FUNCTIONS)))
    shape: str = e_fun.EFFECT_SHAPE[fun_num]
    if shape == "rect":
        width *= 2
    color: str = e_fun.EFFECT_COLOR[fun_num]
    fun: Callable | None = e_fun.EFFECT_FUNCTIONS[fun_num]
    args: tuple | None = e_fun.EFFECT_FUNCTION_ARGS[fun_num]

    dx = velocity[0]
    if dx > DEFAULT_EFFECT_MAX_VELOCITY:
        dx = DEFAULT_EFFECT_MAX_VELOCITY
    if dx < DEFAULT_EFFECT_MIN_VELOCITY:
        dx = DEFAULT_EFFECT_MIN_VELOCITY
    velocity = (dx, 0)

    return EffectInfo(width, shape, color, velocity, fun, args)
