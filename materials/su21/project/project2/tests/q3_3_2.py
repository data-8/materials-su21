test = {   'name': 'q3_3_2',
    'points': [0, 0, 4],
    'suites': [   {   'cases': [   {'code': ">>> test_movie_correctness.labels == ('Title', 'Genre', 'Was correct')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> test_movie_correctness.num_rows == test_movies.num_rows\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure that test_movie_correctness does not modify the original\n'
                                               '>>> # test_movies table.\n'
                                               ">>> print(test_movie_correctness.group('Genre'))\n"
                                               'Genre    | count\n'
                                               'comedy   | 20\n'
                                               'thriller | 36\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
