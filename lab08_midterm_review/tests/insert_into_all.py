test = {
  'name': 'insert_into_all',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> nl = [[], [1, 2], [3]]
          >>> insert_into_all(0, nl)
          [[0], [0, 1, 2], [0, 3]]
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
