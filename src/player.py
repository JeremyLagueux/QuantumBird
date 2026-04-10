from dataclasses import dataclass
from .defaults import DEFAULT_PLAYER_RADIUS, DEFAULT_GRAVITY, DEFAULT_JUMP_FORCE
from .event import RESET, INCREMENT_SCORE
from .pipe import Pipe
from pygame import Surface, draw, Rect, colordict
from typing import Callable
from random import shuffle

_colors = list(colordict.THECOLORS.keys())

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
        res = max(top_res, bottom_res)
        if res != -1 and pipes[res].color == self.color:
            self.fun(RESET)
        if whole_res != -1 and not self.is_scoring:
            self.is_scoring = True
            self.fun(INCREMENT_SCORE)
        elif whole_res == -1:
            self.is_scoring = False

    def _draw(self, screen: Surface) -> None:
        draw.circle(screen, self.color, (self.rect.x, self.rect.y), DEFAULT_PLAYER_RADIUS)

def sort_players_by_color(players: list[Player]) -> dict[str, list[Player]]:
    c_players = {}
    for player in players:
        c_players.setdefault(player.color, [])
        c_players[player.color].append(player)
    return c_players

def get_color() -> str:
    shuffle(_colors)
    color = _colors.pop()
    return color
