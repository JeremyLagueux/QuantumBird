from .player import Player, get_color

def hit(effect, players, i, message: str) -> None:
    print(message)

def hadamard_effect(effect, players, i) -> None:
    players.append(Player(players[i].rect.copy(), players[i].height_limit, players[i].fun,
                          -players[i].velocity, -players[i].jump_force, -players[i].gravity))

def new_qubit(effect, players, i) -> None:
    players.append(Player(players[i].rect.copy(), players[i].height_limit, players[i].fun,
                          0, color = get_color()))

def x_gate(effect, players, i) -> None:
    players[i].velocity = 0
    players[i].gravity = - players[i].gravity
    players[i].jump_force = - players[i].jump_force

EFFECT_FUNCTIONS = [None, hadamard_effect, x_gate, new_qubit]
EFFECT_SHAPE = [None, "rect", "rect", "circle"]
EFFECT_COLOR = [None, "blue", "red", "white"]
EFFECT_FUNCTION_ARGS = [None, (), (), ()]
