#!/usr/bin/python
# -*- coding: utf-8 -*-  
from rest import KK_REST

api_key = ''
api_secret = open('yourprivate.key').read()
password = ''  # RSA private key password

kk_rest = KK_REST(api_key, api_secret, password)

symbol = 'KK_ETH'
order_type = 'LIMIT'
order_op = 'BUY'
price = 0.001
amount = 1000

result = kk_rest.trade(symbol, order_type, order_op, price, amount)
print(result)

result = kk_rest.balance()
print(result)
