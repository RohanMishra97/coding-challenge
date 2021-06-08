from collections.abc import Iterable, Callable


def fold(x: Iterable, func: Callable, init_val=None, foldr=False, debug=False):
    """
    fold is a higher-order-function that processes a data structure using a given combination operation
     to build up a return value. (https://en.wikipedia.org/wiki/Fold_%28higher-order_function%29)<br>
    :param x: iterable sequence to be processed<br>
    :param func: accumulator function<br>
    :param init_val: initial value (In case of None, folding starts from 1st element of sequence)<br>
    :param foldr: evaluation order set to right-most element first if True (default = False)<br>
    :param debug: prints structural transformation on each iteration.<br>
    :return: folded/accumulated result<br>
    """
    it = iter(reversed(x)) if foldr else iter(x)
    if init_val is None:
        try:
            res = next(it)
            rtype = type(res)
        except StopIteration:
            raise TypeError(f"Invalid iterable: {x} & init value: {init_val}")
    else:
        res = init_val
        rtype = type(init_val)
    infix = f"{res}"
    for element in it:
        res = func(element, res) if foldr else func(res, element)
        if debug:
            if callable(element):
                infix = f"{element.__name__}{func.__name__}({infix})" if foldr else f"({infix}){func.__name__}{element.__name__}"
            else:
                infix = f"{element}{func.__name__}({infix})" if foldr else f"({infix}){func.__name__}{element}"
            print(f"{infix}\t={res}")
    assert type(res) == rtype  # sanity check
    return res
