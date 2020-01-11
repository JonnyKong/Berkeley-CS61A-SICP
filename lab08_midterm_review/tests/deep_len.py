test = {
  'name': 'deep_len',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> deep_len(Link(1, Link(2, Link(3))))
          3
          >>> deep_len(Link(Link(1, Link(2)), Link(3, Link(4))))
          4
          >>> levels = Link(Link(Link(1, Link(2)),             Link(3)), Link(Link(4), Link(5)))
          >>> print(levels)
          <<<1 2> 3> <4> 5>
          >>> deep_len(levels)
          5
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
