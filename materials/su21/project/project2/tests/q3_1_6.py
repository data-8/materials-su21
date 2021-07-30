test = {   'name': 'q3_1_6',
    'points': [0, 0, 1, 1, 0],
    'suites': [   {   'cases': [   {'code': '>>> len(my_features) >= 10\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.all([f in test_movies.labels for f in my_features])\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # It looks like there are many movies in the training set that\n'
                                               ">>> # don't have any of your chosen words.  That will make your\n"
                                               '>>> # classifier perform very poorly in some cases.  Try choosing\n'
                                               '>>> # at least 1 common word.\n'
                                               '>>> train_f = train_movies.select(my_features)\n'
                                               '>>> np.count_nonzero(train_f.apply(lambda r: np.sum(np.abs(np.array(list(r)))) == 0)) < len(my_features)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # It looks like there are many movies in the test set that\n'
                                               ">>> # don't have any of your chosen words.  That will make your\n"
                                               '>>> # classifier perform very poorly in some cases.  Try choosing\n'
                                               '>>> # at least 1 common word.\n'
                                               '>>> test_f = test_movies.select(my_features)\n'
                                               '>>> np.count_nonzero(test_f.apply(lambda r: np.sum(np.abs(np.array(list(r)))) == 0)) < 5\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> # It looks like you may have duplicate words! Make sure not to!\n>>> len(set(my_features)) >= 10\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
