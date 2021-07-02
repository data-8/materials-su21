test = {   'name': 'q2_5',
    'points': [2, 2],
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure that the table has a column called department and a column called count.\n'
                                               '>>> set(["department", "count"]) == set(department_and_counts.labels)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # Make sure you do not include departments that don't have positions with average salary above 100k.\n>>> department_and_counts.num_rows\n65",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
