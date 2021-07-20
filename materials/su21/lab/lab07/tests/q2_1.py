test = {   'name': 'q2_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> # This is a little magic to make sure that you see the same results\n'
                                               '>>> # we did.\n'
                                               '>>> np.random.seed(123)\n'
                                               '>>> \n'
                                               '>>> one_resample = simulate_resample()\n'
                                               '>>> ten_rows = one_resample.take(np.arange(10))\n'
                                               '>>> ten_rows\n'
                                               'serial number\n'
                                               '108\n'
                                               '57\n'
                                               '57\n'
                                               '36\n'
                                               '41\n'
                                               '42\n'
                                               '47\n'
                                               '50\n'
                                               '135\n'
                                               '47',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> np.random.seed(123)\n>>> \n>>> one_resample = simulate_resample()\n>>> one_resample.num_rows == 17\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
