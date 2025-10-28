import random
def create_matrix(size,fill = 0):
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

def create_game(mat,card_lst):
    print(card_lst)
    for i in range(len(mat)):
        for j in range(len(mat)):
            card = random.choice(card_lst)
            mat[i][j] = card
            card_lst.remove(card)
    return mat
