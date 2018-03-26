from flask import Flask
import lib.ds18b20 as ds18b20
import time


app = Flask(__name__)
sensors = None

@app.route('/')
def index():
    print("READ")
    print(time.time())
    sensors_temp = []
    for sensor in sensors:
        print(time.time())
        if ds18b20.read(sensor) != None:
            sensors_temp.append(ds18b20.read(sensor)[0])
    #ds18b20.kill()
    return "Inside: " + str(sensors_temp[0]) + " || Outside: " + str(sensors_temp[1])
    #return sensors_temp
    #return "Hello, World!"

if __name__ == '__main__':
    print("INITIALIZE")
    print(time.time())
    sensors = ds18b20.sensor()
    print(time.time())
    app.run(host='0.0.0.0', port='2121')