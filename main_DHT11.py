import RPi.GPIO as GPIO
import lib.dht11 as dht11
import time
import datetime
import saveFile
import emailWrapper

from  email.MIMEMultipart import MIMEMultipart
from  email.MIMEText import MIMEText


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=24)
hourSent = -1
while True:
    result = instance.read()
    while result.is_valid() == False:
        result = instance.read()
    if result.is_valid():
        saveFile.save(result)
        if hourSent != datetime.datetime.now().hour:
            emailWrapper.sendEmail('thiagobordignon@gmail.com', result, datetime.datetime.now())
            hourSent = datetime.datetime.now().hour

    time.sleep(60)

