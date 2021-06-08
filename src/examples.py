from typing import List, Tuple
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


def example_5():
    """
    Using fold to perform Map operation (squaring each element)
    ```console
    ([])sq_mp1	=[1]
    (([])sq_mp1)sq_mp2	=[1, 4]
    ((([])sq_mp1)sq_mp2)sq_mp3	=[1, 4, 9]
    fold([1, 2, 3],sq_mp, []) = [1, 4, 9]
    ```
    """
    square_map = lambda x, y: x + [y ** 2]
    square_map.__name__ = "sq_map"
    x: List[int] = [i for i in range(1, 4)]
    x0: List = []
    res = fold(x, square_map, x0, debug=True)
    print(f"fold({x},{square_map.__name__}, {x0}) = {res}")


def example_6():
    """
    Using fold to perform Filter operation (filter only even terms)
    ```console
    ([])is_even1	=[]
    (([])is_even1)is_even2	=[2]
    ((([])is_even1)is_even2)is_even3	=[2]
    fold([1, 2, 3],is_even,[])=[2]
    ```
    """
    even_fltr = lambda x, y: x + [y] if y % 2 == 0 else x
    even_fltr.__name__ = "is_even"
    x: List[int] = [i for i in range(1,4)]
    x0: List = []
    res = fold(x, even_fltr, x0, debug=True)
    print(f"fold({x},{even_fltr.__name__},{x0})={res}")


def example_7():
    """
    Using fold to generate Prefix List.
    ```console
    ([])pre1	=[[1]]
    (([])pre1)pre3	=[[1], [1, 3]]
    ((([])pre1)pre3)pre4	=[[1], [1, 3], [1, 3, 4]]
    (((([])pre1)pre3)pre4)pre5	=[[1], [1, 3], [1, 3, 4], [1, 3, 4, 5]]
    fold([1, 3, 4, 5],pre, []) = [[1], [1, 3], [1, 3, 4], [1, 3, 4, 5]]
    ```
    """
    pre = lambda x, y: [[y]] if len(x) == 0 else x + [x[-1] + [y]]
    pre.__name__ = "pre"
    x: List[int] = [1, 3, 4, 5]
    x0 = []
    res = fold(x, pre, x0, debug=True)
    print(f"fold({x},{pre.__name__}, {x0}) = {res}")


def example_8():
    """
    Using fold to compose functions.
    ```console
    square(10.0)	=100.0
    inverse(square(10.0))	=0.01
    twice(inverse(square(10.0)))	=0.02
    ```
    """
    def twice(x): return 2 * x;
    def square(x): return x ** 2;
    def inverse(x): return 1 / x;
    def compose(x, y): return x(y);
    compose.__name__ = ""
    res = fold([twice, inverse, square], compose, 10.0, foldr=True, debug=True)
    print(res)


if __name__ == '__main__':
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    example_6()
    example_7()
    example_8()
