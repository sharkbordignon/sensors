from flask import Flask
import lib.ds18b20 as ds18b20

app = Flask(__name__)

@app.route('/')
def index():
    sensors = ds18b20.sensor()
    sensors_temp = []
    for sensor in sensors:
        if ds18b20.read(sensor) != None:
            sensors_temp.append(ds18b20.read(sensor)[0])
    ds18b20.kill()
    return sensors_temp
    #return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='2121')
