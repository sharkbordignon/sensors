import os
import time
import datetime
import saveFile
import emailWrapper
import spreadsheet

import lib.ds18b20 as ds18b20
import lib.rain as rain

hourSent = -1
if __name__ == '__main__':
    try:
        sensors = ds18b20.sensor()
        while True:
            sensors_temp = []
            i = 0
            for sensor in sensors:
                if ds18b20.read(sensor) != None:
                    sensors_temp.append(ds18b20.read(sensor)[0])
                    sensor_name = 'inside' if 1 == 0 else 'outside'
                    spreadsheet.insertRow(sensor_name, datetime.datetime.now(), ds18b20.read(sensor)[0])
                    #print sensor
                    #print "Current temperature : %0.3f C" % ds18b20.read(sensor)[0]
                    #print "Current temperature : %0.3f F" % ds18b20.read(sensor)[1]
            saveFile.saveDS(sensors_temp)
            if hourSent != datetime.datetime.now().hour:
                emailWrapper.sendEmailDS('thiagobordignon@gmail.com', sensors_temp, datetime.datetime.now(), rain.itsRaining())
                hourSent = datetime.datetime.now().hour
            time.sleep(60)
    except KeyboardInterrupt:
        ds18b20.kill()

