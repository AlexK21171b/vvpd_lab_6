"""
Главный модуль для работы с алгортимом через консоль,
на вход поступают 2 кортежа, со значениями от 1 до 8
"""

from knight import *
import argparse

parser = argparse.ArgumentParser(description="Про шахматного коня")
parser.add_argument("-s", "--start", type=int, help="Начало", nargs=2, default=[1, 1], choices=[1, 2, 3, 4, 5, 7, 8])
parser.add_argument("-f", "--finish", type=int, help="Конец", nargs=2, default=[8, 8], choices=[1, 2, 3, 4, 5, 7, 8])
args = parser.parse_args()
print(move(args.start, args.finish))
print(collision(args.start, args.finish))
