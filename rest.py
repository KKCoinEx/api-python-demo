#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import json
import requests
from collections import OrderedDict

from OpenSSL.crypto import load_privatekey, FILETYPE_PEM, sign
from base64 import b64encode, b64decode

BASE_URL = 'https://api.kkcoin.com'

class KK_REST:

    def __init__(self, api_key, api_secret, password):
        self.api_key = api_key
        self.api_secret = api_secret
        self.password = password.encode()

    def sign(self, payload):
        private_key = load_privatekey(FILETYPE_PEM, self.api_secret, self.password)

        signature = sign(private_key, payload, 'sha256')

        return b64encode(signature).decode()

    def trade(self, symbol, order_type, order_op, price, amount):
        path = '/rest/trade'
        request_url = BASE_URL + path

        payload = OrderedDict([
            ('amount', str(amount)),
            ('orderop', order_op),
            ('ordertype', order_type),
            ('price', str(price)),
            ('symbol', symbol)])

        nonce = str(int(time.time()))
        sigPayload = 'trade' + json.dumps(payload, separators=(',', ':')) + nonce
        signature = self.sign(sigPayload)
        print(sigPayload)
        print(signature)

        return requests.post(
            request_url,
            headers = {
                'KKCOINAPIKEY': self.api_key,
                'KKCOINSIGN': signature,
                'KKCOINTIMESTAMP': nonce
            },
            data = payload
        ).json()

    def balance(self):
        path = '/rest/balance'
        request_url = BASE_URL + path

        payload = []

        nonce = str(int(time.time()))
        sigPayload = 'balance' + json.dumps(payload) + nonce
        signature = self.sign(sigPayload)
        print(sigPayload)
        print(signature)

        return requests.get(
            request_url,
            headers = {
                'KKCOINAPIKEY': self.api_key,
                'KKCOINSIGN': signature,
                'KKCOINTIMESTAMP': nonce
            }
        ).json()
    
    def openorders(self, symbol):
        path = '/rest/openorders'
        request_url = BASE_URL + path

        payload = OrderedDict([
            ('symbol', symbol)])

        nonce = str(int(time.time()))
        sigPayload = 'openorders' + json.dumps(payload, separators=(',', ':')) + nonce
        signature = self.sign(sigPayload)

        return requests.get(
            request_url,
            headers = {
                'KKCOINAPIKEY': self.api_key,
                'KKCOINSIGN': signature,
                'KKCOINTIMESTAMP': nonce
            },
            params = payload
        ).json()
