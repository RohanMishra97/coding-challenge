from collections.abc import Iterable, Callable


def fold(x: Iterable, func: Callable, init_val=None, foldr=False):
    """
    fold is a higher-order-function that processes a data structure using a given combination operation
     to build up a return value. (https://en.wikipedia.org/wiki/Fold_%28higher-order_function%29)
    :param x: iterable sequence to be processed
    :param func: accumulator function
    :param init_val: initial value (In case of None, folding starts from 1st element of sequence)
    :param foldr: evaluation order set to right-most element first if True (default = False)
    :return: folded/accumulated result
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
    for element in it:
        res = func(element, res) if foldr else func(res, element)
    assert type(res) == rtype  # sanity check
    return res
