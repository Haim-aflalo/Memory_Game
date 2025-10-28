import random



def choose_size():
    while True:
        size_str = input("choose the size of the game ")
        if not size_str.isdigit():
            print("only numbers")
            continue
        size = int(size_str)
        if size % 2 != 0:
            print("only even numbers")
            continue
        else:
            return size

def game_board_matrix(size,fill = 0):
    mat = []
    for i in range(size):
        col = []
        for j in range(size):
            col.append(fill)
        mat.append(col)
    return mat

def create_cards(size):
    cards = []
    for i in range(1,size*(size//2)+1):
        cards.append(i)
        cards.append(i)
    return cards

def create_game(size,card_lst):
    mat =[]
    for i in range(size):
        lst = []
        for j in range(size):
            card = random.choice(card_lst)
            lst.append(card)
            card_lst.remove(card)
        mat.append(lst)

    return mat

def  choose_card():
    while True:
        card_x_str = input("enter the column of the card ")
        if not card_x_str.isdigit():
            print("only numbers")
            continue
        card_x = int(card_x_str)-1
        card_y_str = input("enter the line of the card ")
        if not card_y_str.isdigit():
            print("only numbers")
            continue
        card_y = int(card_y_str)-1
        return card_x,card_y

def is_won(mat1,mat2):
    return mat1 == mat2
