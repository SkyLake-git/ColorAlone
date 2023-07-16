from PIL import Image
import pyautogui


class Parser:
	pixels: list[tuple[int, int]]

	def __init__(self, image):
		self.image = image.convert('RGB')
		self.pixels = []
		self.streak = 0

	def parse(self):
		size = self.image.size

		for x in range(size[0]):
			for y in range(size[1]):
				r, g, b = self.image.getpixel((x, y))
				if (r == 200 and g == 200 and b == 200) or (r == 142 and g == 142 and b == 142):
					if self.streak > 1:
						self.streak = 0
						print(r, g, b, x, y)
						self.pixels.append((x, y))
					else:
						self.streak += 1
				else:
					if self.streak > 0:
						self.streak -= 1
