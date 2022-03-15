import cv2 as cv
import numpy as np
import os
import pyautogui
from pynput.keyboard import Key, Controller
import time
import mouse
import time
from pynput.keyboard import Listener


# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Can use IMREAD flags to do different pre-processing of image files,
# like making them grayscale or reducing the size.
# https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html


def find_object():
	keyboard = Controller()
	time.sleep(2)
	myScreenshot = pyautogui.screenshot()
	myScreenshot.save(r'.\FT3char.png')

	haystack_img = cv.imread('albion_farm.jpg', cv.IMREAD_UNCHANGED)
	needle_img = cv.imread('albion_cabbage.jpg', cv.IMREAD_UNCHANGED)
	# There are 6 comparison methods to choose from:
	# TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
	# You can see the differences at a glance here:
	# https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
	# Note that the values are inverted for TM_SQDIFF and TM_SQDIFF_NORMED
	result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

	# You can view the result of matchTemplate() like this:
	# cv.imshow('Result', result)
	# cv.waitKey()
	# If you want to save this result to a file, you'll need to normalize the result array
	# from 0..1 to 0..255, see:
	# https://stackoverflow.com/questions/35719480/opencv-black-image-after-matchtemplate
	# cv.imwrite('result_CCOEFF_NORMED.jpg', result * 255)

	# Get the best match position from the match result.
	min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
	# The max location will contain the upper left corner pixel position for the area
	# that most closely matches our needle image. The max value gives an indication
	# of how similar that find is to the original needle, where 1 is perfect and -1
	# is exact opposite.
	print('Best match top left position: %s' % str(max_loc))

	x = max_loc
	# If the best match value is greater than 0.8, we'll trust that we found a match
	threshold = 0.8
	if max_val >= threshold:
		print("foundit")
		time.sleep(2)
		return (x[0], x[1])
		# Get the size of the needle image. With OpenCV images, you can get the dimensions
		# via the shape property. It returns a tuple of the number of rows, columns, and
		# channels (if the image is color):
		needle_w = needle_img.shape[1]
		needle_h = needle_img.shape[0]

		# Calculate the bottom right corner of the rectangle to draw
		top_left = max_loc
		bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

		# Draw a rectangle on our screenshot to highlight where we found the needle.
		# The line color can be set as an RGB tuple
		cv.rectangle(haystack_img, top_left, bottom_right,
					 color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

		# You can view the processed screenshot like this:
		# cv.imshow('Result', haystack_img)
		# cv.waitKey()
		# Or you can save the results to a file.
		# imwrite() will smartly format our output image based on the extension we give it
		# https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce
		cv.imwrite('result.jpg', haystack_img)

	else:
		print('Needle not found.')


def enter_ft3():
	keyboard = Controller()
	time.sleep(2)
	myScreenshot = pyautogui.screenshot()
	myScreenshot.save(r'.\FT3char.png')

	haystack_img = cv.imread('albion_farm.jpg', cv.IMREAD_UNCHANGED)
	needle_img = cv.imread('albion_cabbage.jpg', cv.IMREAD_UNCHANGED)
	# There are 6 comparison methods to choose from:
	# TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
	# You can see the differences at a glance here:
	# https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
	# Note that the values are inverted for TM_SQDIFF and TM_SQDIFF_NORMED
	result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

	# You can view the result of matchTemplate() like this:
	# cv.imshow('Result', result)
	# cv.waitKey()
	# If you want to save this result to a file, you'll need to normalize the result array
	# from 0..1 to 0..255, see:
	# https://stackoverflow.com/questions/35719480/opencv-black-image-after-matchtemplate
	# cv.imwrite('result_CCOEFF_NORMED.jpg', result * 255)

	# Get the best match position from the match result.
	min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
	# The max location will contain the upper left corner pixel position for the area
	# that most closely matches our needle image. The max value gives an indication
	# of how similar that find is to the original needle, where 1 is perfect and -1
	# is exact opposite.
	print('Best match top left position: %s' % str(max_loc))

	x = max_loc
	# If the best match value is greater than 0.8, we'll trust that we found a match
	threshold = 0.8
	if max_val >= threshold:
		print("foundit")
		time.sleep(2)
		x = max_loc
		pyautogui.moveTo(x[0], x[1])
		mouse.move(-555, 0, absolute=False, duration=0.2)
		mouse.click('left')
		time.sleep(2)
		mouse.click('left')
		time.sleep(2)
		mouse.click('left')
		time.sleep(2)
		mouse.click('left')
		pyautogui.moveTo(879,475)
		mouse.click('left')
		#sellect dung
		pyautogui.moveTo(615, 764)
		mouse.click('left')
		# Get the size of the needle image. With OpenCV images, you can get the dimensions
		# via the shape property. It returns a tuple of the number of rows, columns, and
		# channels (if the image is color):
		needle_w = needle_img.shape[1]
		needle_h = needle_img.shape[0]

		# Calculate the bottom right corner of the rectangle to draw
		top_left = max_loc
		bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

		# Draw a rectangle on our screenshot to highlight where we found the needle.
		# The line color can be set as an RGB tuple
		cv.rectangle(haystack_img, top_left, bottom_right,
					 color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

		# You can view the processed screenshot like this:
		# cv.imshow('Result', haystack_img)
		# cv.waitKey()
		# Or you can save the results to a file.
		# imwrite() will smartly format our output image based on the extension we give it
		# https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce
		cv.imwrite('result.jpg', haystack_img)

	else:
		print('Needle not found.')



def exit_dung():
	keyboard = Controller()
	time.sleep(5)
	pyautogui.moveTo(1260, 1030)
	mouse.click('left')
	time.sleep(1)
	pyautogui.moveTo(1305, 631)
	mouse.click('left')
	time.sleep(1)
	pyautogui.moveTo(1550, 701)
	time.sleep(1)
	mouse.click('left')
	pyautogui.moveTo(944, 641)
	time.sleep(1)
	mouse.click('left')
	time.sleep(25)
	key = "x"
	keyboard.press(key)
	time.sleep(2)
	keyboard.release(key)
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


def send_items_back():
	keyboard = Controller()
	time.sleep(5)
	##send looted items back

def second_boss_ft3():
	keyboard = Controller()
	time.sleep(5)

	pyautogui.moveTo(1003, 50)
	mouse.click('left')
	time.sleep(3)

	pyautogui.moveTo(975, 50)
	mouse.click('left')

def inside_ft3():
	keyboard = Controller()
	time.sleep(5)
	pyautogui.moveTo(800, 800)
	time.sleep(1)

	keyboard.press('2')
	keyboard.release('2')
	mouse.click('left')
	key = "="
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(4)

	##aura
	key = "-"
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(4)

	keyboard.press('2')
	keyboard.release('2')

	key = "z"
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(0.5)
	key = "3"
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(3.5)

	keyboard.press('0')
	keyboard.release('0')
	time.sleep(0.3)
	keyboard.press('4')
	keyboard.release('4')
	time.sleep(0.3)
	keyboard.press('5')
	keyboard.release('5')
	time.sleep(0.5)

	keyboard.press('7')
	keyboard.release('7')
	time.sleep(0.3)

	time.sleep(2)

	##target boss
	key = "z"
	keyboard.press(key)
	keyboard.release(key)


	keyboard.press('6')
	keyboard.release('6')
	keyboard.press('9')
	keyboard.release('9')
	time.sleep(3.7)
	key = "3"
	keyboard.press(key)
	keyboard.release(key)

	keyboard.press("2")
	keyboard.release("2")
	time.sleep(99)
	keyboard.press('9')
	keyboard.release('9')
	keyboard.press("8")
	keyboard.release("8")
	time.sleep(13)
	#redo Bm2
	key = "="

	keyboard.press(key)
	keyboard.release(key)
	time.sleep(3)
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(6)

	##aura
	key = "-"
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(2.9)
	##target boss
	key = "z"
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(0.5)
	key = "3"
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(63)
	key = "z"
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(0.5)
	key = "3"
	keyboard.press(key)
	keyboard.release(key)
##looting
	key = "v"
	keyboard.press("2")
	keyboard.release("2")
	time.sleep(3)
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(0.3)
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(0.3)
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(0.3)
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(0.3)
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(5)




def do_FT3():
	##Navigate to Map
	keyboard = Controller()

	keyboard.press('2')
	keyboard.release('2')

	keyboard.press(Key.alt)
	keyboard.press('3')
	keyboard.release('3')
	keyboard.release(Key.alt)


	key = "m"
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(2)
	myScreenshot = pyautogui.screenshot()
	myScreenshot.save(r'.\albion_farm.jpg')

	haystack_img = cv.imread('albion_farm.jpg', cv.IMREAD_UNCHANGED)
	needle_img = cv.imread('albion_cabbage.jpg', cv.IMREAD_UNCHANGED)
	# There are 6 comparison methods to choose from:
	# TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
	# You can see the differences at a glance here:
	# https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
	# Note that the values are inverted for TM_SQDIFF and TM_SQDIFF_NORMED
	result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
	
	# You can view the result of matchTemplate() like this:
	#cv.imshow('Result', result)
	#cv.waitKey()
	# If you want to save this result to a file, you'll need to normalize the result array
	# from 0..1 to 0..255, see:
	# https://stackoverflow.com/questions/35719480/opencv-black-image-after-matchtemplate
	#cv.imwrite('result_CCOEFF_NORMED.jpg', result * 255)

	# Get the best match position from the match result.
	min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
	# The max location will contain the upper left corner pixel position for the area
	# that most closely matches our needle image. The max value gives an indication
	# of how similar that find is to the original needle, where 1 is perfect and -1
	# is exact opposite.
	print('Best match top left position: %s' % str(max_loc))
	
	x=max_loc
	pyautogui.moveTo(x[0] , x[1] )
	mouse.move(25, 25, absolute=False, duration=0.2)
	mouse.click('left')
	mouse.move(-155, 0, absolute=False, duration=0.2)
	mouse.click('left')
	print('Best match confidence: %s' % max_val)

	# If the best match value is greater than 0.8, we'll trust that we found a match
	threshold = 0.8
	if max_val >= threshold:
	    print('Found needle.')

	    # Get the size of the needle image. With OpenCV images, you can get the dimensions 
	    # via the shape property. It returns a tuple of the number of rows, columns, and 
	    # channels (if the image is color):
	    needle_w = needle_img.shape[1]
	    needle_h = needle_img.shape[0]

	    # Calculate the bottom right corner of the rectangle to draw
	    top_left = max_loc
	    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

	    # Draw a rectangle on our screenshot to highlight where we found the needle.
	    # The line color can be set as an RGB tuple
	    cv.rectangle(haystack_img, top_left, bottom_right, 
                    color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

	    # You can view the processed screenshot like this:
	    #cv.imshow('Result', haystack_img)
	    #cv.waitKey()
	    # Or you can save the results to a file.
	    # imwrite() will smartly format our output image based on the extension we give it
	    # https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce
	    cv.imwrite('result.jpg', haystack_img)

	else:
	    print('Needle not found.')



#second_boss_ft3()
# Collect events until released
answer = input("Do You want to Listen for Keys: y/n")
print("Ansered: " + answer)
if(answer=='y'):
	with Listener(
			on_press=on_press,
			on_release=on_release) as listener:
		listener.join()

max_runs=9
time.sleep(3)
cur_run=0
time.sleep(4)
while(cur_run<max_runs):
	keyboard = Controller()
	keyboard.press(Key.f2)
	keyboard.release(Key.f2)
	cur_run=cur_run+1
	do_FT3()
	enter_ft3()
	inside_ft3()
	exit_dung()