from .pipe import Pipe, generate_pipe
from .defaults import DEFAULT_CENTER, DEFAULT_PIPE_GAP
from random import uniform

def generate_info(last_pipe: Pipe | None, around: float) -> tuple[float, float]:
    if last_pipe == None:
        return (DEFAULT_CENTER, DEFAULT_PIPE_GAP)

    center = uniform(last_pipe.center - around, last_pipe.center + around)
    pipe_gap = uniform(last_pipe.pipe_gap - around, last_pipe.pipe_gap + around)
    return (center, pipe_gap)
