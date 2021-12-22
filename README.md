# Алгоритм задачи "Про шахматного коня"
## Постановка задачи
В шахматах конь является весьма уникальной фигурой, а всё из-за схемы его хода. За один ход конь может преодолеть маршрут напоминающий букву «Г». Также математически доказано, что конь за некоторое количество ходов может из любой клетки попасть в любую другую.

![](https://sun9-30.userapi.com/impg/148a60iH8Tq-tIY39jTbNj3k05EvO1trkN1eLA/x8dKhNN8xLY.jpg?size=250x250&quality=95&sign=ef6b3f78650f50ee751317aec0b8a2a9&type=album)

Принцип перемещения коня

### Необходимо было написать две функции
- [X] первая будет считать количество ходов, необходимое коню чтобы добраться из одной клетки шахматной доски до другой;
- [X] вторая будет считать, через какое минимальное количество ходов могут встретиться два коня, расположенных на двух разных клетках доски.
### Входные данные
На вход каждой функции поступают два кортежа целых чисел 𝐶𝑖 таких, что
каждое 8 ≥ 𝐶𝑖 ≥ 1. Для первой функции эти кортежи: стартовая позиция коня и
клетка, на которую коню нужно переместиться; для второй функции эти
кортежи: позиция первого коня и позиция второго коня.
# Реализация алгоритма
## 1 этап реализпции
#### [Подробное описание работы функциий см. в документации модуля knight.py](https://github.com/AlexK21171b/vvpd_6_lab/blob/master/package/knight.py)
Сперва реализованна функция которая считает количество ходов, необходимое коню чтобы добраться из одной клетки шахматной доски до другой.
```
from itertools import product


def move(start, finish):

    a = [[100 for _ in '1'*12] for _ in '1'*12]
    a[start[0]+1][start[1]+1] = 0
    for _, i, j in product('1'*8, range(2, 10), range(2, 10)):
        if a[i][j] > 0:
            a[i][j] = min(a[i-2][j-1], a[i-2][j+1], a[i-1][j-2],
                          a[i-1][j+2], a[i+2][j-1], a[i+2][j+1],
                          a[i+1][j-2], a[i+1][j+2])+1
    return a[finish[0]+1][finish[1]+1]
```
## 2 этап реализпции
Потом реализованна функция которая считает, через какое минимальное количество ходов могут встретиться два коня, расположенных на двух разных клетках доски.
```
def collision(start, finish):
    return -1 if move(start, finish) % 2 > 0 else move(start, finish) // 2
```
# Тестирование кода
Для проверки безошибочной проверки кода было написанно несколько тестов у в отдельном модуле с использованием модуля [pytest](https://pytest.org/en/latest/).
```
from package import knight
import pytest


@pytest.mark.parametrize("start, finish, result", [((8, 8), (1, 1), 6),
                                                   ((1, 8), (1, 1), 5),
                                                   ((3, 3), (1, 1), 4),
                                                   ((5, 8), (1, 4), 4),
                                                   ((3, 8), (4, 2), 3)])
def test_move_good(start, finish, result):
    assert knight.move(start, finish) == result


def test_move_very_bad():
    with pytest.raises(IndexError):
        assert knight.move((19, 91), (20, 21))


@pytest.mark.parametrize("start, finish, result", [((8, 8), (1, 1), 3),
                                                   ((1, 8), (1, 1), -1),
                                                   ((3, 3), (1, 1), 2),
                                                   ((5, 8), (1, 4), 2),
                                                   ((3, 8), (4, 2), -1)])
def test_collision_good(start, finish, result):
    assert knight.collision(start, finish) == result
```
# Полезные ресурсы
[Шахматный конь](https://www.chess.com/ru/terms/kon)

[Python для начинающих](https://www.cyberforum.ru/python-beginners/)
