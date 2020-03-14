test = {
  'name': 'split-accounts',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM split_account_results order by name;
          Alyssa P Hacker's Checking account|510.0
          Alyssa P Hacker's Savings account|510.0
          Ben Bitdiddle's Checking account|1020.0
          Ben Bitdiddle's Savings account|1020.0
          Cy D Fect's Checking account|1173.0
          Cy D Fect's Savings account|1173.0
          Eben Scrooge's Checking account|4998.0
          Eben Scrooge's Savings account|4998.0
          Louis Reasoner's Checking account|3978.0
          Louis Reasoner's Savings account|3978.0
          Robert Cratchet's Checking account|612.0
          Robert Cratchet's Savings account|612.0
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
