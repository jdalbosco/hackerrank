PLAYER_ONE_WINS = 1
PLAYER_TWO_WINS = 2

def tower_breakers(n_of_towers, towers_height):
    return PLAYER_ONE_WINS if n_of_towers % 2 != 0 and towers_height != 1 else PLAYER_TWO_WINS