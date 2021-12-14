def move(start, finish):
    a = [[100 for _ in '1'*12] for _ in '1'*12]
    a[start[0]+1][start[1]+1] = 0
    for _ in '1'*8:
        for i in range(2, 10):
            for j in range(2, 10):
                if a[i][j] > 0:
                    a[i][j] = min(a[i-2][j-1], a[i-2][j+1], a[i-1][j-2],
                                  a[i-1][j+2], a[i+2][j-1], a[i+2][j+1],
                                  a[i+1][j-2], a[i+1][j+2])+1
    return a[finish[0]+1][finish[1]+1]


def collision(start, finish):
    return -1 if move(start, finish) % 2 > 0 else move(start, finish) // 2
