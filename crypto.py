#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: frg
"""
import requests
import yaml

# init logger
with open('./config/config.yml', 'r') as file:
    config = yaml.safe_load(file)


def bitcoin_last_price():
    url = 'https://blockchain.info/ticker'
    response = requests.get(url)

    if response.status_code == 200:
        response_json = response.json()
        data = {
            'USD': response_json['USD']['last'],
            "EUR": response_json['EUR']['last']
               }
    else:
        data = {'msg': 'Error http code ' + str(response.status_code)}

    return data


def last_price(coin=""):
    cyypto_url = config['crypto']['url']
    fiat = ','.join(config['crypto']['currencies'])
    key = config['crypto']['key']
    url = cyypto_url + '?fsym=' + coin + '&tsyms=' + fiat + '&api_key=' + key
    response = requests.get(url)

    if response.status_code == 200:
        response_json = response.json()

        if 'Response' in response_json:
            data = {
                    'msg': response_json['Response'] +
                    ": " + response_json['Message']
                    }
        else:
            data = {
                   coin: {
                        'USD': response_json['USD'],
                        "EUR": response_json['EUR']
                         }
                   }
    else:
        data = {'msg': 'Error http code ' + str(response.status_code)}

    return data
