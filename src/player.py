from dataclasses import dataclass
from .defaults import DEFAULT_PLAYER_RADIUS, DEFAULT_GRAVITY
from .event import RESET, INCREMENT_SCORE
from .pipe import Pipe
from pygame import Surface, draw, Rect
from typing import Callable

@dataclass
class Player:
    x: float
    y: float
    height_limit: float
    fun: Callable
    velocity: float = 0
    color: str = "white"
    is_scoring: bool = False

    def _apply_gravity(self, gravity: float = DEFAULT_GRAVITY) -> None:
        self.velocity += gravity
        self.y += self.velocity
        self.y = self.height_limit - DEFAULT_PLAYER_RADIUS if self.y > \
                self.height_limit - DEFAULT_PLAYER_RADIUS else \
                DEFAULT_PLAYER_RADIUS if self.y < \
                DEFAULT_PLAYER_RADIUS else \
                self.y

    def jump(self, jump_force: float) -> None:
        self.velocity = jump_force
    
    def process(self, screen: Surface, pipes: list[Pipe]) -> None:
        self._apply_gravity()
        self._draw(screen)
        rect = Rect(self.x, self.y, DEFAULT_PLAYER_RADIUS, DEFAULT_PLAYER_RADIUS)
        top: list[Rect] = []
        bottom: list[Rect] = []
        whole: list[Rect] = []
        for pipe in pipes:
            top.append(pipe.top_rect)
            bottom.append(pipe.bottom_rect)
            whole.append(pipe.whole_rect)
        
        top_res = rect.collidelist(top)
        bottom_res = rect.collidelist(bottom)
        whole_res = rect.collidelist(whole)
        if top_res != -1 or bottom_res != -1:
            self.fun(RESET)
        if whole_res != -1 and not self.is_scoring:
            self.is_scoring = True
            self.fun(INCREMENT_SCORE)
        elif whole_res == -1:
            self.is_scoring = False

    def _draw(self, screen: Surface) -> None:
        draw.circle(screen, self.color, (self.x, self.y), DEFAULT_PLAYER_RADIUS)
