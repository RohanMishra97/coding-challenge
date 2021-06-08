from typing import List
from src.funktools import fold


def example_1():
    """
    Add a list of ints
    ```console
    (0)+1	=1
    ((0)+1)+2	=3
    (((0)+1)+2)+3	=6
    fold([1, 2, 3], +, 0) = 6
    ```
    """
    def plus(a, b):
        return a + b
    plus.__name__ = "+"
    x: List[int] = [i for i in range(1, 4)]
    x0 = 0
    res = fold(x, plus, x0, debug=True)
    print(f"fold({x}, {plus.__name__}, {x0}) = {res}")


def example_2():
    """
    Concatenates list of string
    ```console
        ()+fold	=fold
        (()+fold)+ like	=fold like
        ((()+fold)+ like)+ protein	=fold like protein
        fold(['fold', ' like', ' protein'], +, ) = fold like protein
    ```
    """
    def plus(a, b):
        return a + b
    plus.__name__ = "+"
    x: List[str] = ["fold", " like", " protein"]
    x0 = ""
    res = fold(x, plus, x0, debug=True)
    print(f"fold({x}, {plus.__name__}, {x0}) = {res}")


def example_3():
    """
    Concatenates a mixed tuple of floats and ints
    ```console
    (0.0)+1	=1.0
    ((0.0)+1)+2.3	=3.3
    (((0.0)+1)+2.3)+3	=6.3
    ((((0.0)+1)+2.3)+3)+4.2	=10.5
    fold((1, 2.3, 3, 4.2), +, 0.0) = 10.5
    ```
    """
    def plus(a, b):
        return a + b
    plus.__name__ = "+"
    x: Tuple[int, float, int, float] = (1, 2.3, 3, 4.2)
    x0 = 0.0
    res = fold(x, plus, x0, debug=True)
    print(f"fold({x}, {plus.__name__}, {x0}) = {res}")


def example_4():
    """
    Comparison of foldl & foldr.<br>
    *foldl*
    ```console
    (10)-1	=9
    ((10)-1)-3	=6
    (((10)-1)-3)-4	=2
    ((((10)-1)-3)-4)-5	=-3
    fold([1, 3, 4, 5],-, 10, foldr=False) = -3
    ```
    *foldr*
    ```console
    5-(10)	=-5
    4-(5-(10))	=9
    3-(4-(5-(10)))	=-6
    1-(3-(4-(5-(10))))	=7
    fold([1, 3, 4, 5],-, 10, foldr=True) = 7
    ```
    """
    x: List[int] = [1, 3, 4, 5]
    x0 = 10
    minus = lambda a, b: a - b
    minus.__name__ = "-"
    res1 = fold(x, minus, x0, foldr=False, debug=True)
    print(f"fold({x},{minus.__name__}, {x0}, foldr={False}) = {res1}")
    res2 = fold(x, minus, x0, foldr=True, debug=True)
    print(f"fold({x},{minus.__name__}, {x0}, foldr={True}) = {res2}")


def main():
    """
    Comparison of foldl & foldr.<br>
    *foldl*
    ```console
    (10)-1	=9
    ((10)-1)-3	=6
    (((10)-1)-3)-4	=2
    ((((10)-1)-3)-4)-5	=-3
    fold([1, 3, 4, 5],-, 10, foldr=False) = -3
    ```
    *foldr*
    ```console
    5-(10)	=-5
    4-(5-(10))	=9
    3-(4-(5-(10)))	=-6
    1-(3-(4-(5-(10))))	=7
    fold([1, 3, 4, 5],-, 10, foldr=True) = 7
    ```
    """
    x: List[int] = [1, 3, 4, 5]
    x0 = 10
    minus = lambda a, b: a - b
    minus.__name__ = "-"
    res1 = fold(x, minus, x0, foldr=False, debug=True)
    print(f"fold({x},{minus.__name__}, {x0}, foldr={False}) = {res1}")
    res2 = fold(x, minus, x0, foldr=True, debug=True)
    print(f"fold({x},{minus.__name__}, {x0}, foldr={True}) = {res2}")


if __name__ == '__main__':
    example_1()
    example_2()
    example_3()
    example_4()