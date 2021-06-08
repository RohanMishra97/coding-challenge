import os
import sys
import pytest
sys.path.append(os.path.abspath("."))
from src.funktools import fold


@pytest.mark.parametrize("seq, acc, res", [
    ([i for i in range(1, 4)], 0, 6),
    (["fold", " like", " protein"], "", "fold like protein"),
])
def test_plus_fold(seq, acc, res):
    def plus(a, b):
        return a + b
    assert fold(seq, plus, acc) == res