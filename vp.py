# vp.py
# Raunak Anand
# ECS 36A Winter Quarter
# a program that asks the user for the temperature t
# in degrees Celsius
# then displays the estimated vapor pressure of water vapor
# in millibars at that temperature

import math # allows us to use the math module 

def approx(): # function to calculate approximation
    # user input
    temp = input("Enter temperature in degrees C: ")
    try:
        temp = float(temp)
        # vapor pressure formula
        vapor_pressure = 6.112*(math.exp((17.67*temp)/(temp+243.5)))
        # vapor pressure to two decimal places
        vp = '{0:.2f}'.format(vapor_pressure)
        print("At this tenperature, the vapor pressure is approximately",vp,"miligrams")
    
    except:
        print("Please enter an integer!")

approx()
