#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:36:04 2017

@author: chrisjackson
"""
###########################################################
#  Computer Project #1
#   Request input
#      Repeat input
#   Convert input to meters,feet,miles,furlongs, and minutes
#   Output conversions
#
###########################################################
    
#input and repeat output

input_rods=input('Input rods: ')
rods=float(input_rods)
print('You input', rods,'rods.')

#calculations

meters = rods*5.0292

feet = meters/0.3048

miles = meters/1609.34

furlongs = rods/40

minutes = (60/3.1)*miles

#Rounding

minutes = round(minutes, 3)
furlongs = round(furlongs, 3)
miles = round(miles, 3)
feet = round(feet, 3)
meters = round(meters, 3)

#Print
print('')
print('Conversions')
print('Meters:',meters)
print('Feet:',feet)
print('Miles:',miles)
print('Furlongs:',furlongs)
print('Minutes to walk',rods,'rods:',minutes)