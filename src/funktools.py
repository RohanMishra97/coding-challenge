def fold(x, func, init_val=None):
    it = iter(x)
    res = init_val if init_val else next(it)
    for element in it:
        res = func(res, element)
    return res

