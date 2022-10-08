def calculation(amount, nominal):
    if amount != '' and amount != '-' and amount.isnumeric():
        return str(round(float(amount) * nominal, 2))
    else:
        return '0'
calculation_dict_template={'input-500':'','input-200':'','input-100':'','input-50':'','input-20':'','input-10':'',
                           'input-5':'','input-2':'','input-1':'','input-0.5':'','input-0.2':'','input-0.1':'','input-0.05':'',
                           'input-0.02':'','input-0.01':'',}

calculation_dict={'sum-500':'input-500',
                  'sum-200':'input-200',
                  'sum-100':'input-100',
                  'sum-50':'input-50',
                  'sum-20':'input-20',
                  'sum-10':'input-10',
                  'sum-5':'input-5',
                  'sum-2':'input-2',
                  'sum-1':'input-1',
                  'sum-0.5':'input-0.5',
                  'sum-0.2':'input-0.2',
                  'sum-0.1':'input-0.1',
                  'sum-0.05':'input-0.05',
                  'sum-0.02':'input-0.02',
                  'sum-0.01':'input-0.01'}

text_calc_dict={'sumtext-500':"sum-500",
                  'sumtext-200':"sum-200",
                  'sumtext-100':"sum-100",
                  'sumtext-50':"sum-50",
                  'sumtext-20':"sum-20",
                  'sumtext-10':"sum-10",
                  'sumtext-5':"sum-5",
                  'sumtext-2':"sum-2",
                  'sumtext-1':"sum-1",
                  'sumtext-0.5':"sum-0.5",
                  'sumtext-0.2':"sum-0.2",
                  'sumtext-0.1':"sum-0.1",
                  'sumtext-0.05':"sum-0.05",
                  'sumtext-0.02':"sum-0.02",
                   'sumtext-0.01':"sum-0.01"}