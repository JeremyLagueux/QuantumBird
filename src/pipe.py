from pygame import Surface, Rect, draw
from .defaults import DEFAULT_CENTER, DEFAULT_PIPE_GAP, DEFAULT_VELOCITY, DEFAULT_MAX_CENTER, \
    DEFAULT_MAX_PIPE_GAP, DEFAULT_MIN_PIPE_GAP, DEFAULT_MIN_CENTER
from random import uniform

class Pipe:
    def __init__(self, top_rect: Rect, bottom_rect: Rect, x: int, width: int, color: str,
                 velocity: int = DEFAULT_VELOCITY, pipe_gap: float = DEFAULT_PIPE_GAP,
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

def generate_pipe(pipes: list[Pipe], velocity: int, x: int, width: int,
                  center: float, pipe_gap: float, color: str, screen: Surface,
                  gap: int, num_pipes: int) -> None:
    # Remove pipes that are out of bounds
    for pipe in pipes:
        if pipe.top_rect.x + pipe.top_rect.width < 0:
            pipes.remove(pipe)

    # Don't generate if there's enough pipes
    if len(pipes) >= num_pipes:
        return

    # Generate a single pipe if there's enough of a gap between the previous pipe
    if len(pipes) > 0 and pipes[-1].top_rect.x < screen.get_width() - gap or len(pipes) == 0:
        screen_height = screen.get_height()
        height_gap = screen_height * pipe_gap
        top_height = screen_height * center - height_gap
        bottom_height = screen_height * (1 - center) - height_gap

        top_rect = Rect(x, 0, width, top_height)
        bottom_rect = Rect(x, screen_height - bottom_height, width, bottom_height)

        pipe = Pipe(top_rect = top_rect, bottom_rect = bottom_rect, x = x, width = width,
                    color = color, velocity = velocity, center = center, pipe_gap = pipe_gap)
        pipe.whole_rect = Rect(x, 0, width, screen_height)
        pipes.append(pipe)

def generate_info(last_pipe: Pipe | None, around: float) -> tuple[float, float]:
    if last_pipe == None:
        return (DEFAULT_CENTER, DEFAULT_PIPE_GAP)

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

    return (center, pipe_gap)
