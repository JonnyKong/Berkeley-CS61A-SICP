test = {
  'name': 'permutations',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> perms = permutations([100])
          >>> type(perms)
          <class 'generator'>
          >>> next(perms)
          [100]
          >>> try:
          ...     next(perms)
          ... except StopIteration:
          ...     print('No more permutations!')
          No more permutations!
          >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
          [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
          >>> sorted(permutations((10, 20, 30)))
          [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
          >>> sorted(permutations("ab"))
          [['a', 'b'], ['b', 'a']]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '>>> from lab08_extra import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
