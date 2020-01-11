test = {
  'name': 'Keyboard',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> b1 = Button(0, "H")
          >>> b2 = Button(1, "I")
          >>> k = Keyboard(b1, b2)
          >>> k.buttons[0].key
          'H'
          >>> k.press(1)
          'I'
          >>> k.press(2) #No button at this position
          ''
          >>> k.typing([0, 1])
          'HI'
          >>> k.typing([1, 0])
          'IH'
          >>> b1.times_pressed
          2
          >>> b2.times_pressed
          3
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
