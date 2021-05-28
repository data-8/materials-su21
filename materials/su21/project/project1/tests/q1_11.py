test = {   'name': 'q1_11',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Incorrect labels for columns;\n'
                                               '>>> t = stats_for_year(1990);\n'
                                               ">>> t.labels == ('geo', 'population_total', 'children_per_woman_total_fertility', 'child_mortality_under_5_per_1000_born')\n",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> # Incorrect number of rows;\n>>> t = stats_for_year(1990);\n>>> t.num_rows\n', 'hidden': False, 'locked': False},
                                   {'code': ">>> print(stats_for_year(1960).sort('geo').take(np.arange(5, 50, 5)))\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> print(stats_for_year(2010).sort('geo').take(np.arange(3, 50, 5)))\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
