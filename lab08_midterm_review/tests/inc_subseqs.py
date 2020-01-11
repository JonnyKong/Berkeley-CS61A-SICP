test = {
  'name': 'inc_subseqs',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> seqs = inc_subseqs([1, 3, 2])
          >>> sorted(seqs)
          [[], [1], [1, 2], [1, 3], [2], [3]]
          >>> inc_subseqs([])
          [[]]
          >>> seqs2 = inc_subseqs([1, 1, 2])
          >>> sorted(seqs2)
          [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '>>> from lab08 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
