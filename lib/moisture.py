import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

channel = 22

GPIO.setup(channel, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


while True:
    if GPIO.input(channel)==False:
        print('Soil is moist')     # Uncomment to print console commands
        time.sleep(900)             # Sleep for 15 minutes (900 seconds)
    else:
        print('Soil is dry!')      # Uncomment to print console commands
        #postToSlack()               # Trigger the Slack webhook notification
        time.sleep(2700)            # Sleep for 45 minutes (2700 seconds)
