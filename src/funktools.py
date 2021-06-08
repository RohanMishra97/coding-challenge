from collections.abc import Iterable, Callable


def fold(x: Iterable, func: Callable, init_val=None):
    it = iter(x)
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
        res = func(res, element)
    assert type(res) == rtype  # sanity check
    return res
