#!/usr/bin/python

import time
import RPi.GPIO as io

def itsRaining():
    water_sensor = 22
    io.setmode(io.BCM)
    io.setup(water_sensor, io.IN)
    if io.input(water_sensor):
        print("No Rain Detected")                        
    else:
        print("Rain Detected")
    return io.input(water_sensor)
