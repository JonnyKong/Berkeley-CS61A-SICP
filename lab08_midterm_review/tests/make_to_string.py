test = {
  'name': 'make_to_string',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> kevins_to_string = make_to_string("[", "|-]-->", "", "[]")
          >>> jerrys_to_string = make_to_string("(", " . ", ")", "()")
          >>> lst = Link(1, Link(2, Link(3, Link(4))))
          >>> kevins_to_string(lst)
          '[1|-]-->[2|-]-->[3|-]-->[4|-]-->[]'
          >>> kevins_to_string(Link.empty)
          '[]'
          >>> jerrys_to_string(lst)
          '(1 . (2 . (3 . (4 . ()))))'
          >>> jerrys_to_string(Link.empty)
          '()'
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
