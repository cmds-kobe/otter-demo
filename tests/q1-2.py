OK_FORMAT = True

test = {   'name': 'q1-2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': ">>> assert 'chicken_material' in globals(), 'chicken_materialが定義されていません'\n>>> assert chicken_material == 60, 'chicken_materialの値が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert 'demand_per_day' in globals(), 'demand_per_dayが定義されていません'\n>>> assert demand_per_day == 500, 'demand_per_dayの値が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert 'chicken_per_day' in globals(), 'chicken_per_dayが定義されていません'\n>>> assert chicken_per_day == 30.0, 'chicken_per_dayの計算が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
