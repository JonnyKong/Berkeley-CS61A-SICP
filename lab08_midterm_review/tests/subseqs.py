test = {
  'name': 'subseqs',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> seqs = subseqs([1, 2, 3])
          >>> sorted(seqs)
          [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
          >>> subseqs([])
          [[]]
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
