from process import Parser
from PIL import Image, ImageGrab
import window
import pyautogui
import time

time.sleep(2)
for i in range(30):
	image = ImageGrab.grab()

	parser = Parser(image)

	parser.parse()
	skipped = False

	last_image = image

	for pixel in parser.pixels:
		x = pixel[0]
		y = pixel[1]
		print(pixel)

		if not skipped:
			pyautogui.moveTo((30, 200))

		r, g, b = last_image.getpixel((x, y))

		if r != 200 and g != 200 and b != 200:
			skipped = True
			continue
		else:
			skipped = False

		pyautogui.click(x, y, button='left')
		time.sleep(0.1)
		last_image = ImageGrab.grab().convert('RGB')
