test = {
  'name': 'trade',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> a = [1, 1, 3, 2, 1, 1, 4]
          >>> b = [4, 3, 2, 7]
          >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
          'Deal!'
          >>> a
          [4, 3, 1, 1, 4]
          >>> b
          [1, 1, 3, 2, 2, 7]
          >>> c = [3, 3, 2, 4, 1]
          >>> trade(b, c)
          'No deal!'
          >>> b
          [1, 1, 3, 2, 2, 7]
          >>> c
          [3, 3, 2, 4, 1]
          >>> trade(a, c)
          'Deal!'
          >>> a
          [3, 3, 2, 1, 4]
          >>> b
          [1, 1, 3, 2, 2, 7]
          >>> c
          [4, 3, 1, 4, 1]
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
