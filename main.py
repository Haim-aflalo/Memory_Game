from memory import game,utils
from memory.game import play_game

if __name__ == "__main__":
    size = utils.choose_size()
    print(play_game(size))