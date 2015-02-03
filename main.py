#!/usr/bin/env python

from config import SENSOR_MAPPING, RELAY_MAPPING

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/get/data')
def index():
    return render_template('index.html')

class RealWorldData:
    def __init__(self):
        pass

class RealWorldIo:
    def __init__(self, real_world_data):
        pass

class DataBus:
    def __init__(self):
        pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

    data_bus = DataBus()
