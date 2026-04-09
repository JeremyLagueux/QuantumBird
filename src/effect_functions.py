from .player import Player

def hit(effect, players, i, message: str) -> None:
    print(message)

def generate_player(effect, players, i) -> None:
    players.append(Player(players[i].rect.copy(), players[i].height_limit, players[i].fun,
                          -players[i].velocity, -players[i].jump_force, -players[i].gravity))

EFFECT_FUNCTIONS = [None, hit, generate_player]
EFFECT_FUNCTION_ARGS = [None, ("Hit",), ()]
