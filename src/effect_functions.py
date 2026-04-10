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
        players.append(Player(player.rect.copy(), player.height_limit, player.fun,
                              (-1) ** (j + 1 % 2) * player.velocity,
                              (-1) ** (j + 1 % 2) * player.jump_force,
                              (-1) ** (j + 1 % 2) * player.gravity, color = color))

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
        players.append(Player(players[i].rect.copy(), players[i].height_limit, players[i].fun,
                              0, color = get_color()))

def x_gate(effect, players, i) -> None:
    players[i].velocity = 0
    players[i].gravity = - players[i].gravity
    players[i].jump_force = - players[i].jump_force

EFFECT_FUNCTIONS = [hadamard_effect, measure, new_qubit, x_gate]
EFFECT_SHAPE = ["rect", "rect", "circle", "rect"]
EFFECT_COLOR = ["white", "black", "blue", "red"]
EFFECT_FUNCTION_ARGS = [(), (), (), ()]
