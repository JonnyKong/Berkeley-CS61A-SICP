test = {
  'name': 'Question 5b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # example 1
          >>> s0, s1 = hog.play(lambda score, other: (score + 3) // 4 * 2 + 3, lambda score, other: 4 - other // 4 * 2, score0=0, score1=0, goal=10, dice=always_one)
          >>> s0
          9
          >>> s1
          18
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # example 2
          >>> s0, s1 = hog.play(always(2), always(1), score0=0, score1=0, goal=5, dice=hog.make_test_dice(2, 2))
          >>> s0
          7
          >>> s1
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # swap after feral hogs
          >>> s0, s1 = hog.play(always(2), always(1), score0=45, score1=5, goal=50, dice=hog.make_test_dice(5, 2))
          >>> s0
          5
          >>> s1
          55
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_one = hog.make_test_dice(1)
      >>> always_two = hog.make_test_dice(2)
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=45891, score0=47, score1=53, goal=54, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (47, 53).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (54, 53)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=5192, score0=43, score1=12, goal=47, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (43, 12).
          Player 0 rolls 3 dice and gets outcomes [2, 1, 5].
          End scores = (44, 12)
          >>> print(turns[1])
          Start scores = (44, 12).
          Player 1 rolls 8 dice and gets outcomes [1, 3, 3, 2, 3, 5, 2, 5].
          End scores = (44, 13)
          >>> print(turns[2])
          Start scores = (44, 13).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (53, 13)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=95816, score0=15, score1=45, goal=50, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (15, 45).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 1, 6, 5, 1, 5, 6].
          End scores = (16, 45)
          >>> print(turns[1])
          Start scores = (16, 45).
          Player 1 rolls 3 dice and gets outcomes [5, 2, 4].
          End scores = (16, 56)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25365, score0=3, score1=8, goal=34, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 8).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (13, 8)
          >>> print(turns[1])
          Start scores = (13, 8).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (13, 10)
          >>> print(turns[2])
          Start scores = (13, 10).
          Player 0 rolls 9 dice and gets outcomes [5, 4, 6, 5, 1, 2, 2, 3, 1].
          End scores = (14, 10)
          >>> print(turns[3])
          Start scores = (14, 10).
          Player 1 rolls 10 dice and gets outcomes [1, 6, 2, 6, 5, 5, 2, 4, 1, 4].
          End scores = (14, 11)
          >>> print(turns[4])
          Start scores = (14, 11).
          Player 0 rolls 2 dice and gets outcomes [6, 6].
          End scores = (26, 11)
          >>> print(turns[5])
          Start scores = (26, 11).
          Player 1 rolls 3 dice and gets outcomes [6, 6, 4].
          End scores = (26, 27)
          >>> print(turns[6])
          Start scores = (26, 27).
          Player 0 rolls 8 dice and gets outcomes [1, 5, 2, 5, 5, 4, 6, 6].
          End scores = (27, 27)
          >>> print(turns[7])
          Start scores = (27, 27).
          Player 1 rolls 10 dice and gets outcomes [6, 2, 6, 3, 3, 1, 5, 1, 2, 2].
          End scores = (27, 28)
          >>> print(turns[8])
          Start scores = (27, 28).
          Player 0 rolls 10 dice and gets outcomes [4, 3, 4, 1, 4, 4, 6, 1, 5, 3].
          End scores = (31, 28)
          >>> print(turns[9])
          Start scores = (31, 28).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (31, 37)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=11863, score0=55, score1=5, goal=56, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (55, 5).
          Player 0 rolls 7 dice and gets outcomes [5, 1, 2, 1, 3, 5, 1].
          End scores = (56, 5)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=59465, score0=61, score1=16, goal=88, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (61, 16).
          Player 0 rolls 4 dice and gets outcomes [2, 2, 3, 4].
          End scores = (72, 16)
          >>> print(turns[1])
          Start scores = (72, 16).
          Player 1 rolls 7 dice and gets outcomes [2, 3, 2, 6, 3, 6, 2].
          End scores = (72, 40)
          >>> print(turns[2])
          Start scores = (72, 40).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (73, 40)
          >>> print(turns[3])
          Start scores = (73, 40).
          Player 1 rolls 6 dice and gets outcomes [5, 1, 3, 2, 2, 2].
          End scores = (73, 41)
          >>> print(turns[4])
          Start scores = (73, 41).
          Player 0 rolls 4 dice and gets outcomes [2, 2, 1, 1].
          End scores = (74, 41)
          >>> print(turns[5])
          Start scores = (74, 41).
          Player 1 rolls 9 dice and gets outcomes [1, 3, 1, 5, 5, 3, 1, 2, 2].
          End scores = (74, 42)
          >>> print(turns[6])
          Start scores = (74, 42).
          Player 0 rolls 9 dice and gets outcomes [6, 3, 4, 4, 4, 5, 4, 4, 2].
          End scores = (110, 42)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=4714, score0=9, score1=3, goal=20, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (9, 3).
          Player 0 rolls 5 dice and gets outcomes [3, 2, 2, 6, 4].
          End scores = (26, 3)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=10742, score0=4, score1=25, goal=57, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (4, 25).
          Player 0 rolls 3 dice and gets outcomes [2, 3, 1].
          End scores = (5, 25)
          >>> print(turns[1])
          Start scores = (5, 25).
          Player 1 rolls 10 dice and gets outcomes [3, 6, 4, 3, 6, 5, 3, 5, 6, 4].
          End scores = (5, 70)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=5480, score0=5, score1=8, goal=77, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (5, 8).
          Player 0 rolls 4 dice and gets outcomes [3, 6, 3, 3].
          End scores = (20, 8)
          >>> print(turns[1])
          Start scores = (20, 8).
          Player 1 rolls 2 dice and gets outcomes [4, 4].
          End scores = (20, 19)
          >>> print(turns[2])
          Start scores = (20, 19).
          Player 0 rolls 8 dice and gets outcomes [6, 1, 4, 2, 5, 4, 4, 4].
          End scores = (21, 19)
          >>> print(turns[3])
          Start scores = (21, 19).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (21, 31)
          >>> print(turns[4])
          Start scores = (21, 31).
          Player 0 rolls 7 dice and gets outcomes [4, 5, 1, 1, 2, 4, 5].
          End scores = (22, 31)
          >>> print(turns[5])
          Start scores = (22, 31).
          Player 1 rolls 9 dice and gets outcomes [5, 4, 5, 4, 1, 1, 2, 1, 3].
          End scores = (22, 32)
          >>> print(turns[6])
          Start scores = (22, 32).
          Player 0 rolls 6 dice and gets outcomes [1, 4, 3, 6, 1, 5].
          End scores = (32, 23)
          >>> print(turns[7])
          Start scores = (32, 23).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (32, 31)
          >>> print(turns[8])
          Start scores = (32, 31).
          Player 0 rolls 3 dice and gets outcomes [2, 4, 4].
          End scores = (42, 31)
          >>> print(turns[9])
          Start scores = (42, 31).
          Player 1 rolls 3 dice and gets outcomes [6, 4, 5].
          End scores = (42, 46)
          >>> print(turns[10])
          Start scores = (42, 46).
          Player 0 rolls 7 dice and gets outcomes [6, 5, 2, 2, 3, 5, 5].
          End scores = (70, 46)
          >>> print(turns[11])
          Start scores = (70, 46).
          Player 1 rolls 2 dice and gets outcomes [2, 3].
          End scores = (70, 51)
          >>> print(turns[12])
          Start scores = (70, 51).
          Player 0 rolls 8 dice and gets outcomes [5, 1, 1, 4, 6, 6, 2, 2].
          End scores = (71, 51)
          >>> print(turns[13])
          Start scores = (71, 51).
          Player 1 rolls 9 dice and gets outcomes [2, 6, 4, 2, 4, 2, 2, 3, 5].
          End scores = (71, 81)
          >>> print(turns[14])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=5014, score0=56, score1=59, goal=64, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (56, 59).
          Player 0 rolls 9 dice and gets outcomes [1, 3, 1, 4, 5, 1, 4, 5, 6].
          End scores = (57, 59)
          >>> print(turns[1])
          Start scores = (57, 59).
          Player 1 rolls 10 dice and gets outcomes [5, 4, 2, 5, 6, 5, 2, 4, 2, 5].
          End scores = (57, 99)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=50496, score0=4, score1=15, goal=19, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (4, 15).
          Player 0 rolls 3 dice and gets outcomes [6, 4, 2].
          End scores = (16, 15)
          >>> print(turns[1])
          Start scores = (16, 15).
          Player 1 rolls 9 dice and gets outcomes [6, 1, 5, 5, 2, 6, 3, 1, 1].
          End scores = (16, 16)
          >>> print(turns[2])
          Start scores = (16, 16).
          Player 0 rolls 6 dice and gets outcomes [4, 5, 1, 1, 6, 4].
          End scores = (17, 16)
          >>> print(turns[3])
          Start scores = (17, 16).
          Player 1 rolls 10 dice and gets outcomes [1, 6, 6, 4, 1, 2, 5, 6, 1, 5].
          End scores = (17, 17)
          >>> print(turns[4])
          Start scores = (17, 17).
          Player 0 rolls 2 dice and gets outcomes [6, 1].
          End scores = (18, 17)
          >>> print(turns[5])
          Start scores = (18, 17).
          Player 1 rolls 2 dice and gets outcomes [5, 5].
          End scores = (18, 27)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=97617, score0=16, score1=27, goal=35, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (16, 27).
          Player 0 rolls 7 dice and gets outcomes [4, 3, 5, 1, 5, 2, 6].
          End scores = (17, 27)
          >>> print(turns[1])
          Start scores = (17, 27).
          Player 1 rolls 10 dice and gets outcomes [2, 2, 2, 5, 4, 2, 1, 1, 2, 5].
          End scores = (17, 28)
          >>> print(turns[2])
          Start scores = (17, 28).
          Player 0 rolls 8 dice and gets outcomes [6, 2, 6, 4, 2, 6, 3, 3].
          End scores = (49, 28)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=19709, score0=27, score1=6, goal=85, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (27, 6).
          Player 0 rolls 8 dice and gets outcomes [4, 4, 4, 1, 3, 6, 2, 4].
          End scores = (28, 6)
          >>> print(turns[1])
          Start scores = (28, 6).
          Player 1 rolls 3 dice and gets outcomes [4, 6, 3].
          End scores = (28, 19)
          >>> print(turns[2])
          Start scores = (28, 19).
          Player 0 rolls 4 dice and gets outcomes [1, 6, 2, 3].
          End scores = (29, 19)
          >>> print(turns[3])
          Start scores = (29, 19).
          Player 1 rolls 4 dice and gets outcomes [4, 2, 4, 5].
          End scores = (29, 34)
          >>> print(turns[4])
          Start scores = (29, 34).
          Player 0 rolls 6 dice and gets outcomes [6, 1, 1, 3, 4, 5].
          End scores = (33, 34)
          >>> print(turns[5])
          Start scores = (33, 34).
          Player 1 rolls 7 dice and gets outcomes [2, 2, 2, 2, 2, 4, 2].
          End scores = (33, 50)
          >>> print(turns[6])
          Start scores = (33, 50).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (43, 50)
          >>> print(turns[7])
          Start scores = (43, 50).
          Player 1 rolls 6 dice and gets outcomes [1, 2, 5, 3, 4, 2].
          End scores = (43, 51)
          >>> print(turns[8])
          Start scores = (43, 51).
          Player 0 rolls 8 dice and gets outcomes [4, 5, 4, 6, 4, 1, 6, 2].
          End scores = (44, 51)
          >>> print(turns[9])
          Start scores = (44, 51).
          Player 1 rolls 8 dice and gets outcomes [5, 2, 5, 1, 6, 1, 1, 4].
          End scores = (44, 55)
          >>> print(turns[10])
          Start scores = (44, 55).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (45, 55)
          >>> print(turns[11])
          Start scores = (45, 55).
          Player 1 rolls 3 dice and gets outcomes [4, 3, 2].
          End scores = (45, 64)
          >>> print(turns[12])
          Start scores = (45, 64).
          Player 0 rolls 5 dice and gets outcomes [6, 2, 3, 6, 4].
          End scores = (66, 64)
          >>> print(turns[13])
          Start scores = (66, 64).
          Player 1 rolls 5 dice and gets outcomes [4, 6, 2, 5, 5].
          End scores = (66, 89)
          >>> print(turns[14])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=33634, score0=48, score1=74, goal=92, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (48, 74).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (51, 74)
          >>> print(turns[1])
          Start scores = (51, 74).
          Player 1 rolls 9 dice and gets outcomes [5, 1, 3, 3, 4, 3, 1, 3, 6].
          End scores = (51, 75)
          >>> print(turns[2])
          Start scores = (51, 75).
          Player 0 rolls 6 dice and gets outcomes [3, 3, 4, 6, 6, 2].
          End scores = (75, 75)
          >>> print(turns[3])
          Start scores = (75, 75).
          Player 1 rolls 7 dice and gets outcomes [2, 2, 6, 4, 1, 1, 5].
          End scores = (75, 76)
          >>> print(turns[4])
          Start scores = (75, 76).
          Player 0 rolls 6 dice and gets outcomes [6, 4, 5, 1, 2, 1].
          End scores = (76, 76)
          >>> print(turns[5])
          Start scores = (76, 76).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (76, 79)
          >>> print(turns[6])
          Start scores = (76, 79).
          Player 0 rolls 8 dice and gets outcomes [1, 6, 1, 6, 4, 4, 6, 3].
          End scores = (77, 79)
          >>> print(turns[7])
          Start scores = (77, 79).
          Player 1 rolls 10 dice and gets outcomes [5, 1, 3, 2, 2, 4, 4, 5, 2, 1].
          End scores = (77, 80)
          >>> print(turns[8])
          Start scores = (77, 80).
          Player 0 rolls 5 dice and gets outcomes [5, 1, 5, 1, 6].
          End scores = (78, 80)
          >>> print(turns[9])
          Start scores = (78, 80).
          Player 1 rolls 10 dice and gets outcomes [2, 4, 3, 5, 3, 2, 5, 4, 2, 5].
          End scores = (78, 115)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=22855, score0=12, score1=22, goal=98, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (12, 22).
          Player 0 rolls 9 dice and gets outcomes [3, 6, 5, 3, 3, 2, 5, 3, 3].
          End scores = (45, 22)
          >>> print(turns[1])
          Start scores = (45, 22).
          Player 1 rolls 8 dice and gets outcomes [5, 2, 6, 4, 6, 2, 3, 1].
          End scores = (45, 23)
          >>> print(turns[2])
          Start scores = (45, 23).
          Player 0 rolls 10 dice and gets outcomes [4, 4, 1, 4, 5, 5, 3, 1, 2, 6].
          End scores = (46, 23)
          >>> print(turns[3])
          Start scores = (46, 23).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (46, 29)
          >>> print(turns[4])
          Start scores = (46, 29).
          Player 0 rolls 3 dice and gets outcomes [6, 2, 3].
          End scores = (57, 29)
          >>> print(turns[5])
          Start scores = (57, 29).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (57, 32)
          >>> print(turns[6])
          Start scores = (57, 32).
          Player 0 rolls 9 dice and gets outcomes [4, 1, 3, 1, 2, 2, 5, 3, 2].
          End scores = (58, 32)
          >>> print(turns[7])
          Start scores = (58, 32).
          Player 1 rolls 6 dice and gets outcomes [4, 5, 4, 6, 6, 3].
          End scores = (58, 60)
          >>> print(turns[8])
          Start scores = (58, 60).
          Player 0 rolls 2 dice and gets outcomes [5, 4].
          End scores = (67, 60)
          >>> print(turns[9])
          Start scores = (67, 60).
          Player 1 rolls 9 dice and gets outcomes [3, 1, 5, 2, 2, 6, 4, 2, 6].
          End scores = (67, 61)
          >>> print(turns[10])
          Start scores = (67, 61).
          Player 0 rolls 5 dice and gets outcomes [5, 6, 4, 3, 1].
          End scores = (68, 61)
          >>> print(turns[11])
          Start scores = (68, 61).
          Player 1 rolls 4 dice and gets outcomes [2, 5, 1, 6].
          End scores = (68, 62)
          >>> print(turns[12])
          Start scores = (68, 62).
          Player 0 rolls 2 dice and gets outcomes [2, 2].
          End scores = (72, 62)
          >>> print(turns[13])
          Start scores = (72, 62).
          Player 1 rolls 8 dice and gets outcomes [4, 3, 5, 3, 5, 4, 3, 3].
          End scores = (72, 92)
          >>> print(turns[14])
          Start scores = (72, 92).
          Player 0 rolls 3 dice and gets outcomes [2, 3, 5].
          End scores = (82, 92)
          >>> print(turns[15])
          Start scores = (82, 92).
          Player 1 rolls 6 dice and gets outcomes [6, 1, 6, 4, 5, 6].
          End scores = (82, 96)
          >>> print(turns[16])
          Start scores = (82, 96).
          Player 0 rolls 4 dice and gets outcomes [4, 1, 2, 6].
          End scores = (83, 96)
          >>> print(turns[17])
          Start scores = (83, 96).
          Player 1 rolls 2 dice and gets outcomes [2, 3].
          End scores = (83, 101)
          >>> print(turns[18])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=49015, score0=12, score1=5, goal=82, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (12, 5).
          Player 0 rolls 10 dice and gets outcomes [1, 3, 2, 1, 5, 1, 4, 1, 1, 6].
          End scores = (13, 5)
          >>> print(turns[1])
          Start scores = (13, 5).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (13, 7)
          >>> print(turns[2])
          Start scores = (13, 7).
          Player 0 rolls 7 dice and gets outcomes [5, 5, 6, 5, 4, 1, 2].
          End scores = (14, 7)
          >>> print(turns[3])
          Start scores = (14, 7).
          Player 1 rolls 10 dice and gets outcomes [2, 4, 2, 4, 2, 5, 3, 5, 6, 6].
          End scores = (14, 46)
          >>> print(turns[4])
          Start scores = (14, 46).
          Player 0 rolls 8 dice and gets outcomes [3, 5, 4, 5, 3, 2, 1, 6].
          End scores = (15, 46)
          >>> print(turns[5])
          Start scores = (15, 46).
          Player 1 rolls 2 dice and gets outcomes [3, 1].
          End scores = (15, 47)
          >>> print(turns[6])
          Start scores = (15, 47).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (21, 47)
          >>> print(turns[7])
          Start scores = (21, 47).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (21, 56)
          >>> print(turns[8])
          Start scores = (21, 56).
          Player 0 rolls 9 dice and gets outcomes [4, 1, 6, 4, 6, 2, 2, 4, 6].
          End scores = (22, 56)
          >>> print(turns[9])
          Start scores = (22, 56).
          Player 1 rolls 4 dice and gets outcomes [3, 4, 6, 2].
          End scores = (22, 71)
          >>> print(turns[10])
          Start scores = (22, 71).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (31, 71)
          >>> print(turns[11])
          Start scores = (31, 71).
          Player 1 rolls 8 dice and gets outcomes [6, 2, 5, 4, 4, 3, 3, 3].
          End scores = (31, 101)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=50497, score0=46, score1=5, goal=51, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (46, 5).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (49, 5)
          >>> print(turns[1])
          Start scores = (49, 5).
          Player 1 rolls 10 dice and gets outcomes [3, 1, 2, 5, 2, 4, 5, 6, 6, 2].
          End scores = (6, 49)
          >>> print(turns[2])
          Start scores = (6, 49).
          Player 0 rolls 4 dice and gets outcomes [3, 3, 3, 4].
          End scores = (19, 49)
          >>> print(turns[3])
          Start scores = (19, 49).
          Player 1 rolls 5 dice and gets outcomes [2, 6, 6, 1, 4].
          End scores = (19, 50)
          >>> print(turns[4])
          Start scores = (19, 50).
          Player 0 rolls 3 dice and gets outcomes [6, 1, 6].
          End scores = (50, 20)
          >>> print(turns[5])
          Start scores = (50, 20).
          Player 1 rolls 2 dice and gets outcomes [3, 6].
          End scores = (50, 29)
          >>> print(turns[6])
          Start scores = (50, 29).
          Player 0 rolls 2 dice and gets outcomes [3, 5].
          End scores = (58, 29)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=42297, score0=6, score1=22, goal=25, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (6, 22).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (12, 22)
          >>> print(turns[1])
          Start scores = (12, 22).
          Player 1 rolls 6 dice and gets outcomes [1, 1, 2, 5, 1, 2].
          End scores = (12, 23)
          >>> print(turns[2])
          Start scores = (12, 23).
          Player 0 rolls 5 dice and gets outcomes [2, 3, 4, 3, 6].
          End scores = (30, 23)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=1726, score0=19, score1=5, goal=52, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (19, 5).
          Player 0 rolls 9 dice and gets outcomes [5, 1, 3, 4, 3, 1, 5, 1, 5].
          End scores = (20, 5)
          >>> print(turns[1])
          Start scores = (20, 5).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (20, 8)
          >>> print(turns[2])
          Start scores = (20, 8).
          Player 0 rolls 4 dice and gets outcomes [2, 2, 3, 3].
          End scores = (30, 8)
          >>> print(turns[3])
          Start scores = (30, 8).
          Player 1 rolls 10 dice and gets outcomes [5, 6, 2, 6, 4, 6, 6, 4, 4, 4].
          End scores = (30, 55)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=17218, score0=19, score1=10, goal=50, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (19, 10).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (22, 10)
          >>> print(turns[1])
          Start scores = (22, 10).
          Player 1 rolls 5 dice and gets outcomes [1, 5, 2, 3, 3].
          End scores = (22, 11)
          >>> print(turns[2])
          Start scores = (22, 11).
          Player 0 rolls 5 dice and gets outcomes [5, 1, 1, 4, 6].
          End scores = (23, 11)
          >>> print(turns[3])
          Start scores = (23, 11).
          Player 1 rolls 7 dice and gets outcomes [3, 2, 6, 2, 2, 5, 3].
          End scores = (23, 34)
          >>> print(turns[4])
          Start scores = (23, 34).
          Player 0 rolls 5 dice and gets outcomes [2, 5, 3, 5, 6].
          End scores = (44, 34)
          >>> print(turns[5])
          Start scores = (44, 34).
          Player 1 rolls 5 dice and gets outcomes [1, 2, 6, 6, 5].
          End scores = (44, 35)
          >>> print(turns[6])
          Start scores = (44, 35).
          Player 0 rolls 2 dice and gets outcomes [3, 4].
          End scores = (51, 35)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=88988, score0=15, score1=95, goal=100, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (15, 95).
          Player 0 rolls 3 dice and gets outcomes [5, 3, 2].
          End scores = (25, 95)
          >>> print(turns[1])
          Start scores = (25, 95).
          Player 1 rolls 5 dice and gets outcomes [4, 2, 1, 3, 2].
          End scores = (25, 96)
          >>> print(turns[2])
          Start scores = (25, 96).
          Player 0 rolls 10 dice and gets outcomes [5, 6, 4, 3, 2, 6, 4, 6, 1, 2].
          End scores = (26, 96)
          >>> print(turns[3])
          Start scores = (26, 96).
          Player 1 rolls 2 dice and gets outcomes [1, 6].
          End scores = (26, 97)
          >>> print(turns[4])
          Start scores = (26, 97).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (29, 97)
          >>> print(turns[5])
          Start scores = (29, 97).
          Player 1 rolls 2 dice and gets outcomes [5, 1].
          End scores = (29, 98)
          >>> print(turns[6])
          Start scores = (29, 98).
          Player 0 rolls 2 dice and gets outcomes [3, 1].
          End scores = (30, 98)
          >>> print(turns[7])
          Start scores = (30, 98).
          Player 1 rolls 9 dice and gets outcomes [5, 6, 2, 4, 2, 2, 3, 6, 1].
          End scores = (30, 99)
          >>> print(turns[8])
          Start scores = (30, 99).
          Player 0 rolls 4 dice and gets outcomes [4, 4, 1, 2].
          End scores = (31, 99)
          >>> print(turns[9])
          Start scores = (31, 99).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (31, 102)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=8964, score0=79, score1=56, goal=83, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (79, 56).
          Player 0 rolls 7 dice and gets outcomes [5, 2, 3, 6, 6, 1, 6].
          End scores = (80, 56)
          >>> print(turns[1])
          Start scores = (80, 56).
          Player 1 rolls 5 dice and gets outcomes [1, 2, 5, 1, 2].
          End scores = (80, 57)
          >>> print(turns[2])
          Start scores = (80, 57).
          Player 0 rolls 3 dice and gets outcomes [5, 6, 3].
          End scores = (94, 57)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=24932, score0=12, score1=0, goal=14, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (12, 0).
          Player 0 rolls 7 dice and gets outcomes [1, 1, 1, 3, 3, 2, 4].
          End scores = (13, 0)
          >>> print(turns[1])
          Start scores = (13, 0).
          Player 1 rolls 9 dice and gets outcomes [1, 5, 4, 3, 3, 5, 1, 5, 3].
          End scores = (13, 1)
          >>> print(turns[2])
          Start scores = (13, 1).
          Player 0 rolls 9 dice and gets outcomes [2, 3, 5, 2, 1, 6, 6, 3, 4].
          End scores = (14, 1)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=76726, score0=40, score1=73, goal=93, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (40, 73).
          Player 0 rolls 2 dice and gets outcomes [6, 6].
          End scores = (52, 73)
          >>> print(turns[1])
          Start scores = (52, 73).
          Player 1 rolls 8 dice and gets outcomes [1, 2, 5, 6, 1, 4, 2, 1].
          End scores = (52, 74)
          >>> print(turns[2])
          Start scores = (52, 74).
          Player 0 rolls 5 dice and gets outcomes [6, 1, 6, 4, 2].
          End scores = (53, 74)
          >>> print(turns[3])
          Start scores = (53, 74).
          Player 1 rolls 8 dice and gets outcomes [5, 4, 1, 6, 2, 5, 5, 3].
          End scores = (53, 75)
          >>> print(turns[4])
          Start scores = (53, 75).
          Player 0 rolls 3 dice and gets outcomes [6, 1, 2].
          End scores = (54, 75)
          >>> print(turns[5])
          Start scores = (54, 75).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (54, 77)
          >>> print(turns[6])
          Start scores = (54, 77).
          Player 0 rolls 4 dice and gets outcomes [5, 2, 4, 5].
          End scores = (70, 77)
          >>> print(turns[7])
          Start scores = (70, 77).
          Player 1 rolls 3 dice and gets outcomes [6, 2, 5].
          End scores = (90, 70)
          >>> print(turns[8])
          Start scores = (90, 70).
          Player 0 rolls 5 dice and gets outcomes [4, 2, 3, 3, 6].
          End scores = (108, 70)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=85393, score0=3, score1=0, goal=44, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 0).
          Player 0 rolls 5 dice and gets outcomes [3, 2, 5, 1, 6].
          End scores = (4, 0)
          >>> print(turns[1])
          Start scores = (4, 0).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (4, 3)
          >>> print(turns[2])
          Start scores = (4, 3).
          Player 0 rolls 8 dice and gets outcomes [2, 6, 5, 3, 4, 2, 4, 6].
          End scores = (36, 3)
          >>> print(turns[3])
          Start scores = (36, 3).
          Player 1 rolls 3 dice and gets outcomes [3, 2, 1].
          End scores = (36, 7)
          >>> print(turns[4])
          Start scores = (36, 7).
          Player 0 rolls 9 dice and gets outcomes [1, 2, 3, 4, 3, 2, 5, 1, 6].
          End scores = (37, 7)
          >>> print(turns[5])
          Start scores = (37, 7).
          Player 1 rolls 10 dice and gets outcomes [1, 1, 1, 1, 6, 4, 4, 3, 4, 4].
          End scores = (37, 8)
          >>> print(turns[6])
          Start scores = (37, 8).
          Player 0 rolls 3 dice and gets outcomes [1, 6, 2].
          End scores = (38, 8)
          >>> print(turns[7])
          Start scores = (38, 8).
          Player 1 rolls 9 dice and gets outcomes [3, 5, 1, 1, 4, 6, 1, 3, 4].
          End scores = (38, 9)
          >>> print(turns[8])
          Start scores = (38, 9).
          Player 0 rolls 9 dice and gets outcomes [6, 5, 3, 1, 1, 2, 6, 3, 2].
          End scores = (39, 9)
          >>> print(turns[9])
          Start scores = (39, 9).
          Player 1 rolls 6 dice and gets outcomes [4, 1, 5, 4, 2, 1].
          End scores = (39, 10)
          >>> print(turns[10])
          Start scores = (39, 10).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (10, 40)
          >>> print(turns[11])
          Start scores = (10, 40).
          Player 1 rolls 3 dice and gets outcomes [1, 4, 6].
          End scores = (10, 41)
          >>> print(turns[12])
          Start scores = (10, 41).
          Player 0 rolls 8 dice and gets outcomes [2, 5, 6, 4, 6, 2, 6, 6].
          End scores = (47, 41)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=35702, score0=10, score1=13, goal=14, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (10, 13).
          Player 0 rolls 6 dice and gets outcomes [5, 4, 6, 2, 3, 5].
          End scores = (35, 13)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=75713, score0=62, score1=6, goal=63, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (62, 6).
          Player 0 rolls 3 dice and gets outcomes [1, 6, 2].
          End scores = (63, 6)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=14879, score0=24, score1=8, goal=29, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (24, 8).
          Player 0 rolls 10 dice and gets outcomes [1, 1, 6, 6, 2, 6, 5, 1, 4, 6].
          End scores = (25, 8)
          >>> print(turns[1])
          Start scores = (25, 8).
          Player 1 rolls 8 dice and gets outcomes [3, 4, 6, 3, 3, 2, 3, 6].
          End scores = (25, 38)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=62742, score0=9, score1=5, goal=11, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (9, 5).
          Player 0 rolls 7 dice and gets outcomes [3, 2, 4, 1, 3, 5, 1].
          End scores = (10, 5)
          >>> print(turns[1])
          Start scores = (10, 5).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (10, 15)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=99168, score0=34, score1=40, goal=95, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (34, 40).
          Player 0 rolls 2 dice and gets outcomes [1, 5].
          End scores = (38, 40)
          >>> print(turns[1])
          Start scores = (38, 40).
          Player 1 rolls 9 dice and gets outcomes [2, 5, 1, 5, 5, 2, 6, 4, 4].
          End scores = (38, 41)
          >>> print(turns[2])
          Start scores = (38, 41).
          Player 0 rolls 10 dice and gets outcomes [3, 1, 4, 1, 5, 4, 4, 6, 1, 3].
          End scores = (39, 41)
          >>> print(turns[3])
          Start scores = (39, 41).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (39, 48)
          >>> print(turns[4])
          Start scores = (39, 48).
          Player 0 rolls 4 dice and gets outcomes [5, 5, 2, 1].
          End scores = (40, 48)
          >>> print(turns[5])
          Start scores = (40, 48).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (40, 53)
          >>> print(turns[6])
          Start scores = (40, 53).
          Player 0 rolls 9 dice and gets outcomes [1, 2, 2, 4, 5, 2, 1, 5, 2].
          End scores = (41, 53)
          >>> print(turns[7])
          Start scores = (41, 53).
          Player 1 rolls 10 dice and gets outcomes [6, 1, 6, 1, 1, 5, 1, 1, 5, 3].
          End scores = (41, 54)
          >>> print(turns[8])
          Start scores = (41, 54).
          Player 0 rolls 3 dice and gets outcomes [6, 3, 6].
          End scores = (56, 54)
          >>> print(turns[9])
          Start scores = (56, 54).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (56, 55)
          >>> print(turns[10])
          Start scores = (56, 55).
          Player 0 rolls 6 dice and gets outcomes [3, 2, 2, 3, 2, 4].
          End scores = (72, 55)
          >>> print(turns[11])
          Start scores = (72, 55).
          Player 1 rolls 3 dice and gets outcomes [6, 2, 4].
          End scores = (72, 70)
          >>> print(turns[12])
          Start scores = (72, 70).
          Player 0 rolls 9 dice and gets outcomes [1, 3, 2, 3, 3, 3, 5, 2, 3].
          End scores = (73, 70)
          >>> print(turns[13])
          Start scores = (73, 70).
          Player 1 rolls 3 dice and gets outcomes [1, 3, 1].
          End scores = (73, 71)
          >>> print(turns[14])
          Start scores = (73, 71).
          Player 0 rolls 9 dice and gets outcomes [1, 1, 6, 5, 3, 2, 1, 1, 1].
          End scores = (74, 71)
          >>> print(turns[15])
          Start scores = (74, 71).
          Player 1 rolls 2 dice and gets outcomes [2, 4].
          End scores = (74, 77)
          >>> print(turns[16])
          Start scores = (74, 77).
          Player 0 rolls 2 dice and gets outcomes [1, 5].
          End scores = (75, 77)
          >>> print(turns[17])
          Start scores = (75, 77).
          Player 1 rolls 10 dice and gets outcomes [1, 6, 1, 5, 6, 5, 2, 2, 4, 3].
          End scores = (75, 78)
          >>> print(turns[18])
          Start scores = (75, 78).
          Player 0 rolls 8 dice and gets outcomes [6, 5, 1, 5, 6, 5, 1, 2].
          End scores = (76, 78)
          >>> print(turns[19])
          Start scores = (76, 78).
          Player 1 rolls 3 dice and gets outcomes [5, 2, 3].
          End scores = (76, 88)
          >>> print(turns[20])
          Start scores = (76, 88).
          Player 0 rolls 7 dice and gets outcomes [6, 4, 4, 5, 3, 5, 2].
          End scores = (105, 88)
          >>> print(turns[21])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=98804, score0=37, score1=45, goal=47, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (37, 45).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (38, 45)
          >>> print(turns[1])
          Start scores = (38, 45).
          Player 1 rolls 2 dice and gets outcomes [3, 3].
          End scores = (38, 51)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=27518, score0=87, score1=16, goal=92, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (87, 16).
          Player 0 rolls 6 dice and gets outcomes [6, 1, 6, 6, 1, 5].
          End scores = (88, 16)
          >>> print(turns[1])
          Start scores = (88, 16).
          Player 1 rolls 7 dice and gets outcomes [2, 6, 1, 6, 5, 4, 2].
          End scores = (88, 17)
          >>> print(turns[2])
          Start scores = (88, 17).
          Player 0 rolls 7 dice and gets outcomes [4, 5, 5, 4, 2, 1, 1].
          End scores = (89, 17)
          >>> print(turns[3])
          Start scores = (89, 17).
          Player 1 rolls 3 dice and gets outcomes [1, 6, 2].
          End scores = (89, 18)
          >>> print(turns[4])
          Start scores = (89, 18).
          Player 0 rolls 3 dice and gets outcomes [2, 2, 2].
          End scores = (95, 18)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=75062, score0=43, score1=5, goal=97, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (43, 5).
          Player 0 rolls 6 dice and gets outcomes [6, 1, 4, 5, 6, 6].
          End scores = (44, 5)
          >>> print(turns[1])
          Start scores = (44, 5).
          Player 1 rolls 9 dice and gets outcomes [5, 3, 5, 5, 2, 4, 6, 2, 1].
          End scores = (44, 6)
          >>> print(turns[2])
          Start scores = (44, 6).
          Player 0 rolls 2 dice and gets outcomes [1, 5].
          End scores = (45, 6)
          >>> print(turns[3])
          Start scores = (45, 6).
          Player 1 rolls 6 dice and gets outcomes [3, 3, 4, 5, 5, 4].
          End scores = (45, 30)
          >>> print(turns[4])
          Start scores = (45, 30).
          Player 0 rolls 6 dice and gets outcomes [6, 1, 6, 6, 6, 5].
          End scores = (46, 30)
          >>> print(turns[5])
          Start scores = (46, 30).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (46, 36)
          >>> print(turns[6])
          Start scores = (46, 36).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (49, 36)
          >>> print(turns[7])
          Start scores = (49, 36).
          Player 1 rolls 8 dice and gets outcomes [2, 5, 2, 5, 3, 2, 6, 1].
          End scores = (49, 37)
          >>> print(turns[8])
          Start scores = (49, 37).
          Player 0 rolls 7 dice and gets outcomes [1, 5, 1, 4, 6, 5, 5].
          End scores = (50, 37)
          >>> print(turns[9])
          Start scores = (50, 37).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (50, 38)
          >>> print(turns[10])
          Start scores = (50, 38).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (57, 38)
          >>> print(turns[11])
          Start scores = (57, 38).
          Player 1 rolls 7 dice and gets outcomes [1, 4, 1, 2, 5, 6, 6].
          End scores = (57, 39)
          >>> print(turns[12])
          Start scores = (57, 39).
          Player 0 rolls 9 dice and gets outcomes [3, 6, 2, 2, 5, 1, 4, 5, 4].
          End scores = (58, 39)
          >>> print(turns[13])
          Start scores = (58, 39).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (58, 44)
          >>> print(turns[14])
          Start scores = (58, 44).
          Player 0 rolls 5 dice and gets outcomes [5, 5, 2, 1, 6].
          End scores = (59, 44)
          >>> print(turns[15])
          Start scores = (59, 44).
          Player 1 rolls 10 dice and gets outcomes [5, 1, 4, 2, 4, 5, 6, 2, 2, 5].
          End scores = (59, 45)
          >>> print(turns[16])
          Start scores = (59, 45).
          Player 0 rolls 3 dice and gets outcomes [3, 6, 5].
          End scores = (73, 45)
          >>> print(turns[17])
          Start scores = (73, 45).
          Player 1 rolls 5 dice and gets outcomes [1, 3, 1, 3, 2].
          End scores = (73, 46)
          >>> print(turns[18])
          Start scores = (73, 46).
          Player 0 rolls 10 dice and gets outcomes [3, 6, 1, 6, 3, 1, 2, 3, 1, 1].
          End scores = (74, 46)
          >>> print(turns[19])
          Start scores = (74, 46).
          Player 1 rolls 4 dice and gets outcomes [5, 2, 3, 5].
          End scores = (74, 61)
          >>> print(turns[20])
          Start scores = (74, 61).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (83, 61)
          >>> print(turns[21])
          Start scores = (83, 61).
          Player 1 rolls 8 dice and gets outcomes [5, 5, 2, 3, 4, 4, 3, 3].
          End scores = (83, 90)
          >>> print(turns[22])
          Start scores = (83, 90).
          Player 0 rolls 5 dice and gets outcomes [4, 5, 3, 1, 3].
          End scores = (84, 90)
          >>> print(turns[23])
          Start scores = (84, 90).
          Player 1 rolls 7 dice and gets outcomes [5, 5, 2, 5, 5, 4, 6].
          End scores = (84, 122)
          >>> print(turns[24])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=578, score0=7, score1=24, goal=30, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (7, 24).
          Player 0 rolls 3 dice and gets outcomes [1, 1, 3].
          End scores = (8, 24)
          >>> print(turns[1])
          Start scores = (8, 24).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (8, 34)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=93942, score0=42, score1=41, goal=43, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (42, 41).
          Player 0 rolls 5 dice and gets outcomes [3, 6, 3, 3, 2].
          End scores = (59, 41)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=48161, score0=15, score1=55, goal=83, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (15, 55).
          Player 0 rolls 8 dice and gets outcomes [1, 4, 5, 6, 3, 6, 5, 4].
          End scores = (16, 55)
          >>> print(turns[1])
          Start scores = (16, 55).
          Player 1 rolls 9 dice and gets outcomes [2, 5, 3, 1, 3, 4, 3, 1, 6].
          End scores = (16, 56)
          >>> print(turns[2])
          Start scores = (16, 56).
          Player 0 rolls 5 dice and gets outcomes [6, 1, 3, 2, 2].
          End scores = (17, 56)
          >>> print(turns[3])
          Start scores = (17, 56).
          Player 1 rolls 7 dice and gets outcomes [5, 3, 6, 1, 3, 1, 2].
          End scores = (17, 57)
          >>> print(turns[4])
          Start scores = (17, 57).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (22, 57)
          >>> print(turns[5])
          Start scores = (22, 57).
          Player 1 rolls 4 dice and gets outcomes [5, 4, 5, 4].
          End scores = (22, 75)
          >>> print(turns[6])
          Start scores = (22, 75).
          Player 0 rolls 9 dice and gets outcomes [5, 4, 4, 2, 1, 3, 3, 3, 3].
          End scores = (23, 75)
          >>> print(turns[7])
          Start scores = (23, 75).
          Player 1 rolls 6 dice and gets outcomes [6, 3, 2, 2, 6, 4].
          End scores = (23, 98)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=52136, score0=2, score1=14, goal=15, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (2, 14).
          Player 0 rolls 10 dice and gets outcomes [3, 3, 1, 5, 1, 5, 2, 4, 6, 6].
          End scores = (3, 14)
          >>> print(turns[1])
          Start scores = (3, 14).
          Player 1 rolls 9 dice and gets outcomes [1, 6, 5, 4, 4, 3, 4, 6, 6].
          End scores = (3, 15)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=30971, score0=11, score1=12, goal=25, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (11, 12).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (20, 12)
          >>> print(turns[1])
          Start scores = (20, 12).
          Player 1 rolls 3 dice and gets outcomes [2, 2, 1].
          End scores = (20, 13)
          >>> print(turns[2])
          Start scores = (20, 13).
          Player 0 rolls 6 dice and gets outcomes [2, 6, 5, 4, 6, 3].
          End scores = (46, 13)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=69948, score0=11, score1=19, goal=43, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (11, 19).
          Player 0 rolls 10 dice and gets outcomes [1, 5, 6, 6, 2, 6, 1, 6, 4, 2].
          End scores = (12, 19)
          >>> print(turns[1])
          Start scores = (12, 19).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (12, 28)
          >>> print(turns[2])
          Start scores = (12, 28).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 6, 1, 3, 1, 6].
          End scores = (13, 28)
          >>> print(turns[3])
          Start scores = (13, 28).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (13, 32)
          >>> print(turns[4])
          Start scores = (13, 32).
          Player 0 rolls 6 dice and gets outcomes [5, 6, 6, 5, 6, 2].
          End scores = (43, 32)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=33856, score0=9, score1=9, goal=19, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (9, 9).
          Player 0 rolls 2 dice and gets outcomes [3, 5].
          End scores = (17, 9)
          >>> print(turns[1])
          Start scores = (17, 9).
          Player 1 rolls 5 dice and gets outcomes [5, 6, 5, 1, 5].
          End scores = (17, 10)
          >>> print(turns[2])
          Start scores = (17, 10).
          Player 0 rolls 10 dice and gets outcomes [5, 2, 4, 6, 2, 5, 6, 1, 4, 4].
          End scores = (18, 10)
          >>> print(turns[3])
          Start scores = (18, 10).
          Player 1 rolls 3 dice and gets outcomes [1, 1, 2].
          End scores = (18, 11)
          >>> print(turns[4])
          Start scores = (18, 11).
          Player 0 rolls 4 dice and gets outcomes [4, 2, 6, 6].
          End scores = (36, 11)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=93176, score0=7, score1=37, goal=80, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (7, 37).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (13, 37)
          >>> print(turns[1])
          Start scores = (13, 37).
          Player 1 rolls 3 dice and gets outcomes [6, 6, 6].
          End scores = (13, 55)
          >>> print(turns[2])
          Start scores = (13, 55).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (18, 55)
          >>> print(turns[3])
          Start scores = (18, 55).
          Player 1 rolls 4 dice and gets outcomes [3, 6, 4, 6].
          End scores = (18, 74)
          >>> print(turns[4])
          Start scores = (18, 74).
          Player 0 rolls 7 dice and gets outcomes [4, 1, 3, 2, 6, 4, 6].
          End scores = (19, 74)
          >>> print(turns[5])
          Start scores = (19, 74).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (19, 83)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=85986, score0=35, score1=12, goal=74, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (35, 12).
          Player 0 rolls 7 dice and gets outcomes [6, 2, 3, 4, 3, 3, 6].
          End scores = (62, 12)
          >>> print(turns[1])
          Start scores = (62, 12).
          Player 1 rolls 6 dice and gets outcomes [5, 1, 2, 5, 3, 6].
          End scores = (62, 13)
          >>> print(turns[2])
          Start scores = (62, 13).
          Player 0 rolls 5 dice and gets outcomes [1, 2, 3, 3, 6].
          End scores = (63, 13)
          >>> print(turns[3])
          Start scores = (63, 13).
          Player 1 rolls 8 dice and gets outcomes [4, 2, 5, 1, 6, 3, 6, 4].
          End scores = (63, 14)
          >>> print(turns[4])
          Start scores = (63, 14).
          Player 0 rolls 5 dice and gets outcomes [3, 3, 5, 2, 2].
          End scores = (78, 14)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=76820, score0=28, score1=14, goal=61, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (28, 14).
          Player 0 rolls 7 dice and gets outcomes [2, 6, 4, 1, 1, 1, 1].
          End scores = (29, 14)
          >>> print(turns[1])
          Start scores = (29, 14).
          Player 1 rolls 5 dice and gets outcomes [3, 3, 6, 6, 6].
          End scores = (29, 38)
          >>> print(turns[2])
          Start scores = (29, 38).
          Player 0 rolls 8 dice and gets outcomes [4, 2, 5, 4, 1, 5, 5, 3].
          End scores = (30, 38)
          >>> print(turns[3])
          Start scores = (30, 38).
          Player 1 rolls 10 dice and gets outcomes [6, 5, 4, 4, 5, 3, 5, 6, 5, 4].
          End scores = (30, 85)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=83984, score0=64, score1=49, goal=78, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (64, 49).
          Player 0 rolls 2 dice and gets outcomes [3, 5].
          End scores = (75, 49)
          >>> print(turns[1])
          Start scores = (75, 49).
          Player 1 rolls 10 dice and gets outcomes [3, 5, 6, 3, 4, 3, 1, 4, 3, 6].
          End scores = (75, 50)
          >>> print(turns[2])
          Start scores = (75, 50).
          Player 0 rolls 3 dice and gets outcomes [3, 5, 3].
          End scores = (86, 50)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25773, score0=3, score1=17, goal=30, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 17).
          Player 0 rolls 8 dice and gets outcomes [3, 4, 5, 4, 6, 2, 1, 4].
          End scores = (4, 17)
          >>> print(turns[1])
          Start scores = (4, 17).
          Player 1 rolls 7 dice and gets outcomes [5, 1, 5, 3, 1, 4, 3].
          End scores = (4, 18)
          >>> print(turns[2])
          Start scores = (4, 18).
          Player 0 rolls 5 dice and gets outcomes [2, 1, 5, 6, 2].
          End scores = (5, 18)
          >>> print(turns[3])
          Start scores = (5, 18).
          Player 1 rolls 3 dice and gets outcomes [6, 5, 6].
          End scores = (5, 35)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=6012, score0=30, score1=3, goal=85, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (30, 3).
          Player 0 rolls 5 dice and gets outcomes [1, 4, 6, 2, 4].
          End scores = (31, 3)
          >>> print(turns[1])
          Start scores = (31, 3).
          Player 1 rolls 6 dice and gets outcomes [2, 4, 2, 4, 3, 3].
          End scores = (31, 21)
          >>> print(turns[2])
          Start scores = (31, 21).
          Player 0 rolls 2 dice and gets outcomes [4, 6].
          End scores = (41, 21)
          >>> print(turns[3])
          Start scores = (41, 21).
          Player 1 rolls 4 dice and gets outcomes [4, 4, 6, 6].
          End scores = (41, 41)
          >>> print(turns[4])
          Start scores = (41, 41).
          Player 0 rolls 3 dice and gets outcomes [6, 5, 5].
          End scores = (57, 41)
          >>> print(turns[5])
          Start scores = (57, 41).
          Player 1 rolls 3 dice and gets outcomes [1, 1, 4].
          End scores = (57, 42)
          >>> print(turns[6])
          Start scores = (57, 42).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (65, 42)
          >>> print(turns[7])
          Start scores = (65, 42).
          Player 1 rolls 9 dice and gets outcomes [2, 4, 5, 3, 3, 4, 1, 1, 5].
          End scores = (65, 43)
          >>> print(turns[8])
          Start scores = (65, 43).
          Player 0 rolls 10 dice and gets outcomes [6, 1, 1, 6, 1, 6, 1, 6, 1, 1].
          End scores = (66, 43)
          >>> print(turns[9])
          Start scores = (66, 43).
          Player 1 rolls 5 dice and gets outcomes [3, 2, 2, 6, 3].
          End scores = (66, 59)
          >>> print(turns[10])
          Start scores = (66, 59).
          Player 0 rolls 3 dice and gets outcomes [6, 5, 1].
          End scores = (67, 59)
          >>> print(turns[11])
          Start scores = (67, 59).
          Player 1 rolls 6 dice and gets outcomes [4, 4, 1, 4, 6, 4].
          End scores = (67, 60)
          >>> print(turns[12])
          Start scores = (67, 60).
          Player 0 rolls 6 dice and gets outcomes [4, 2, 3, 2, 3, 6].
          End scores = (87, 60)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=56692, score0=69, score1=40, goal=71, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (69, 40).
          Player 0 rolls 3 dice and gets outcomes [6, 4, 6].
          End scores = (85, 40)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=11528, score0=6, score1=7, goal=17, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (6, 7).
          Player 0 rolls 10 dice and gets outcomes [2, 6, 2, 6, 3, 1, 5, 2, 6, 5].
          End scores = (7, 7)
          >>> print(turns[1])
          Start scores = (7, 7).
          Player 1 rolls 9 dice and gets outcomes [5, 5, 2, 2, 1, 6, 4, 6, 4].
          End scores = (7, 8)
          >>> print(turns[2])
          Start scores = (7, 8).
          Player 0 rolls 4 dice and gets outcomes [1, 2, 6, 6].
          End scores = (8, 8)
          >>> print(turns[3])
          Start scores = (8, 8).
          Player 1 rolls 6 dice and gets outcomes [1, 3, 1, 5, 5, 2].
          End scores = (8, 9)
          >>> print(turns[4])
          Start scores = (8, 9).
          Player 0 rolls 4 dice and gets outcomes [2, 4, 4, 4].
          End scores = (22, 9)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=95684, score0=3, score1=1, goal=10, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 1).
          Player 0 rolls 6 dice and gets outcomes [3, 4, 1, 3, 5, 1].
          End scores = (4, 1)
          >>> print(turns[1])
          Start scores = (4, 1).
          Player 1 rolls 4 dice and gets outcomes [6, 2, 6, 1].
          End scores = (4, 2)
          >>> print(turns[2])
          Start scores = (4, 2).
          Player 0 rolls 3 dice and gets outcomes [4, 5, 5].
          End scores = (18, 2)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=81397, score0=45, score1=40, goal=52, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (45, 40).
          Player 0 rolls 10 dice and gets outcomes [6, 5, 3, 1, 1, 2, 4, 1, 3, 1].
          End scores = (46, 40)
          >>> print(turns[1])
          Start scores = (46, 40).
          Player 1 rolls 9 dice and gets outcomes [4, 5, 6, 4, 2, 1, 5, 3, 3].
          End scores = (46, 41)
          >>> print(turns[2])
          Start scores = (46, 41).
          Player 0 rolls 7 dice and gets outcomes [2, 2, 5, 3, 4, 2, 3].
          End scores = (67, 41)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=22637, score0=32, score1=11, goal=58, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (32, 11).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (41, 11)
          >>> print(turns[1])
          Start scores = (41, 11).
          Player 1 rolls 6 dice and gets outcomes [6, 6, 5, 5, 5, 1].
          End scores = (41, 12)
          >>> print(turns[2])
          Start scores = (41, 12).
          Player 0 rolls 2 dice and gets outcomes [4, 6].
          End scores = (54, 12)
          >>> print(turns[3])
          Start scores = (54, 12).
          Player 1 rolls 3 dice and gets outcomes [6, 6, 1].
          End scores = (54, 13)
          >>> print(turns[4])
          Start scores = (54, 13).
          Player 0 rolls 6 dice and gets outcomes [5, 5, 6, 4, 1, 5].
          End scores = (55, 13)
          >>> print(turns[5])
          Start scores = (55, 13).
          Player 1 rolls 6 dice and gets outcomes [6, 6, 1, 4, 6, 6].
          End scores = (55, 14)
          >>> print(turns[6])
          Start scores = (55, 14).
          Player 0 rolls 3 dice and gets outcomes [1, 3, 3].
          End scores = (56, 14)
          >>> print(turns[7])
          Start scores = (56, 14).
          Player 1 rolls 4 dice and gets outcomes [6, 4, 2, 5].
          End scores = (56, 34)
          >>> print(turns[8])
          Start scores = (56, 34).
          Player 0 rolls 6 dice and gets outcomes [5, 2, 3, 2, 3, 6].
          End scores = (77, 34)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=11998, score0=16, score1=21, goal=67, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (16, 21).
          Player 0 rolls 6 dice and gets outcomes [4, 2, 3, 5, 6, 3].
          End scores = (39, 21)
          >>> print(turns[1])
          Start scores = (39, 21).
          Player 1 rolls 3 dice and gets outcomes [3, 6, 2].
          End scores = (39, 32)
          >>> print(turns[2])
          Start scores = (39, 32).
          Player 0 rolls 9 dice and gets outcomes [1, 6, 4, 5, 3, 4, 6, 2, 3].
          End scores = (40, 32)
          >>> print(turns[3])
          Start scores = (40, 32).
          Player 1 rolls 9 dice and gets outcomes [4, 2, 3, 4, 3, 6, 2, 5, 6].
          End scores = (40, 67)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=69783, score0=11, score1=13, goal=38, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (11, 13).
          Player 0 rolls 3 dice and gets outcomes [4, 6, 6].
          End scores = (27, 13)
          >>> print(turns[1])
          Start scores = (27, 13).
          Player 1 rolls 6 dice and gets outcomes [4, 4, 5, 6, 4, 3].
          End scores = (27, 39)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=37364, score0=29, score1=22, goal=35, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (29, 22).
          Player 0 rolls 8 dice and gets outcomes [1, 6, 1, 6, 5, 6, 6, 3].
          End scores = (30, 22)
          >>> print(turns[1])
          Start scores = (30, 22).
          Player 1 rolls 2 dice and gets outcomes [5, 2].
          End scores = (30, 32)
          >>> print(turns[2])
          Start scores = (30, 32).
          Player 0 rolls 10 dice and gets outcomes [4, 4, 5, 6, 4, 4, 1, 4, 2, 5].
          End scores = (34, 32)
          >>> print(turns[3])
          Start scores = (34, 32).
          Player 1 rolls 5 dice and gets outcomes [4, 4, 1, 1, 6].
          End scores = (34, 33)
          >>> print(turns[4])
          Start scores = (34, 33).
          Player 0 rolls 6 dice and gets outcomes [4, 3, 3, 6, 1, 1].
          End scores = (35, 33)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=5143, score0=2, score1=15, goal=79, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (2, 15).
          Player 0 rolls 6 dice and gets outcomes [4, 6, 6, 6, 4, 4].
          End scores = (32, 15)
          >>> print(turns[1])
          Start scores = (32, 15).
          Player 1 rolls 7 dice and gets outcomes [3, 3, 2, 3, 4, 6, 2].
          End scores = (32, 38)
          >>> print(turns[2])
          Start scores = (32, 38).
          Player 0 rolls 3 dice and gets outcomes [2, 2, 4].
          End scores = (40, 38)
          >>> print(turns[3])
          Start scores = (40, 38).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (40, 41)
          >>> print(turns[4])
          Start scores = (40, 41).
          Player 0 rolls 10 dice and gets outcomes [3, 3, 6, 1, 4, 5, 1, 5, 5, 3].
          End scores = (41, 41)
          >>> print(turns[5])
          Start scores = (41, 41).
          Player 1 rolls 6 dice and gets outcomes [2, 1, 2, 6, 2, 1].
          End scores = (41, 42)
          >>> print(turns[6])
          Start scores = (41, 42).
          Player 0 rolls 6 dice and gets outcomes [5, 2, 5, 3, 3, 2].
          End scores = (61, 42)
          >>> print(turns[7])
          Start scores = (61, 42).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (61, 46)
          >>> print(turns[8])
          Start scores = (61, 46).
          Player 0 rolls 2 dice and gets outcomes [4, 4].
          End scores = (69, 46)
          >>> print(turns[9])
          Start scores = (69, 46).
          Player 1 rolls 9 dice and gets outcomes [2, 4, 6, 2, 5, 6, 4, 1, 5].
          End scores = (69, 47)
          >>> print(turns[10])
          Start scores = (69, 47).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (71, 47)
          >>> print(turns[11])
          Start scores = (71, 47).
          Player 1 rolls 10 dice and gets outcomes [2, 4, 2, 3, 2, 2, 6, 4, 5, 6].
          End scores = (71, 83)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=82888, score0=26, score1=39, goal=87, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (26, 39).
          Player 0 rolls 4 dice and gets outcomes [4, 4, 3, 4].
          End scores = (41, 39)
          >>> print(turns[1])
          Start scores = (41, 39).
          Player 1 rolls 7 dice and gets outcomes [3, 6, 5, 2, 6, 6, 6].
          End scores = (41, 73)
          >>> print(turns[2])
          Start scores = (41, 73).
          Player 0 rolls 5 dice and gets outcomes [3, 1, 2, 4, 4].
          End scores = (42, 73)
          >>> print(turns[3])
          Start scores = (42, 73).
          Player 1 rolls 9 dice and gets outcomes [5, 5, 4, 4, 2, 2, 5, 3, 3].
          End scores = (42, 109)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25835, score0=15, score1=64, goal=95, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (15, 64).
          Player 0 rolls 2 dice and gets outcomes [3, 2].
          End scores = (20, 64)
          >>> print(turns[1])
          Start scores = (20, 64).
          Player 1 rolls 8 dice and gets outcomes [3, 4, 3, 1, 2, 1, 3, 1].
          End scores = (20, 65)
          >>> print(turns[2])
          Start scores = (20, 65).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (25, 65)
          >>> print(turns[3])
          Start scores = (25, 65).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (25, 71)
          >>> print(turns[4])
          Start scores = (25, 71).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (34, 71)
          >>> print(turns[5])
          Start scores = (34, 71).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (34, 77)
          >>> print(turns[6])
          Start scores = (34, 77).
          Player 0 rolls 2 dice and gets outcomes [4, 4].
          End scores = (42, 77)
          >>> print(turns[7])
          Start scores = (42, 77).
          Player 1 rolls 8 dice and gets outcomes [2, 3, 4, 2, 5, 3, 1, 6].
          End scores = (42, 78)
          >>> print(turns[8])
          Start scores = (42, 78).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (45, 78)
          >>> print(turns[9])
          Start scores = (45, 78).
          Player 1 rolls 8 dice and gets outcomes [6, 4, 5, 5, 4, 2, 2, 1].
          End scores = (45, 79)
          >>> print(turns[10])
          Start scores = (45, 79).
          Player 0 rolls 10 dice and gets outcomes [3, 5, 2, 1, 6, 3, 5, 2, 2, 4].
          End scores = (46, 79)
          >>> print(turns[11])
          Start scores = (46, 79).
          Player 1 rolls 9 dice and gets outcomes [1, 3, 5, 3, 4, 5, 5, 2, 6].
          End scores = (46, 80)
          >>> print(turns[12])
          Start scores = (46, 80).
          Player 0 rolls 4 dice and gets outcomes [3, 5, 2, 2].
          End scores = (58, 80)
          >>> print(turns[13])
          Start scores = (58, 80).
          Player 1 rolls 3 dice and gets outcomes [5, 1, 3].
          End scores = (58, 81)
          >>> print(turns[14])
          Start scores = (58, 81).
          Player 0 rolls 7 dice and gets outcomes [1, 3, 3, 3, 3, 3, 4].
          End scores = (59, 81)
          >>> print(turns[15])
          Start scores = (59, 81).
          Player 1 rolls 8 dice and gets outcomes [5, 4, 3, 6, 3, 6, 6, 5].
          End scores = (59, 119)
          >>> print(turns[16])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=85071, score0=86, score1=5, goal=89, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (86, 5).
          Player 0 rolls 7 dice and gets outcomes [1, 3, 2, 6, 4, 5, 6].
          End scores = (87, 5)
          >>> print(turns[1])
          Start scores = (87, 5).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (87, 11)
          >>> print(turns[2])
          Start scores = (87, 11).
          Player 0 rolls 9 dice and gets outcomes [6, 1, 3, 5, 6, 6, 5, 5, 3].
          End scores = (88, 11)
          >>> print(turns[3])
          Start scores = (88, 11).
          Player 1 rolls 8 dice and gets outcomes [4, 4, 2, 5, 5, 4, 6, 4].
          End scores = (88, 45)
          >>> print(turns[4])
          Start scores = (88, 45).
          Player 0 rolls 8 dice and gets outcomes [5, 2, 4, 5, 2, 3, 4, 4].
          End scores = (117, 45)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=23577, score0=32, score1=23, goal=45, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (32, 23).
          Player 0 rolls 10 dice and gets outcomes [1, 4, 6, 5, 3, 6, 4, 2, 1, 3].
          End scores = (33, 23)
          >>> print(turns[1])
          Start scores = (33, 23).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (33, 30)
          >>> print(turns[2])
          Start scores = (33, 30).
          Player 0 rolls 8 dice and gets outcomes [5, 3, 6, 6, 5, 1, 4, 4].
          End scores = (34, 30)
          >>> print(turns[3])
          Start scores = (34, 30).
          Player 1 rolls 5 dice and gets outcomes [5, 2, 6, 4, 2].
          End scores = (34, 49)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=663, score0=44, score1=13, goal=59, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (44, 13).
          Player 0 rolls 8 dice and gets outcomes [5, 6, 6, 4, 5, 3, 5, 5].
          End scores = (83, 13)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=6543, score0=65, score1=70, goal=87, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (65, 70).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (75, 70)
          >>> print(turns[1])
          Start scores = (75, 70).
          Player 1 rolls 7 dice and gets outcomes [5, 3, 3, 3, 2, 3, 6].
          End scores = (75, 95)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=31919, score0=2, score1=16, goal=28, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (2, 16).
          Player 0 rolls 3 dice and gets outcomes [5, 6, 2].
          End scores = (15, 16)
          >>> print(turns[1])
          Start scores = (15, 16).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (15, 25)
          >>> print(turns[2])
          Start scores = (15, 25).
          Player 0 rolls 5 dice and gets outcomes [2, 3, 2, 5, 2].
          End scores = (29, 25)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=67699, score0=24, score1=17, goal=28, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (24, 17).
          Player 0 rolls 8 dice and gets outcomes [2, 1, 3, 6, 6, 4, 3, 5].
          End scores = (25, 17)
          >>> print(turns[1])
          Start scores = (25, 17).
          Player 1 rolls 5 dice and gets outcomes [4, 3, 4, 4, 5].
          End scores = (25, 37)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25815, score0=52, score1=11, goal=54, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (52, 11).
          Player 0 rolls 2 dice and gets outcomes [5, 5].
          End scores = (62, 11)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=41969, score0=38, score1=54, goal=78, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (38, 54).
          Player 0 rolls 7 dice and gets outcomes [1, 1, 2, 5, 6, 2, 4].
          End scores = (39, 54)
          >>> print(turns[1])
          Start scores = (39, 54).
          Player 1 rolls 2 dice and gets outcomes [1, 4].
          End scores = (39, 55)
          >>> print(turns[2])
          Start scores = (39, 55).
          Player 0 rolls 7 dice and gets outcomes [5, 6, 4, 2, 2, 5, 2].
          End scores = (65, 55)
          >>> print(turns[3])
          Start scores = (65, 55).
          Player 1 rolls 2 dice and gets outcomes [3, 5].
          End scores = (65, 63)
          >>> print(turns[4])
          Start scores = (65, 63).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (68, 63)
          >>> print(turns[5])
          Start scores = (68, 63).
          Player 1 rolls 7 dice and gets outcomes [1, 6, 5, 5, 1, 6, 6].
          End scores = (68, 64)
          >>> print(turns[6])
          Start scores = (68, 64).
          Player 0 rolls 6 dice and gets outcomes [1, 1, 3, 3, 3, 1].
          End scores = (69, 64)
          >>> print(turns[7])
          Start scores = (69, 64).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (69, 68)
          >>> print(turns[8])
          Start scores = (69, 68).
          Player 0 rolls 10 dice and gets outcomes [5, 2, 4, 6, 3, 4, 3, 4, 4, 2].
          End scores = (106, 68)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=68309, score0=53, score1=40, goal=56, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (53, 40).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (55, 40)
          >>> print(turns[1])
          Start scores = (55, 40).
          Player 1 rolls 4 dice and gets outcomes [4, 3, 5, 6].
          End scores = (55, 58)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=8243, score0=28, score1=23, goal=30, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (28, 23).
          Player 0 rolls 2 dice and gets outcomes [4, 2].
          End scores = (34, 23)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=43015, score0=53, score1=74, goal=77, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (53, 74).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (59, 74)
          >>> print(turns[1])
          Start scores = (59, 74).
          Player 1 rolls 7 dice and gets outcomes [5, 6, 6, 6, 1, 4, 3].
          End scores = (59, 75)
          >>> print(turns[2])
          Start scores = (59, 75).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (64, 75)
          >>> print(turns[3])
          Start scores = (64, 75).
          Player 1 rolls 4 dice and gets outcomes [3, 2, 1, 6].
          End scores = (64, 76)
          >>> print(turns[4])
          Start scores = (64, 76).
          Player 0 rolls 8 dice and gets outcomes [5, 4, 6, 2, 3, 2, 4, 4].
          End scores = (94, 76)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=76012, score0=39, score1=36, goal=73, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (39, 36).
          Player 0 rolls 9 dice and gets outcomes [1, 4, 6, 6, 6, 6, 6, 2, 1].
          End scores = (40, 36)
          >>> print(turns[1])
          Start scores = (40, 36).
          Player 1 rolls 2 dice and gets outcomes [3, 3].
          End scores = (40, 42)
          >>> print(turns[2])
          Start scores = (40, 42).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 5, 3, 6, 2].
          End scores = (61, 42)
          >>> print(turns[3])
          Start scores = (61, 42).
          Player 1 rolls 5 dice and gets outcomes [6, 3, 5, 1, 1].
          End scores = (61, 43)
          >>> print(turns[4])
          Start scores = (61, 43).
          Player 0 rolls 7 dice and gets outcomes [5, 1, 6, 6, 6, 2, 1].
          End scores = (43, 62)
          >>> print(turns[5])
          Start scores = (43, 62).
          Player 1 rolls 7 dice and gets outcomes [2, 4, 4, 4, 5, 5, 5].
          End scores = (43, 91)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=9818, score0=11, score1=9, goal=64, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (11, 9).
          Player 0 rolls 7 dice and gets outcomes [2, 5, 3, 3, 6, 6, 4].
          End scores = (40, 9)
          >>> print(turns[1])
          Start scores = (40, 9).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (10, 40)
          >>> print(turns[2])
          Start scores = (10, 40).
          Player 0 rolls 4 dice and gets outcomes [1, 2, 4, 1].
          End scores = (11, 40)
          >>> print(turns[3])
          Start scores = (11, 40).
          Player 1 rolls 10 dice and gets outcomes [2, 6, 3, 4, 2, 6, 5, 5, 4, 2].
          End scores = (11, 79)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25916, score0=86, score1=24, goal=88, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (86, 24).
          Player 0 rolls 5 dice and gets outcomes [4, 1, 5, 5, 1].
          End scores = (87, 24)
          >>> print(turns[1])
          Start scores = (87, 24).
          Player 1 rolls 6 dice and gets outcomes [5, 4, 4, 2, 5, 2].
          End scores = (87, 46)
          >>> print(turns[2])
          Start scores = (87, 46).
          Player 0 rolls 5 dice and gets outcomes [2, 2, 1, 2, 4].
          End scores = (88, 46)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=15583, score0=11, score1=40, goal=55, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (11, 40).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (12, 40)
          >>> print(turns[1])
          Start scores = (12, 40).
          Player 1 rolls 6 dice and gets outcomes [2, 3, 5, 4, 4, 2].
          End scores = (12, 60)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=7242, score0=19, score1=46, goal=98, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (19, 46).
          Player 0 rolls 7 dice and gets outcomes [2, 2, 3, 5, 4, 1, 1].
          End scores = (20, 46)
          >>> print(turns[1])
          Start scores = (20, 46).
          Player 1 rolls 9 dice and gets outcomes [3, 1, 1, 6, 6, 5, 3, 1, 4].
          End scores = (20, 47)
          >>> print(turns[2])
          Start scores = (20, 47).
          Player 0 rolls 5 dice and gets outcomes [4, 5, 4, 6, 1].
          End scores = (24, 47)
          >>> print(turns[3])
          Start scores = (24, 47).
          Player 1 rolls 8 dice and gets outcomes [1, 6, 2, 3, 1, 1, 5, 4].
          End scores = (24, 48)
          >>> print(turns[4])
          Start scores = (24, 48).
          Player 0 rolls 2 dice and gets outcomes [4, 5].
          End scores = (33, 48)
          >>> print(turns[5])
          Start scores = (33, 48).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (33, 55)
          >>> print(turns[6])
          Start scores = (33, 55).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (36, 55)
          >>> print(turns[7])
          Start scores = (36, 55).
          Player 1 rolls 2 dice and gets outcomes [2, 2].
          End scores = (36, 62)
          >>> print(turns[8])
          Start scores = (36, 62).
          Player 0 rolls 9 dice and gets outcomes [1, 1, 1, 1, 1, 6, 6, 3, 5].
          End scores = (37, 62)
          >>> print(turns[9])
          Start scores = (37, 62).
          Player 1 rolls 2 dice and gets outcomes [3, 2].
          End scores = (37, 67)
          >>> print(turns[10])
          Start scores = (37, 67).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 4, 5, 3, 1, 6, 1].
          End scores = (38, 67)
          >>> print(turns[11])
          Start scores = (38, 67).
          Player 1 rolls 5 dice and gets outcomes [6, 6, 3, 2, 1].
          End scores = (38, 68)
          >>> print(turns[12])
          Start scores = (38, 68).
          Player 0 rolls 8 dice and gets outcomes [1, 3, 6, 3, 1, 6, 3, 2].
          End scores = (39, 68)
          >>> print(turns[13])
          Start scores = (39, 68).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (39, 70)
          >>> print(turns[14])
          Start scores = (39, 70).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (44, 70)
          >>> print(turns[15])
          Start scores = (44, 70).
          Player 1 rolls 10 dice and gets outcomes [6, 2, 6, 3, 3, 6, 4, 4, 4, 1].
          End scores = (44, 71)
          >>> print(turns[16])
          Start scores = (44, 71).
          Player 0 rolls 8 dice and gets outcomes [4, 2, 5, 5, 1, 3, 4, 1].
          End scores = (45, 71)
          >>> print(turns[17])
          Start scores = (45, 71).
          Player 1 rolls 4 dice and gets outcomes [2, 1, 5, 3].
          End scores = (45, 72)
          >>> print(turns[18])
          Start scores = (45, 72).
          Player 0 rolls 8 dice and gets outcomes [1, 2, 3, 3, 1, 5, 4, 3].
          End scores = (46, 72)
          >>> print(turns[19])
          Start scores = (46, 72).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (46, 74)
          >>> print(turns[20])
          Start scores = (46, 74).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (52, 74)
          >>> print(turns[21])
          Start scores = (52, 74).
          Player 1 rolls 3 dice and gets outcomes [1, 6, 3].
          End scores = (52, 78)
          >>> print(turns[22])
          Start scores = (52, 78).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (55, 78)
          >>> print(turns[23])
          Start scores = (55, 78).
          Player 1 rolls 2 dice and gets outcomes [6, 5].
          End scores = (55, 89)
          >>> print(turns[24])
          Start scores = (55, 89).
          Player 0 rolls 3 dice and gets outcomes [5, 6, 2].
          End scores = (68, 89)
          >>> print(turns[25])
          Start scores = (68, 89).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 6].
          End scores = (68, 104)
          >>> print(turns[26])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=74122, score0=18, score1=14, goal=32, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (18, 14).
          Player 0 rolls 7 dice and gets outcomes [3, 2, 5, 2, 2, 6, 1].
          End scores = (19, 14)
          >>> print(turns[1])
          Start scores = (19, 14).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (19, 23)
          >>> print(turns[2])
          Start scores = (19, 23).
          Player 0 rolls 5 dice and gets outcomes [1, 3, 3, 5, 3].
          End scores = (20, 23)
          >>> print(turns[3])
          Start scores = (20, 23).
          Player 1 rolls 6 dice and gets outcomes [4, 3, 6, 3, 2, 5].
          End scores = (20, 46)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=59593, score0=27, score1=9, goal=40, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (27, 9).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (37, 9)
          >>> print(turns[1])
          Start scores = (37, 9).
          Player 1 rolls 7 dice and gets outcomes [5, 4, 4, 2, 2, 5, 4].
          End scores = (37, 35)
          >>> print(turns[2])
          Start scores = (37, 35).
          Player 0 rolls 10 dice and gets outcomes [6, 2, 2, 4, 4, 1, 6, 4, 4, 4].
          End scores = (38, 35)
          >>> print(turns[3])
          Start scores = (38, 35).
          Player 1 rolls 9 dice and gets outcomes [2, 1, 4, 6, 3, 1, 2, 2, 4].
          End scores = (38, 36)
          >>> print(turns[4])
          Start scores = (38, 36).
          Player 0 rolls 5 dice and gets outcomes [6, 1, 5, 6, 1].
          End scores = (39, 36)
          >>> print(turns[5])
          Start scores = (39, 36).
          Player 1 rolls 10 dice and gets outcomes [6, 3, 1, 6, 6, 2, 5, 2, 4, 4].
          End scores = (39, 37)
          >>> print(turns[6])
          Start scores = (39, 37).
          Player 0 rolls 9 dice and gets outcomes [3, 2, 6, 4, 2, 6, 4, 6, 5].
          End scores = (77, 37)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=8128, score0=17, score1=8, goal=29, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (17, 8).
          Player 0 rolls 7 dice and gets outcomes [4, 2, 4, 5, 3, 2, 3].
          End scores = (40, 8)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=22810, score0=7, score1=0, goal=43, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (7, 0).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (17, 0)
          >>> print(turns[1])
          Start scores = (17, 0).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (17, 9)
          >>> print(turns[2])
          Start scores = (17, 9).
          Player 0 rolls 3 dice and gets outcomes [5, 3, 2].
          End scores = (27, 9)
          >>> print(turns[3])
          Start scores = (27, 9).
          Player 1 rolls 2 dice and gets outcomes [1, 4].
          End scores = (27, 10)
          >>> print(turns[4])
          Start scores = (27, 10).
          Player 0 rolls 10 dice and gets outcomes [1, 1, 3, 1, 4, 3, 5, 3, 5, 1].
          End scores = (28, 10)
          >>> print(turns[5])
          Start scores = (28, 10).
          Player 1 rolls 4 dice and gets outcomes [6, 3, 1, 5].
          End scores = (28, 11)
          >>> print(turns[6])
          Start scores = (28, 11).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (37, 11)
          >>> print(turns[7])
          Start scores = (37, 11).
          Player 1 rolls 10 dice and gets outcomes [4, 3, 1, 2, 6, 5, 5, 4, 6, 6].
          End scores = (37, 12)
          >>> print(turns[8])
          Start scores = (37, 12).
          Player 0 rolls 2 dice and gets outcomes [6, 2].
          End scores = (45, 12)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=59348, score0=95, score1=84, goal=97, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (95, 84).
          Player 0 rolls 5 dice and gets outcomes [2, 3, 3, 4, 1].
          End scores = (96, 84)
          >>> print(turns[1])
          Start scores = (96, 84).
          Player 1 rolls 9 dice and gets outcomes [3, 1, 1, 6, 2, 4, 4, 2, 3].
          End scores = (96, 85)
          >>> print(turns[2])
          Start scores = (96, 85).
          Player 0 rolls 6 dice and gets outcomes [4, 1, 3, 1, 5, 6].
          End scores = (97, 85)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=88169, score0=23, score1=40, goal=79, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (23, 40).
          Player 0 rolls 3 dice and gets outcomes [1, 5, 6].
          End scores = (24, 40)
          >>> print(turns[1])
          Start scores = (24, 40).
          Player 1 rolls 5 dice and gets outcomes [2, 6, 6, 6, 2].
          End scores = (24, 62)
          >>> print(turns[2])
          Start scores = (24, 62).
          Player 0 rolls 2 dice and gets outcomes [3, 3].
          End scores = (30, 62)
          >>> print(turns[3])
          Start scores = (30, 62).
          Player 1 rolls 7 dice and gets outcomes [6, 5, 4, 2, 3, 5, 1].
          End scores = (30, 63)
          >>> print(turns[4])
          Start scores = (30, 63).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (37, 63)
          >>> print(turns[5])
          Start scores = (37, 63).
          Player 1 rolls 3 dice and gets outcomes [6, 3, 2].
          End scores = (37, 74)
          >>> print(turns[6])
          Start scores = (37, 74).
          Player 0 rolls 8 dice and gets outcomes [5, 6, 6, 4, 5, 3, 3, 4].
          End scores = (73, 74)
          >>> print(turns[7])
          Start scores = (73, 74).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (73, 81)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=70467, score0=61, score1=74, goal=97, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (61, 74).
          Player 0 rolls 8 dice and gets outcomes [4, 4, 6, 4, 3, 1, 5, 1].
          End scores = (62, 74)
          >>> print(turns[1])
          Start scores = (62, 74).
          Player 1 rolls 4 dice and gets outcomes [5, 6, 5, 3].
          End scores = (62, 93)
          >>> print(turns[2])
          Start scores = (62, 93).
          Player 0 rolls 3 dice and gets outcomes [4, 1, 5].
          End scores = (63, 93)
          >>> print(turns[3])
          Start scores = (63, 93).
          Player 1 rolls 8 dice and gets outcomes [6, 6, 4, 6, 1, 5, 3, 2].
          End scores = (63, 94)
          >>> print(turns[4])
          Start scores = (63, 94).
          Player 0 rolls 7 dice and gets outcomes [2, 1, 3, 3, 6, 1, 6].
          End scores = (64, 94)
          >>> print(turns[5])
          Start scores = (64, 94).
          Player 1 rolls 7 dice and gets outcomes [3, 6, 4, 5, 3, 1, 2].
          End scores = (64, 95)
          >>> print(turns[6])
          Start scores = (64, 95).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (69, 95)
          >>> print(turns[7])
          Start scores = (69, 95).
          Player 1 rolls 4 dice and gets outcomes [6, 4, 4, 2].
          End scores = (69, 111)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=8714, score0=38, score1=19, goal=57, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (38, 19).
          Player 0 rolls 10 dice and gets outcomes [5, 1, 1, 1, 4, 5, 5, 4, 6, 5].
          End scores = (39, 19)
          >>> print(turns[1])
          Start scores = (39, 19).
          Player 1 rolls 4 dice and gets outcomes [6, 3, 4, 3].
          End scores = (39, 35)
          >>> print(turns[2])
          Start scores = (39, 35).
          Player 0 rolls 9 dice and gets outcomes [5, 1, 5, 4, 2, 5, 5, 5, 4].
          End scores = (40, 35)
          >>> print(turns[3])
          Start scores = (40, 35).
          Player 1 rolls 4 dice and gets outcomes [2, 1, 5, 4].
          End scores = (40, 36)
          >>> print(turns[4])
          Start scores = (40, 36).
          Player 0 rolls 5 dice and gets outcomes [3, 6, 1, 5, 1].
          End scores = (41, 36)
          >>> print(turns[5])
          Start scores = (41, 36).
          Player 1 rolls 7 dice and gets outcomes [3, 3, 4, 6, 5, 4, 2].
          End scores = (41, 63)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=13230, score0=65, score1=56, goal=77, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (65, 56).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (67, 56)
          >>> print(turns[1])
          Start scores = (67, 56).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (67, 61)
          >>> print(turns[2])
          Start scores = (67, 61).
          Player 0 rolls 5 dice and gets outcomes [2, 1, 3, 4, 2].
          End scores = (68, 61)
          >>> print(turns[3])
          Start scores = (68, 61).
          Player 1 rolls 2 dice and gets outcomes [5, 4].
          End scores = (68, 70)
          >>> print(turns[4])
          Start scores = (68, 70).
          Player 0 rolls 5 dice and gets outcomes [1, 1, 5, 3, 6].
          End scores = (69, 70)
          >>> print(turns[5])
          Start scores = (69, 70).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (69, 77)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=96667, score0=2, score1=3, goal=13, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (2, 3).
          Player 0 rolls 5 dice and gets outcomes [1, 1, 3, 5, 3].
          End scores = (3, 3)
          >>> print(turns[1])
          Start scores = (3, 3).
          Player 1 rolls 8 dice and gets outcomes [6, 6, 4, 1, 2, 3, 5, 3].
          End scores = (3, 4)
          >>> print(turns[2])
          Start scores = (3, 4).
          Player 0 rolls 7 dice and gets outcomes [6, 2, 1, 4, 6, 5, 2].
          End scores = (7, 4)
          >>> print(turns[3])
          Start scores = (7, 4).
          Player 1 rolls 6 dice and gets outcomes [2, 6, 2, 4, 1, 3].
          End scores = (7, 8)
          >>> print(turns[4])
          Start scores = (7, 8).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (10, 8)
          >>> print(turns[5])
          Start scores = (10, 8).
          Player 1 rolls 5 dice and gets outcomes [4, 2, 4, 3, 6].
          End scores = (10, 27)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=27904, score0=23, score1=39, goal=92, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (23, 39).
          Player 0 rolls 3 dice and gets outcomes [6, 6, 2].
          End scores = (37, 39)
          >>> print(turns[1])
          Start scores = (37, 39).
          Player 1 rolls 6 dice and gets outcomes [6, 1, 4, 3, 4, 3].
          End scores = (37, 40)
          >>> print(turns[2])
          Start scores = (37, 40).
          Player 0 rolls 3 dice and gets outcomes [4, 3, 3].
          End scores = (47, 40)
          >>> print(turns[3])
          Start scores = (47, 40).
          Player 1 rolls 7 dice and gets outcomes [4, 5, 5, 6, 2, 4, 1].
          End scores = (47, 41)
          >>> print(turns[4])
          Start scores = (47, 41).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 4, 5, 2, 2, 4].
          End scores = (72, 41)
          >>> print(turns[5])
          Start scores = (72, 41).
          Player 1 rolls 6 dice and gets outcomes [1, 1, 5, 5, 6, 1].
          End scores = (72, 42)
          >>> print(turns[6])
          Start scores = (72, 42).
          Player 0 rolls 3 dice and gets outcomes [6, 1, 1].
          End scores = (73, 42)
          >>> print(turns[7])
          Start scores = (73, 42).
          Player 1 rolls 10 dice and gets outcomes [2, 5, 2, 2, 5, 2, 6, 6, 2, 3].
          End scores = (73, 77)
          >>> print(turns[8])
          Start scores = (73, 77).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 4, 5, 2, 1].
          End scores = (74, 77)
          >>> print(turns[9])
          Start scores = (74, 77).
          Player 1 rolls 9 dice and gets outcomes [5, 5, 3, 6, 6, 2, 2, 6, 1].
          End scores = (74, 78)
          >>> print(turns[10])
          Start scores = (74, 78).
          Player 0 rolls 8 dice and gets outcomes [1, 6, 5, 2, 3, 2, 2, 2].
          End scores = (75, 78)
          >>> print(turns[11])
          Start scores = (75, 78).
          Player 1 rolls 6 dice and gets outcomes [4, 4, 6, 1, 5, 4].
          End scores = (75, 79)
          >>> print(turns[12])
          Start scores = (75, 79).
          Player 0 rolls 7 dice and gets outcomes [6, 5, 5, 4, 6, 5, 2].
          End scores = (108, 79)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=36152, score0=49, score1=25, goal=52, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (49, 25).
          Player 0 rolls 10 dice and gets outcomes [1, 5, 6, 1, 3, 3, 1, 2, 2, 2].
          End scores = (50, 25)
          >>> print(turns[1])
          Start scores = (50, 25).
          Player 1 rolls 10 dice and gets outcomes [2, 3, 1, 5, 5, 3, 2, 2, 3, 1].
          End scores = (50, 26)
          >>> print(turns[2])
          Start scores = (50, 26).
          Player 0 rolls 7 dice and gets outcomes [5, 3, 2, 2, 4, 3, 5].
          End scores = (74, 26)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=97165, score0=13, score1=4, goal=42, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (13, 4).
          Player 0 rolls 3 dice and gets outcomes [1, 3, 1].
          End scores = (14, 4)
          >>> print(turns[1])
          Start scores = (14, 4).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 4].
          End scores = (14, 17)
          >>> print(turns[2])
          Start scores = (14, 17).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 3, 5, 4, 6].
          End scores = (40, 17)
          >>> print(turns[3])
          Start scores = (40, 17).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (40, 18)
          >>> print(turns[4])
          Start scores = (40, 18).
          Player 0 rolls 2 dice and gets outcomes [2, 4].
          End scores = (46, 18)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=7964, score0=0, score1=12, goal=30, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (0, 12).
          Player 0 rolls 5 dice and gets outcomes [2, 5, 5, 4, 6].
          End scores = (22, 12)
          >>> print(turns[1])
          Start scores = (22, 12).
          Player 1 rolls 5 dice and gets outcomes [3, 3, 2, 4, 2].
          End scores = (22, 26)
          >>> print(turns[2])
          Start scores = (22, 26).
          Player 0 rolls 2 dice and gets outcomes [2, 1].
          End scores = (23, 26)
          >>> print(turns[3])
          Start scores = (23, 26).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (23, 27)
          >>> print(turns[4])
          Start scores = (23, 27).
          Player 0 rolls 7 dice and gets outcomes [2, 4, 1, 2, 5, 5, 5].
          End scores = (24, 27)
          >>> print(turns[5])
          Start scores = (24, 27).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (24, 35)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=87291, score0=59, score1=15, goal=87, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (59, 15).
          Player 0 rolls 6 dice and gets outcomes [2, 2, 1, 6, 2, 4].
          End scores = (60, 15)
          >>> print(turns[1])
          Start scores = (60, 15).
          Player 1 rolls 10 dice and gets outcomes [4, 4, 3, 5, 2, 3, 3, 5, 1, 6].
          End scores = (60, 16)
          >>> print(turns[2])
          Start scores = (60, 16).
          Player 0 rolls 2 dice and gets outcomes [6, 2].
          End scores = (68, 16)
          >>> print(turns[3])
          Start scores = (68, 16).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (68, 19)
          >>> print(turns[4])
          Start scores = (68, 19).
          Player 0 rolls 7 dice and gets outcomes [4, 6, 2, 5, 6, 3, 2].
          End scores = (96, 19)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=2481, score0=32, score1=79, goal=98, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (32, 79).
          Player 0 rolls 4 dice and gets outcomes [2, 4, 4, 5].
          End scores = (47, 79)
          >>> print(turns[1])
          Start scores = (47, 79).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (47, 85)
          >>> print(turns[2])
          Start scores = (47, 85).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (52, 85)
          >>> print(turns[3])
          Start scores = (52, 85).
          Player 1 rolls 4 dice and gets outcomes [2, 5, 3, 1].
          End scores = (52, 86)
          >>> print(turns[4])
          Start scores = (52, 86).
          Player 0 rolls 3 dice and gets outcomes [2, 5, 2].
          End scores = (61, 86)
          >>> print(turns[5])
          Start scores = (61, 86).
          Player 1 rolls 3 dice and gets outcomes [2, 5, 5].
          End scores = (61, 98)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=57878, score0=4, score1=13, goal=29, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (4, 13).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 1, 6, 3, 3].
          End scores = (5, 13)
          >>> print(turns[1])
          Start scores = (5, 13).
          Player 1 rolls 5 dice and gets outcomes [4, 2, 3, 3, 4].
          End scores = (5, 29)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=27303, score0=31, score1=3, goal=39, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (31, 3).
          Player 0 rolls 4 dice and gets outcomes [6, 5, 6, 1].
          End scores = (32, 3)
          >>> print(turns[1])
          Start scores = (32, 3).
          Player 1 rolls 4 dice and gets outcomes [6, 2, 2, 2].
          End scores = (32, 15)
          >>> print(turns[2])
          Start scores = (32, 15).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (38, 15)
          >>> print(turns[3])
          Start scores = (38, 15).
          Player 1 rolls 9 dice and gets outcomes [1, 6, 1, 1, 5, 5, 2, 1, 6].
          End scores = (38, 16)
          >>> print(turns[4])
          Start scores = (38, 16).
          Player 0 rolls 9 dice and gets outcomes [3, 6, 6, 6, 6, 3, 3, 5, 5].
          End scores = (81, 16)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=98514, score0=46, score1=42, goal=60, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (46, 42).
          Player 0 rolls 7 dice and gets outcomes [5, 1, 3, 3, 5, 6, 3].
          End scores = (47, 42)
          >>> print(turns[1])
          Start scores = (47, 42).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (47, 48)
          >>> print(turns[2])
          Start scores = (47, 48).
          Player 0 rolls 6 dice and gets outcomes [4, 4, 5, 1, 4, 6].
          End scores = (48, 48)
          >>> print(turns[3])
          Start scores = (48, 48).
          Player 1 rolls 9 dice and gets outcomes [4, 5, 6, 3, 2, 2, 6, 5, 4].
          End scores = (48, 85)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=64395, score0=3, score1=18, goal=52, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (3, 18).
          Player 0 rolls 10 dice and gets outcomes [4, 4, 6, 3, 2, 6, 3, 3, 2, 2].
          End scores = (38, 18)
          >>> print(turns[1])
          Start scores = (38, 18).
          Player 1 rolls 2 dice and gets outcomes [1, 2].
          End scores = (38, 19)
          >>> print(turns[2])
          Start scores = (38, 19).
          Player 0 rolls 10 dice and gets outcomes [6, 5, 6, 3, 3, 2, 6, 4, 1, 4].
          End scores = (39, 19)
          >>> print(turns[3])
          Start scores = (39, 19).
          Player 1 rolls 2 dice and gets outcomes [5, 2].
          End scores = (39, 26)
          >>> print(turns[4])
          Start scores = (39, 26).
          Player 0 rolls 10 dice and gets outcomes [1, 3, 4, 4, 5, 3, 1, 1, 4, 3].
          End scores = (40, 26)
          >>> print(turns[5])
          Start scores = (40, 26).
          Player 1 rolls 2 dice and gets outcomes [6, 2].
          End scores = (40, 34)
          >>> print(turns[6])
          Start scores = (40, 34).
          Player 0 rolls 9 dice and gets outcomes [4, 3, 2, 2, 6, 1, 1, 2, 5].
          End scores = (41, 34)
          >>> print(turns[7])
          Start scores = (41, 34).
          Player 1 rolls 7 dice and gets outcomes [5, 6, 6, 6, 2, 1, 5].
          End scores = (41, 35)
          >>> print(turns[8])
          Start scores = (41, 35).
          Player 0 rolls 6 dice and gets outcomes [6, 5, 4, 2, 2, 4].
          End scores = (64, 35)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=13464, score0=27, score1=4, goal=47, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (27, 4).
          Player 0 rolls 4 dice and gets outcomes [3, 1, 5, 4].
          End scores = (4, 28)
          >>> print(turns[1])
          Start scores = (4, 28).
          Player 1 rolls 8 dice and gets outcomes [5, 3, 2, 5, 4, 5, 3, 6].
          End scores = (4, 61)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=92338, score0=64, score1=67, goal=69, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (64, 67).
          Player 0 rolls 7 dice and gets outcomes [6, 2, 4, 4, 6, 4, 4].
          End scores = (94, 67)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=55414, score0=9, score1=19, goal=32, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (9, 19).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (10, 19)
          >>> print(turns[1])
          Start scores = (10, 19).
          Player 1 rolls 7 dice and gets outcomes [3, 2, 6, 1, 2, 5, 3].
          End scores = (20, 10)
          >>> print(turns[2])
          Start scores = (20, 10).
          Player 0 rolls 2 dice and gets outcomes [4, 2].
          End scores = (26, 10)
          >>> print(turns[3])
          Start scores = (26, 10).
          Player 1 rolls 8 dice and gets outcomes [4, 6, 1, 5, 1, 3, 2, 1].
          End scores = (26, 11)
          >>> print(turns[4])
          Start scores = (26, 11).
          Player 0 rolls 9 dice and gets outcomes [3, 4, 2, 6, 6, 6, 2, 2, 5].
          End scores = (62, 11)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=2412, score0=90, score1=38, goal=94, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (90, 38).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (95, 38)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=43957, score0=35, score1=51, goal=100, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (35, 51).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (44, 51)
          >>> print(turns[1])
          Start scores = (44, 51).
          Player 1 rolls 9 dice and gets outcomes [2, 3, 4, 6, 3, 2, 5, 3, 1].
          End scores = (44, 52)
          >>> print(turns[2])
          Start scores = (44, 52).
          Player 0 rolls 4 dice and gets outcomes [1, 3, 5, 1].
          End scores = (45, 52)
          >>> print(turns[3])
          Start scores = (45, 52).
          Player 1 rolls 3 dice and gets outcomes [1, 4, 2].
          End scores = (45, 53)
          >>> print(turns[4])
          Start scores = (45, 53).
          Player 0 rolls 8 dice and gets outcomes [5, 3, 3, 4, 5, 5, 3, 6].
          End scores = (79, 53)
          >>> print(turns[5])
          Start scores = (79, 53).
          Player 1 rolls 4 dice and gets outcomes [6, 5, 2, 6].
          End scores = (79, 72)
          >>> print(turns[6])
          Start scores = (79, 72).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (87, 72)
          >>> print(turns[7])
          Start scores = (87, 72).
          Player 1 rolls 3 dice and gets outcomes [5, 1, 3].
          End scores = (87, 73)
          >>> print(turns[8])
          Start scores = (87, 73).
          Player 0 rolls 2 dice and gets outcomes [1, 2].
          End scores = (91, 73)
          >>> print(turns[9])
          Start scores = (91, 73).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (91, 82)
          >>> print(turns[10])
          Start scores = (91, 82).
          Player 0 rolls 6 dice and gets outcomes [1, 1, 3, 2, 3, 1].
          End scores = (92, 82)
          >>> print(turns[11])
          Start scores = (92, 82).
          Player 1 rolls 8 dice and gets outcomes [3, 4, 4, 4, 4, 1, 5, 4].
          End scores = (92, 83)
          >>> print(turns[12])
          Start scores = (92, 83).
          Player 0 rolls 10 dice and gets outcomes [5, 3, 2, 1, 3, 3, 3, 1, 3, 6].
          End scores = (93, 83)
          >>> print(turns[13])
          Start scores = (93, 83).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (93, 89)
          >>> print(turns[14])
          Start scores = (93, 89).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (95, 89)
          >>> print(turns[15])
          Start scores = (95, 89).
          Player 1 rolls 8 dice and gets outcomes [1, 3, 5, 1, 6, 4, 3, 6].
          End scores = (95, 90)
          >>> print(turns[16])
          Start scores = (95, 90).
          Player 0 rolls 6 dice and gets outcomes [4, 5, 1, 6, 3, 6].
          End scores = (96, 90)
          >>> print(turns[17])
          Start scores = (96, 90).
          Player 1 rolls 7 dice and gets outcomes [3, 4, 3, 3, 6, 2, 3].
          End scores = (96, 114)
          >>> print(turns[18])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=36287, score0=42, score1=52, goal=100, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (42, 52).
          Player 0 rolls 5 dice and gets outcomes [5, 4, 1, 5, 6].
          End scores = (43, 52)
          >>> print(turns[1])
          Start scores = (43, 52).
          Player 1 rolls 2 dice and gets outcomes [4, 2].
          End scores = (43, 61)
          >>> print(turns[2])
          Start scores = (43, 61).
          Player 0 rolls 4 dice and gets outcomes [3, 4, 4, 3].
          End scores = (57, 61)
          >>> print(turns[3])
          Start scores = (57, 61).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (57, 65)
          >>> print(turns[4])
          Start scores = (57, 65).
          Player 0 rolls 3 dice and gets outcomes [6, 2, 4].
          End scores = (69, 65)
          >>> print(turns[5])
          Start scores = (69, 65).
          Player 1 rolls 7 dice and gets outcomes [2, 4, 6, 4, 3, 6, 4].
          End scores = (69, 94)
          >>> print(turns[6])
          Start scores = (69, 94).
          Player 0 rolls 8 dice and gets outcomes [4, 6, 6, 4, 4, 4, 4, 1].
          End scores = (70, 94)
          >>> print(turns[7])
          Start scores = (70, 94).
          Player 1 rolls 9 dice and gets outcomes [6, 1, 6, 2, 6, 5, 4, 1, 3].
          End scores = (70, 98)
          >>> print(turns[8])
          Start scores = (70, 98).
          Player 0 rolls 10 dice and gets outcomes [1, 3, 1, 1, 2, 2, 2, 2, 2, 1].
          End scores = (74, 98)
          >>> print(turns[9])
          Start scores = (74, 98).
          Player 1 rolls 6 dice and gets outcomes [5, 4, 5, 2, 3, 4].
          End scores = (74, 121)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=36008, score0=3, score1=9, goal=11, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 9).
          Player 0 rolls 5 dice and gets outcomes [3, 3, 4, 3, 2].
          End scores = (18, 9)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> # Fuzz Testing
      >>> # Plays a lot of random games, and calculates a secret value.
      >>> # Failing this test means something is wrong, but you should
      >>> # look at other tests to see where the problem might be.
      >>> # Hint: make sure you're only calling take_turn once per turn!
      >>> #
      >>> import hog, importlib, hog_gui
      >>> # importlib.reload(hog)
      >>> import tests.play_utils
      """,
      'teardown': r"""
      
      """,
      'type': 'doctest'
    }
  ]
}
