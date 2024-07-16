OK_FORMAT = True

test = {   'name': 'q1-5',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> assert 'principal' in globals(), 'principalが定義されていません'\n>>> assert principal == 10000000, 'principalの値が正しくありません'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert 'rate' in globals(), 'rateが定義されていません'\n>>> assert rate == 0.002, 'rateの値が正しくありません'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert 'years' in globals(), 'yearsが定義されていません'\n>>> assert years == 10, 'yearsの値が正しくありません'\n", 'hidden': False, 'locked': False},
                                   {   'code': ">>> assert 'after_10_year' in globals(), 'after_10_yearが定義されていません'\n"
                                               ">>> assert after_10_year == principal * (1 + rate) ** years, 'after_10_yearの計算が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
