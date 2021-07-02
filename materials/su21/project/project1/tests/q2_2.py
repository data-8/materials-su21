test = {   'name': 'q2_2',
    'points': [0, 0, 0, 0],
    'suites': [   {   'cases': [   {   'code': '>>> # Remember to rename the columns from "Cell Name" to "Cell" \n'
                                               '>>> # and "Gene Name" to "Gene"\n'
                                               '>>> # You can use the tbl.relabeled function\n'
                                               ">>> 'Cell Name' not in matrix_with_names.labels\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # The new table should have the columns Cell, Gene and Expression\n'
                                               ">>> sorted(matrix_with_names.labels) == sorted(('Cell', 'Gene', 'Expression'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> # You shouldn't be modifiying any row names\n>>> matrix_with_names.num_rows == matrix.num_rows\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> # The Gene and Cell columns should contain strings not numbers\n'
                                               '>>> type(matrix_with_names.column("Gene").item(0)) != int and type(matrix_with_names.column("Cell").item(0)) != int\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
