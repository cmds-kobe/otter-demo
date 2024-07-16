OK_FORMAT = True

test = {   'name': 'q1-1',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> assert 'mackerel' in globals(), 'mackerelが定義されていません'\n>>> assert mackerel == 176, 'mackerelの価格が正しくありません'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert 'egg' in globals(), 'eggが定義されていません'\n>>> assert egg == 88, 'eggの価格が正しくありません'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert 'salad' in globals(), 'saladが定義されていません'\n>>> assert salad == 44, 'saladの価格が正しくありません'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert 'chicken' in globals(), 'chickenが定義されていません'\n>>> assert chicken == 130, 'chickenの価格が正しくありません'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert 'rice' in globals(), 'riceが定義されていません'\n>>> assert rice == 94, 'riceの価格が正しくありません'\n", 'hidden': False, 'locked': False},
                                   {   'code': ">>> assert 'price_total' in globals(), 'price_totalが定義されていません'\n>>> assert price_total == 176 + 88 + 44 + 130 + 94, '合計金額が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> \n', 'hidden': False, 'locked': False},
                                   {'code': '>>> \n', 'hidden': False, 'locked': False},
                                   {'code': '>>> \n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
