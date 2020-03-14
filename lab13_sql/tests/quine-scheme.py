test = {
  'name': 'quine',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (null? quine)
          #f
          scm> (list? quine)
          #t
          scm> (equal? quine (eval quine))
          #t
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
