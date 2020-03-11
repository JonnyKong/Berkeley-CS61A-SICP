test = {
  'name': 'obedience',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM obedience LIMIT 10;
          seven|Image 4
          7|Image 3
          the number 7 below.|Image 5
          7|Image 5
          You're not the boss of me!|Image 1
          7|Image 3
          Choose this option instead|Image 4
          7|Image 5
          You're not the boss of me!|Image 4
          Choose this option instead|Image 1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
