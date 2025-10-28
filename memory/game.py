import copy
import time
from memory import utils


def play_game(size):
    cards = utils.create_cards(size)
    game_board = utils.game_board_matrix(size)
    game_cards = utils.create_game(size,cards)
    counter = 0
    used_point = set()
    while True:
        game_show = copy.deepcopy(game_board)
        print(game_board)
        while True:
            choice_1 = utils.choose_card()
            if choice_1[0] >= size or choice_1[1]>= size:
                print("one of your card doesn't exist please choose another")
                continue
            choice_2 = utils.choose_card()
            if choice_2 == choice_1:
                print("You cant choose the same card")
                continue
            if choice_2[0] >= size or choice_2[1] >= size:
                print("one of your card doesn't exist please choose another")
                continue
            if (choice_1,choice_2) in used_point:
                print("these points were already false")
                continue
            else:
                new = choice_1,choice_2
                used_point.add(new)
                break

        if game_cards[choice_1[0]][choice_1[1]] == game_cards[choice_2[0]][choice_2[1]]:
            game_board[choice_1[0]][choice_1[1]] = game_cards[choice_1[0]][choice_1[1]]
            game_board[choice_2[0]][choice_2[1]] = game_cards[choice_2[0]][choice_2[1]]
            counter += 1
        else:
            game_show[choice_1[0]][choice_1[1]] = game_cards[choice_1[0]][choice_1[1]]
            game_show[choice_2[0]][choice_2[1]] = game_cards[choice_2[0]][choice_2[1]]
            print(game_show)
            time.sleep(3)
            continue
        if utils.is_won(game_board,game_cards):
            print("Yoy Won!!!")
            return counter

