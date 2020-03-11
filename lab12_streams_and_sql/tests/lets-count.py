test = {
  'name': 'lets-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from fa19favpets;
          dog|58
          cat|27
          panda|23
          tiger|14
          elephant|9
          dolphin|8
          penguin|8
          turtle|5
          cheetah|4
          doggo|4
          sqlite> SELECT * from fa19dog;
          dog|58
          sqlite> SELECT * from obedienceimages;
          7|Image 1|26
          7|Image 2|25
          7|Image 3|21
          7|Image 4|35
          7|Image 5|31
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
