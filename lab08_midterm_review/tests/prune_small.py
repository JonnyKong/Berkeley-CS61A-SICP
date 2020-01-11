test = {
  'name': 'prune_small',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t1 = Tree(6)
          >>> prune_small(t1, 2)
          >>> t1
          Tree(6)
          >>> t2 = Tree(6, [Tree(3), Tree(4)])
          >>> prune_small(t2, 1)
          >>> t2
          Tree(6, [Tree(3)])
          >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
          >>> prune_small(t3, 2)
          >>> t3
          Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
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
