test = {
  'name': 'num_trees',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> num_trees(1)
          1
          >>> num_trees(2)
          1
          >>> num_trees(3)
          2
          >>> num_trees(8)
          429
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
