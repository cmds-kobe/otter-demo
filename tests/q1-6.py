OK_FORMAT = True

test = {   'name': 'q1-6',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> (total, average) = subject_total(100, 100, 100, 100, 100)\n>>> assert total == 500, '合計点が正しくありません'\n>>> assert average == 100.0, '平均点が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> (total, average) = subject_total(80, 90, 85, 70, 75)\n>>> assert total == 400, '合計点が正しくありません'\n>>> assert average == 80.0, '平均点が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> (total, average) = subject_total(0, 50, 75, 85, 95)\n>>> assert total == 305, '合計点が正しくありません'\n>>> assert average == 61.0, '平均点が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> (total, average) = subject_total(88, 76, 94, 85, 92)\n>>> assert total == 435, '合計点が正しくありません'\n>>> assert average == 87.0, '平均点が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
