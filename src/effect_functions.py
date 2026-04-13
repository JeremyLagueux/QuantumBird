from .player import Player, get_color, sort_players_by_color
from .game import post_event
from .event import RESET, post_event
from .defaults import DEFAULT_NUM_MAX_PLAYERS

from random import choice

def hit(effect, players, i, message: str) -> None:
    print(message)

def hadamard_effect(effect, players, i) -> None:
    color = players[i].color
    dict_players = sort_players_by_color(players)

    if len(dict_players[color]) > 1:
        players.remove(players[i])

    else:
        players.append(Player(rect = players[i].rect.copy(), height_limit = players[i].height_limit,
                              fun = players[i].fun, velocity = (-1) * players[i].velocity,
                              jump_force = (-1) * players[i].jump_force,
                              gravity = (-1) * players[i].gravity, color = color,
                              sprite = players[i].sprite.copy()))

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

def cx_gate(effect, players, i, color1: str, color2: str) -> None:
    dict_players = sort_players_by_color(players)

    if dict_players[color1][0].gravity < 0:
        for player in dict_players[color2]:
            player.velocity = 0
            player.gravity = - player.gravity
            player.jump_force = - player.jump_force
    

def x_gate(effect, players, i) -> None:
    players[i].velocity = 0
    players[i].gravity = - players[i].gravity
    players[i].jump_force = - players[i].jump_force

EFFECT_FUNCTIONS = [hadamard_effect, measure, new_qubit, x_gate, cx_gate]
EFFECT_SHAPE = ["rect", "rect", "circle", "rect", "rect"]
EFFECT_COLOR = ["white", "white", "blue", "white", "white"]
EFFECT_SPRITE = ["src/sprites/Hadamard.png", "src/sprites/Meter.png", None, "src/sprites/XGate.png", None]
EFFECT_FUNCTION_ARGS = [(), (), (), (), ()]
