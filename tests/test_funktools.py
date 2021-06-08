import os
import sys
import pytest
sys.path.append(os.path.abspath("."))
from src.funktools import fold


def plus(a, b):
    return a + b


plus.__name__ = "+"


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