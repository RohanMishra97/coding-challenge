import os
import sys
from typing import List

import pytest
sys.path.append(os.path.abspath("."))
from src.funktools import fold


def plus(a, b):
    return a + b


plus.__name__ = "+"


def minus(a, b):
    return a - b


minus.__name__ = "-"


@pytest.mark.parametrize("seq, acc, res", [
    ([i for i in range(1, 4)], 0, 6),
    (["fold", " like", " protein"], "", "fold like protein"),
    ([1, 2, 3], None, 6)
])
def test_plus_fold(seq, acc, res):
    assert fold(seq, plus, acc) == res


def test_non_iterable():
    with pytest.raises(TypeError):
        fold(None, plus, 0.0)


def test_empty_seq_no_init():
    with pytest.raises(TypeError):
        fold([], plus, None)


def test_lfold():
    x: List[int] = [1, 3, 4, 5]
    x0 = 10
    res = fold(x, minus, x0, foldr=False)
    assert res == -3


def test_rfold():
    x: List[int] = [1, 3, 4, 5]
    x0 = 10
    res = fold(x, minus, x0, foldr=True)
    assert res == 7