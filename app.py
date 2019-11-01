#!/usr/bin/env python3

from flask import *
from fetch_data_from_webapi import *

DHT_WEB_API = 'http://10.0.0.234:8080/thermohygrometer' # DHT_WebAPI URL

app = Flask(__name__)


@app.route('/', methods=['GET'])
def respond():
    return render_template('main.html')


# API
@app.route('/temperature_and_humidity', methods=['GET'])
def respond_temperature_and_humidity():
    temperature, humidity = fetch_temperature_and_humidity(DHT_WEB_API)
    return jsonify({'temperature': temperature, 'humidity': humidity})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
