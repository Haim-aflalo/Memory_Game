def create_matrix(size,fill = 0):
    mat = []
    for i in range(size):
        lst = []
        for j in range(size):
            lst.append(fill)
        mat.append(lst)
    return mat

