test = {
  'name': 'shuffle',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> shuffle(range(6))
          [0, 3, 1, 4, 2, 5]
          >>> suits = ['♡', '♢', '♤', '♧']
          >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
          >>> cards[:12]
          ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
          >>> cards[26:30]
          ['7♤', '7♧', '8♡', '8♢']
          >>> shuffle(cards)[:12]
          ['A♡', '7♤', 'A♢', '7♧', 'A♤', '8♡', 'A♧', '8♢', '2♡', '8♤', '2♢', '8♧']
          >>> shuffle(shuffle(cards))[:12]
          ['A♡', '4♢', '7♤', '10♧', 'A♢', '4♤', '7♧', 'J♡', 'A♤', '4♧', '8♡', 'J♢']
          >>> cards[:12]  # Should not be changed
          ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
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
