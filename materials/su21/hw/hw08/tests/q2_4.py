test = {   'name': 'q2_4',
    'points': [0, 0, 0],
    'suites': [   {   'cases': [   {'code': '>>> 1 <= restaurants_tied <= 3\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> # Remember, we are using a 95% confidence interval of [1.2, 11.2]. Our null hypothesis claims that Imm Thai's lead is 0.\n"
                                               '>>> # This falls outside of our 95% confidence interval. What can we conclude if we use a 5% p-value cutoff? \n'
                                               '>>> restaurants_tied == 3\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # We are using a 95% confidence interval of [1.2, 11.2]. Our null hypothesis claims that Imm Thai's lead is 0. This falls outside of our 95% "
                                               'confidence interval. \n'
                                               ">>> # 100% - 95% = 5%, which is our p-value cutoff. At the 5% level of significance, 0 doesn't seem like a plausible value for Imm Thai's lead. We "
                                               'would reject the null.\n'
                                               '>>> # Remember, there is a duality between confidence intervals and tests: if you are testing whether or not the true lead is a particular value x, '
                                               'and you use the 5% cutoff for the P-value, then you will reject the null hypothesis if x is not in your 95% confidence interval for the lead.\n'
                                               '>>> restaurants_tied == 2\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
