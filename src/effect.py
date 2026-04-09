from pygame import Surface, draw, Rect
from .player import Player
from .defaults import DEFAULT_EFFECT_RADIUS, DEFAULT_EFFECT_VELOCITY

from typing import Union

PositionTuple = Union[tuple[int, int], tuple[int, int, int, int]]

class Effect:
    def __init__(self, position: PositionTuple, 
                 shape: str, velocity: tuple[int, int], color: str = "white") -> None:
        self.position = position
        self.shape = shape
        self.velocity = velocity
        self.color = color

    def process(self, screen: Surface, dt: float) -> None:
        self._draw(screen)
        self._move(dt)

    def _draw(self, screen: Surface) -> None:
        match self.shape:
            case "circle":
                draw.circle(screen, self.color, self.position, DEFAULT_EFFECT_RADIUS)
            case "rect":
                rect = Rect(self.position)
                draw.rect(screen, self.color, rect)
        
    
    def _move(self, dt: float) -> None:
        match self.shape:
            case "circle":
                x, y = self.position
                dx, dy = self.velocity
                y -= int(dt * dy)
                x -= int(dt * dx)
                self.position = (x, y)
                print(self.position)

    def _collide(self, players: list[Player]) -> None:
        ...

def generate_effect(screen: Surface, effects: list[Effect]) -> None:
    # Remove effects that are outside the view
    if len(effects) > 0 and effects[-1].position[0] < 0:
        effects.pop()

    if len(effects) == 0:
        effect = Effect((int(screen.get_width() + DEFAULT_EFFECT_RADIUS),
                         int(screen.get_height() / 2)), "circle",
                        (DEFAULT_EFFECT_VELOCITY, 0))
        effects.append(effect)
