test = {
  'name': 'whoops',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> create table accounts as select 1 as n; -- if this fails, the table must still exist
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
