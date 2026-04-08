from pygame import Surface, Rect, draw
from dataclasses import dataclass

@dataclass
class Pipe:
    velocity: float
    top_rect: Rect
    bottom_rect: Rect
    x: int
    width: int
    center: float
    pipe_gap: float
    color: str
    
    def draw(self, screen: Surface) -> None:
        draw.rect(screen, self.color, self.top_rect)
        draw.rect(screen, self.color, self.bottom_rect)

    def move(self, dt) -> None:
        self.top_rect.x -= self.velocity * dt
        self.bottom_rect.x -= self.velocity * dt

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

        pipe = Pipe(velocity, top_rect, bottom_rect, x, width, center, pipe_gap, color)
        pipes.append(pipe)
