from .player import Player, get_color, sort_players_by_color
from .game import post_event
from .event import RESET, post_event
from .defaults import DEFAULT_NUM_MAX_PLAYERS

def hit(effect, players, i, message: str) -> None:
    print(message)

def hadamard_effect(effect, players, i) -> None:
    color = players[i].color
    dict_players = sort_players_by_color(players)

    
    for j, player in enumerate(dict_players[color]):
        # inverse direction
        players.append(Player(rect = player.rect.copy(), height_limit = player.height_limit,
                              fun = player.fun, velocity = (-1) ** (j + 1 % 2) * player.velocity,
                              jump_force = (-1) ** (j + 1 % 2) * player.jump_force,
                              gravity = (-1) ** (j + 1 % 2) * player.gravity, color = color,
                              sprite = player.sprite.copy()))

def measure(effect, players, i) -> None:
    color = players[i].color
    dict_players = sort_players_by_color(players)
    
    for player in dict_players[color]:
        players.remove(player)
    if len(players) == 0:
        post_event(RESET)

def new_qubit(effect, players, i) -> None:
    dict_player = sort_players_by_color(players)
    if len(dict_player.keys()) != DEFAULT_NUM_MAX_PLAYERS:
        players.append(Player(rect = players[i].rect.copy(), height_limit = players[i].height_limit,
                              fun = players[i].fun, velocity = 0, color = get_color(),
                              sprite = players[i].sprite.copy()))

def x_gate(effect, players, i) -> None:
    players[i].velocity = 0
    players[i].gravity = - players[i].gravity
    players[i].jump_force = - players[i].jump_force

EFFECT_FUNCTIONS = [hadamard_effect, measure, new_qubit, x_gate]
EFFECT_SHAPE = ["rect", "rect", "circle", "rect"]
EFFECT_COLOR = ["white", "white", "blue", "white"]
EFFECT_SPRITE = ["src/sprites/Hadamard.png", "src/sprites/Meter.png", None, "src/sprites/XGate.png"]
EFFECT_FUNCTION_ARGS = [(), (), (), ()]
