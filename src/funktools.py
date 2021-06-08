def fold(x, func, init_val):
    res = init_val
    for element in x:
        res = func(res, element)
    return res

