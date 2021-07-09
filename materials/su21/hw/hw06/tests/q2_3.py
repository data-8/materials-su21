test = {   'name': 'q2_3',
    'points': [0, 1, 2],
    'suites': [   {   'cases': [   {'code': '>>> len(simulate_several_key_strikes(15)) == 15\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> # Make sure your function returns a string.\n>>> isinstance(simulate_several_key_strikes(15), str)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> # It looks like your simulation doesn't use all the letters,\n"
                                               '>>> # or it uses more than the 26 lower-case letters.\n'
                                               '>>> import numpy as np\n'
                                               '>>> np.random.seed(22)\n'
                                               '>>> 63 >= len(np.unique(list(simulate_several_key_strikes(500)))) >= 45\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
