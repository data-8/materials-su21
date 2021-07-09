test = {   'name': 'q3_1',
    'points': [0, 2, 2],
    'suites': [   {   'cases': [   {'code': '>>> full_data.num_rows == 457\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> # Double check the way you're combining the two tables. Are you combining in the correct order\n"
                                               '>>> # (in terms of the arguments)? The problem statement saying "except \'Name\' column" is a hint\n'
                                               '>>> # at the order in which you should combine the tables.\n'
                                               ">>> list(full_data.labels)[0] == 'Player'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> full_data.select(sorted(full_data.labels)).sort(4).take(range(3))\n'
                                               '2P   | 3P   | PTS  | Player         | Salary\n'
                                               '0    | 0    | 0    | William Howard | 50000\n'
                                               '2    | 0    | 6    | Eric Mika      | 50752\n'
                                               '0    | 0    | 0    | Marques Bolden | 50752',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
