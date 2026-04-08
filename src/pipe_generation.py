from .defaults import DEFAULT_CENTER, DEFAULT_PIPE_GAP, DEFAULT_MIN_PIPE_GAP
from .defaults import DEFAULT_MIN_CENTER, DEFAULT_MAX_PIPE_GAP, DEFAULT_MAX_CENTER

from .pipe import Pipe
from random import uniform

def generate_info(last_pipe: Pipe | None, around: float) -> tuple[float, float]:
    if last_pipe == None:
        return (DEFAULT_CENTER, DEFAULT_PIPE_GAP)

    center = uniform(last_pipe.center - around, last_pipe.center + around)
    pipe_gap = uniform(last_pipe.pipe_gap - around, last_pipe.pipe_gap + around)

    if center < DEFAULT_MIN_CENTER:
        center = DEFAULT_MIN_CENTER
    if pipe_gap < DEFAULT_MIN_CENTER:
        pipe_gap = DEFAULT_MIN_PIPE_GAP

    if center > DEFAULT_MAX_CENTER:
        center = DEFAULT_MAX_CENTER
    if pipe_gap > DEFAULT_MAX_CENTER:
        pipe_gap = DEFAULT_MAX_PIPE_GAP

    return (center, pipe_gap)
