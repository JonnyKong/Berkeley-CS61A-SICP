test = {
  'name': 'matchmaker',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker LIMIT 10;
          dog|Everytime We Touch|blue|green
          dog|Everytime We Touch|blue|blue
          dog|Everytime We Touch|blue|blue
          dog|The Middle|black.|red
          dog|The Middle|black.|purple
          dog|The Middle|black.|dark blue
          dog|The Middle|black.|blue
          dog|The Middle|black.|light blue
          dog|The Middle|black.|green
          dog|The Middle|black.|green
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
