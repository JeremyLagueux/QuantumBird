from pygame import Surface, Rect, draw
from .defaults import DEFAULT_CENTER, DEFAULT_PIPE_GAP, DEFAULT_MAX_CENTER, \
    DEFAULT_MAX_PIPE_GAP, DEFAULT_MIN_PIPE_GAP, DEFAULT_MIN_CENTER, DEFAULT_VELOCITY
from random import uniform, choice
from dataclasses import dataclass

class Pipe:
    def __init__(self, top_rect: Rect, bottom_rect: Rect, x: int, width: int, color: str,
                 velocity: int, pipe_gap: float = DEFAULT_PIPE_GAP,
                 center: float = DEFAULT_CENTER):
        self.top_rect = top_rect
        self.bottom_rect = bottom_rect
        self.whole_rect: Rect
        self.x = x
        self.width = width
        self.color = color

        self.velocity = velocity
        self.pipe_gap = pipe_gap
        self.center = center
    
    def process(self, screen: Surface, dt: float) -> None:
        self._draw(screen)
        self._move(dt)
    
    def _draw(self, screen: Surface) -> None:
        draw.rect(screen, self.color, self.top_rect)
        draw.rect(screen, self.color, self.bottom_rect)

    def _move(self, dt: float) -> None:
        self.top_rect.x -= int(self.velocity * dt)
        self.bottom_rect.x -= int(self.velocity * dt)
        self.whole_rect.x -= int(self.velocity * dt)

def generate_pipe(pipes: list[Pipe], num_pipes: int, x: int, width: int,
                  screen: Surface, players: list) -> None:
    # Remove pipes that are out of bounds
    for pipe in pipes:
        if pipe.top_rect.x + pipe.top_rect.width < 0:
            pipes.remove(pipe)

    # Don't generate if there's enough pipes
    if len(pipes) >= num_pipes:
        return

    pipe_info: PipeInfo = _generate_info(screen, num_pipes,
                                         pipes[-1] if len(pipes) > 0 else None, 0.2)

    colors = [player.color for player in players]
    color = choice(colors)

    # Generate a single pipe if there's enough of a gap between the previous pipe
    if len(pipes) > 0 and pipes[-1].top_rect.x < screen.get_width() - pipe_info.gap or len(pipes) == 0:
        screen_height = screen.get_height()
        height_gap = screen_height * pipe_info.pipe_gap
        top_height = screen_height * pipe_info.center - height_gap
        bottom_height = screen_height * (1 - pipe_info.center) - height_gap

        top_rect = Rect(x, 0, width, top_height)
        bottom_rect = Rect(x, screen_height - bottom_height, width, bottom_height)

        pipe = Pipe(top_rect = top_rect, bottom_rect = bottom_rect, x = x, width = width,
                    color = color, velocity = pipe_info.velocity, center = pipe_info.center,
                    pipe_gap = pipe_info.pipe_gap)
        pipe.whole_rect = Rect(x, 0, width, screen_height)
        pipes.append(pipe)

@dataclass
class PipeInfo:
    velocity: int
    gap: int
    center: float
    pipe_gap: float

def _generate_info(screen: Surface, num_pipes: int, last_pipe: Pipe | None, around: float) -> PipeInfo:
    if last_pipe == None:
        return PipeInfo(500, 500, DEFAULT_CENTER, DEFAULT_PIPE_GAP)

    velocity = DEFAULT_VELOCITY
    gap = int(screen.get_width() / num_pipes)
    center = uniform(last_pipe.center - around, last_pipe.center + around)
    pipe_gap = uniform(last_pipe.pipe_gap - around, last_pipe.pipe_gap + around)

    if center < DEFAULT_MIN_CENTER:
        center = DEFAULT_MIN_CENTER
    if pipe_gap < DEFAULT_MIN_PIPE_GAP:
        pipe_gap = DEFAULT_MIN_PIPE_GAP

    if center > DEFAULT_MAX_CENTER:
        center = DEFAULT_MAX_CENTER
    if pipe_gap > DEFAULT_MAX_PIPE_GAP:
        pipe_gap = DEFAULT_MAX_PIPE_GAP

    return PipeInfo(velocity, gap, center, pipe_gap)
