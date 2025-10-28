import random
def choose_size():
    size = int(input("choose the size of the game "))
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
    card_x = int(input("enter the column of the card "))-1
    card_y = int(input("enter the line of the card "))-1

    return card_x,card_y

def is_won(mat1,mat2):
    return mat1 == mat2
