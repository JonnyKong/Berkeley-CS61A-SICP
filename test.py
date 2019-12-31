a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def key_func(a):
    return a % 3

b = a.sort(key=key_func)