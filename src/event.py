from pygame import USEREVENT, event

INCREMENT_SCORE = USEREVENT + 1
TRIGGER_LOOP = USEREVENT + 2
RESET = USEREVENT + 3
PAUSE = USEREVENT + 4


def post_event(evt_code: int) -> None:
    evt = event.Event(evt_code)
    event.post(evt)
