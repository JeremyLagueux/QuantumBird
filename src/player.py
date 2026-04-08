from dataclasses import dataclass
from .defaults import DEFAULT_PLAYER_RADIUS
from pygame import Surface, draw

@dataclass
class Player:
    x: float
    y: float
    velocity: float
    color: str

    def apply_gravity(self, gravity: float) -> None:
        self.velocity += gravity
        self.y += self.velocity

    def jump(self, jump_force: float) -> None:
        self.velocity = jump_force

    def draw(self, screen: Surface) -> None:
        draw.circle(screen, self.color, (self.x, self.y), DEFAULT_PLAYER_RADIUS)
