from dataclasses import dataclass
from .defaults import DEFAULT_PLAYER_RADIUS, DEFAULT_GRAVITY, DEFAULT_JUMP_FORCE
from .event import RESET, INCREMENT_SCORE
from .pipe import Pipe
from pygame import Surface, draw, Rect
from typing import Callable

@dataclass
class Player:
    rect: Rect
    height_limit: float
    fun: Callable
    velocity: float = 0
    jump_force: float = DEFAULT_JUMP_FORCE
    gravity: float = DEFAULT_GRAVITY
    color: str = "white"
    is_scoring: bool = False

    def _apply_gravity(self, dt: float) -> None:
        self.velocity += self.gravity
        self.rect.y += int(self.velocity * dt)
        self.rect.y = int(self.height_limit - self.rect.width if self.rect.y > \
                self.height_limit - self.rect.width else \
                self.rect.width if self.rect.y < \
                self.rect.width else \
                self.rect.y)

    def jump(self) -> None:
        self.velocity = self.jump_force
    
    def process(self, screen: Surface, dt: float, pipes: list[Pipe]) -> None:
        self._apply_gravity(dt)
        self._draw(screen)
        top: list[Rect] = []
        bottom: list[Rect] = []
        whole: list[Rect] = []
        for pipe in pipes:
            top.append(pipe.top_rect)
            bottom.append(pipe.bottom_rect)
            whole.append(pipe.whole_rect)
        
        top_res = self.rect.collidelist(top)
        bottom_res = self.rect.collidelist(bottom)
        whole_res = self.rect.collidelist(whole)
        if top_res != -1 or bottom_res != -1:
            self.fun(RESET)
        if whole_res != -1 and not self.is_scoring:
            self.is_scoring = True
            self.fun(INCREMENT_SCORE)
        elif whole_res == -1:
            self.is_scoring = False

    def _draw(self, screen: Surface) -> None:
        draw.circle(screen, self.color, (self.rect.x, self.rect.y), DEFAULT_PLAYER_RADIUS)
