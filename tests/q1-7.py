OK_FORMAT = True

test = {   'name': 'q1-7',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': ">>> result = calculate_order('Apple', 100, 10)\n"
                                               ">>> assert result['product_name'] == 'Apple', '商品名が正しくありません'\n"
                                               ">>> assert result['unit_price'] == 100, '単価が正しくありません'\n"
                                               ">>> assert result['quantity'] == 10, '数量が正しくありません'\n"
                                               ">>> assert result['tax_excluded_price'] == 1000, '税抜価格が正しくありません'\n"
                                               ">>> assert result['tax'] == 100, '消費税が正しくありません'\n"
                                               ">>> assert result['total_price'] == 1100, '合計価格が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> result = calculate_order('Banana', 200, 5)\n"
                                               ">>> assert result['product_name'] == 'Banana', '商品名が正しくありません'\n"
                                               ">>> assert result['unit_price'] == 200, '単価が正しくありません'\n"
                                               ">>> assert result['quantity'] == 5, '数量が正しくありません'\n"
                                               ">>> assert result['tax_excluded_price'] == 1000, '税抜価格が正しくありません'\n"
                                               ">>> assert result['tax'] == 100, '消費税が正しくありません'\n"
                                               ">>> assert result['total_price'] == 1100, '合計価格が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> result = calculate_order('Cherry', 50, 100)\n"
                                               ">>> assert result['product_name'] == 'Cherry', '商品名が正しくありません'\n"
                                               ">>> assert result['unit_price'] == 50, '単価が正しくありません'\n"
                                               ">>> assert result['quantity'] == 100, '数量が正しくありません'\n"
                                               ">>> assert result['tax_excluded_price'] == 5000, '税抜価格が正しくありません'\n"
                                               ">>> assert result['tax'] == 500, '消費税が正しくありません'\n"
                                               ">>> assert result['total_price'] == 5500, '合計価格が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> result = calculate_order('Grape', 123.45, 10)\n"
                                               ">>> assert result['product_name'] == 'Grape', '商品名が正しくありません'\n"
                                               ">>> assert result['unit_price'] == 123.45, '単価が正しくありません'\n"
                                               ">>> assert result['quantity'] == 10, '数量が正しくありません'\n"
                                               ">>> assert result['tax_excluded_price'] == 1234.5, '税抜価格が正しくありません'\n"
                                               ">>> assert result['tax'] == 123, '消費税が正しくありません'\n"
                                               ">>> assert result['total_price'] == 1357, '合計価格が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> \n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import io\n'
                                               '>>> import sys\n'
                                               '>>> captured_output = io.StringIO()\n'
                                               '>>> sys.stdout = captured_output\n'
                                               ">>> result = calculate_order('DUAL-RX7800XT-O16G', 79455, 23)\n"
                                               '>>> print_order_form(result)\n'
                                               ">>> expected_output = '注文商品           : DUAL-RX7800XT-O16G\\n＠    79,455円 × 23個\\n税抜価格           :  1,827,465円\\n消費税            :    "
                                               "182,746円\\n合計金額           :  2,010,211円\\n'\n"
                                               ">>> assert captured_output.getvalue() == expected_output, 'テストケース1が失敗しました'\n"
                                               '>>> sys.stdout = sys.__stdout__\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
