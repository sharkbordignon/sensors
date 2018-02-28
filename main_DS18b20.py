import os
import time
import datetime
import saveFile
import emailWrapper

def sensor():
    sensors = []
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            sensors.append(i)
          
    print sensors
    return sensors
 
def read(sensor):
    location = '/sys/bus/w1/devices/' + sensor + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit

hourSent = -1
if __name__ == '__main__':
    try:
        sensors = sensor()
        while True:
            sensors_temp = []
            for sensor in sensors:
                if read(sensor) != None:
                    sensors_temp.append(read(sensor)[0])
                    print sensor
                    print "Current temperature : %0.3f C" % read(sensor)[0]
                    #print "Current temperature : %0.3f F" % read(sensor)[1]
            saveFile.saveDS(sensors_temp)
            if hourSent != datetime.datetime.now().hour:
                emailWrapper.sendEmailDS('thiagobordignon@gmail.com', sensors_temp, datetime.datetime.now())
                hourSent = datetime.datetime.now().hour
            time.sleep(60)
    except KeyboardInterrupt:
        kill()
       

