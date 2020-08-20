#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging.config
import logging
import yaml

from flask import Flask, jsonify
import crypto


# init logger
with open('./config/config.yml', 'r') as file:
    config = yaml.safe_load(file)

logging.config.dictConfig(config['logger'])
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/price/bitcoin', methods=['GET'])
def price_bitcoin():

    data = crypto.bitcoin_last_price()
    if data:
        logger.info('Get bitcoin price: ' + str(data))
        response_json = {"success": "true", "data": data}
    else:
        logger.error('Couldn\'t get bitcoin price, something went wrong.')
        response_json = {"success": "false"}

    return jsonify(response_json)


@app.route('/price/<coin>', methods=['GET'])
def last_price(coin=""):

    if coin:
        data = crypto.last_price(coin)
        if data:
            logger.info('Get ' + coin + ' price: ' + str(data))
            response_json = {"success": "true", "data": data}
        else:
            logger.error('Couldn\'t get ' + coin +
                         ' price, something went wrong.')
            response_json = '{ "success": "false"}'
    else:
        logger.error('Must provide a coin.')
        response_json = {
            "success": "false",
            "msg": "Must provide a coin"
            }
    return jsonify(response_json)


@app.route('/', methods=['GET'])
@app.route('/portfolio', methods=['GET'])
def portfolio():
    portfolio = []
    coins = ['BTC', 'ETH', 'BNB', 'BAT', 'DENT', 'ENJ', 'MIOTA', 'XLM']

    for coin in coins:

        data = crypto.last_price(coin)
        if data:
            logger.info('Get ' + coin + ' price: ' + str(data))
            portfolio.append(data)
        else:
            logger.error('Couldn\'t get ' + coin +
                         ' price, something went wrong.')

    response_json = {"success": "true", "data": portfolio}
    return jsonify(response_json)


@app.route('/health', methods=['GET'])
def get_health():

    response_json = {"success": "true"}
    return jsonify(response_json)


if __name__ == '__main__':

    debug = config['flask']['debug'] == 'True'
    logger.info('DEBUG MODE: ' + str(debug))

    app.run(debug=debug)
