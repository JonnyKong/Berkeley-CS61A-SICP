""" Lab 04 """


this_file = __file__

def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0 or n == 1:
        return n
    else:
        return n + skip_add(n - 2)

def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n == 1:
        return term(1)
    else:
        return term(n) + summation(n - 1, term)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a < b:
        b, a = a, b
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def couple(s1, s2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> s1 = [1, 2, 3]
    >>> s2 = [4, 5, 6]
    >>> couple(s1, s2)
    [[1, 4], [2, 5], [3, 6]]
    >>> s3 = ['c', 6]
    >>> s4 = ['s', '1']
    >>> couple(s3, s4)
    [['c', 's'], [6, '1']]
    """
    assert len(s1) == len(s2)
    "*** YOUR CODE HERE ***"
    return [list(x) for x in zip(s1, s2)]

def enumerate(s, start=0):
    """Returns a list of lists, where the i-th list contains i+start and
    the i-th element of s.
    >>> enumerate([6, 1, 'a'])
    [[0, 6], [1, 1], [2, 'a']]
    >>> enumerate('five', 5)
    [[5, 'f'], [6, 'i'], [7, 'v'], [8, 'e']]
    """
    "*** YOUR CODE HERE ***"
    return couple(range(start, len(s) + start), s)

# Optional problems

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"

def key_of_min_value(d):
    """Returns the key in a dict d that corresponds to the minimum value of d.
    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    >>> min(letters)
    'a'
    >>> key_of_min_value(letters)
    'c'
    """
    "*** YOUR CODE HERE ***"

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    