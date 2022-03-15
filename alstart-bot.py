import cv2 as cv
import numpy as np
import os
import pyautogui
from pynput.keyboard import Key, Controller
import time
import mouse
import time
from pynput.keyboard import Listener

import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('Jir Productions Present', font='starwars'),
       'red', 'on_black', attrs=['bold'])


# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Can use IMREAD flags to do different pre-processing of image files,
# like making them grayscale or reducing the size.
# https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html

##Listen for Keys
def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False



# Collect events until released
answer = input("Do You want to Listen for Keys: y/n")
print("Ansered: " + answer)
if(answer=='y'):
	with Listener(
			on_press=on_press,
			on_release=on_release) as listener:
		listener.join()
