#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author: frg
"""
import requests


def bitcoin_last_price():
    url = 'https://blockchain.info/ticker'
    response = requests.get(url)

    if response.status_code == 200:
        response_json = response.json()
        data = {'USD': response_json['USD']['last'], "EUR": response_json['EUR']['last']}
    else:
        data = {'msg': 'Error http code ' + str(response.status_code)}

    return data


def last_price(coin=""):
    cyypto_url = 'https://min-api.cryptocompare.com/data/price'
    fiat = 'USD,EUR'
    key = '79d1890732c82b42fc6497c1dc59297ce5a8afae1127f27b303a7465bc65751d'
    coin = coin.upper()
    url = cyypto_url + '?fsym=' + coin + '&tsyms=' + fiat + '&api_key=' + key
    response = requests.get(url)

    if response.status_code == 200:
        response_json = response.json()

        if 'Response' in response_json:
            data = {'msg': response_json['Response'] + ": " + response_json['Message']}
        else:
            data = {coin: {'USD': response_json['USD'], "EUR": response_json['EUR']}}
    else:
        data = {'msg': 'Error http code ' + str(response.status_code)}

    return data
