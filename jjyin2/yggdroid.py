import numpy as np
import pyautogui
from pyautogui import typewrite
import imutils
import cv2
import pytesseract
WINDOW_POSITION = (0,0)
WINDOW_SIZE = (1280,640)
FULL_SCREEN = (1835,1040)
HEADER_HEIGHT = 30
character = {
	'frey':(64,290),
	'lorraine':(120,290),
	'miruru':(170,290),
	'clause':(64,350)
}

"""
Before running, resize window to 
1280 by 720+30
640 by 360
"""
def help():
	pass
def init():
	pass
def start_nox():
	pass
def position_nox():
	pass
def start_kr():
	pass
	
def screenshot(bw=True):
	image = pyautogui.screenshot()
	if bw:
		return cv2.cvtColor(np.array(image),cv2.COLOR_RGB2GRAY)
	return cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
	
def click(x, y):
	x, y = rescale((x,y))
	pyautogui.moveTo(x,y,.5, pyautogui.easeInQuad)
	pyautogui.click()
def rescale(pos):
	x, y= pos
	x = int(WINDOW_SIZE[0]/640*x)
	y = int(WINDOW_SIZE[1]/360*(y-30)+30)
	return (x,y)
def focus_textbox():
	click(320, 360)
def confirm_input():
	click(622,360)

def chat(message):
	click(280,350)
	typewrite(message, interval = .05)
	confirm_input()

def grab_box(topleft, bottomright):
	#topleft = rescale(topleft)
	#bottomright = rescale(bottomright)
	image = screenshot()
	return image[topleft[1]:bottomright[1],topleft[0]:bottomright[0]]
	
def scan_chat():
	#image = grab_box((289,320),(410,333))
	image = grab_box((855,852),(1190,885))
	cv2.imwrite('output.png',image)
	image = preprocess(image)
	text = pytesseract.image_to_string(image).lower()
	print(text)
	if len(text) > 3 and text[:3] == "ygg":
		handle_input(text[4:].strip())
	
def sell(input):
	click(65,250)
	click(550,340)
	click(370,340)
	click(385,335)
	click(380,295)
	click(400,40)
	
def handle_input(input):
	if input in commands.keys():
		commands[input](input)
	else:
		chat("Invalid command: "+input)
	
def invert(image):
	_, thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
	return thresh
	
def toggle_char(char):
	click(*character[char])
commands = {
	'frey': toggle_char,
	'lorraine': toggle_char,
	'miruru': toggle_char,
	'clause': toggle_char,
	'help': help,
	'sell': sell
}
def preprocess(image):
	image = invert(image)
	return cv2.medianBlur(image, 3)
def log_position():
	print('Press Ctrl-C to quit.')
	try:
		while True:
			x, y = pyautogui.position()
			positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
			print(positionStr, end='')
			print('\b' * len(positionStr), end='', flush=True)
	except KeyboardInterrupt:
		print('\n')

WINDOW_SIZE = FULL_SCREEN
#click(100,100)
#focus_textbox()
#chat('Hello world')
scan_chat()
log_position()