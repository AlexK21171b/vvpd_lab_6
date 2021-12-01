import argparse

parser = argparse.ArgumentParser(description="Про шахматного коня")
parser.add_argument("-s", "--start", type=int, help="Начало", nargs=2, default=[1, 1])
parser.add_argument("-f", "--finish", type=int, help="Конец", nargs=2, default=[8, 8])
args = parser.parse_args()


def knight_move(start, finish):
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


