#!/usr/bin/env python
'''
Serial device to keyboard press 
Nick McComb | www.nickmccomb.net
Written October 2016 originally for OSURC

Serial port to keyboard press.

Linux Prereq:
sudo pip install python-Xlib
sudo apt-get install python-tk
sudo pip install PyAutoGui
pip install pyserial

pyserial

Windows Prereq:
pip install Image
Download autopygui from github https://github.com/asweigart/pyautogui
Run python setup.py install on extracted folder
pip install pyserial
  
'''

import pyautogui
import time
import serial
import sys

if len(sys.argv) < 2:
  print "Use command like args, plz."
  quit()

serialPath = sys.argv[1]
print "Opening: " + serialPath
ser = serial.Serial(serialPath)

while 1:
  if(ser.inWaiting()):
    byte = ser.read()
    pyautogui.press(byte)
  #time.sleep(.002)
  #print "checking"
  #time.sleep(1)
  #print("pressing keyboard!");
  #pyautogui.press('l')
