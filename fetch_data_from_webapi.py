#!/usr/bin/env python3

import requests
import json


def fetch_temperature_and_humidity(url):
    r = requests.get(url)
    data = json.loads(r.text)
    return data['temperature'], data['humidity']


def fetch_temperature_and_humidity_test(url):
    return -273.1, 100.0


if __name__ == '__main__':
    DHT_WEB_API = 'http://10.0.0.234:8080/thermohygrometer' # DHT_WebAPI URL
    print(fetch_temperature_and_humidity(DHT_WEB_API))
