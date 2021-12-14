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
