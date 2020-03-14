test = {
  'name': 'give-interest',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM give_interest_result;
          Alyssa P Hacker|1020.0
          Ben Bitdiddle|2040.0
          Cy D Fect|2346.0
          Eben Scrooge|9996.0
          Louis Reasoner|7956.0
          Robert Cratchet|1224.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
