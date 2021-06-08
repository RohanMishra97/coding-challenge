from typing import List
from src.funktools import fold


def main():
    x: List[int] = [1, 3, 4, 5]
    x0 = 10
    minus = lambda a, b: a - b
    minus.__name__ = "-"
    res1 = fold(x, minus, x0, foldr=False)
    print(f"fold({x},{minus.__name__}, {x0}, foldr={False}) = {res1}")
    res2 = fold(x, minus, x0, foldr=True)
    print(f"fold({x},{minus.__name__}, {x0}, foldr={True}) = {res2}")


if __name__ == '__main__':
    main()