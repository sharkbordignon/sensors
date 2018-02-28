import datetime
import csv

def getFileName():
    #file name creation
    dateFile = datetime.datetime.now().date()
    hourFile = datetime.datetime.now().hour
    filename ='output_weather_{}_{}.csv'.format(str(dateFile),str(hourFile))
    return filename

def save(result):
    filename= getFileName()
    with open(filename, 'a') as csvfile:
        fieldnames = ['time', 'temperature', 'humidity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        #writer.writeheader()
        writer.writerow({'time': str(datetime.datetime.now()), 'temperature': result.temperature, 'humidity': result.humidity})


def saveDS(result):
    filename= getFileName()
    with open(filename, 'a') as csvfile:
        fieldnames = ['time', 'temperature']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        #writer.writeheader()
        writer.writerow({'time': str(datetime.datetime.now()), 'temperature_inside': result[0], 'temperature_outside': result[1]})
