import os,sys
from PIL import Image
import numpy

website = "http://reservation.crous-lille.fr:82/index.php"
LETTER_NB = 5
LETTER_SPACE = 1
LETTER_SIZE = 8
LETTER_LEFT = 10
LETTER_RIGHT = 16

class CreditExtractor(object):
	"""docstring for CreditExtractor"""

	def __init__(self):
		super(CreditExtractor, self).__init__()

	def process(self):
		
		capfile = Image.open("cap/cap.php-1.png")
		mat_pix = self.openImage(capfile)
		self.extractSymbol(mat_pix)

		capfile.save("cap/00.png")

	def openImage(self, pil_image):
		
		return numpy.array(pil_image)

	def extractSymbol(self, mat_pix):

		list_im = []
		for i in range(5):
			left  = LETTER_LEFT + i * (LETTER_SIZE + LETTER_SPACE)
			right = LETTER_LEFT + (i + 1) * (LETTER_SIZE + LETTER_SPACE) - 1
			symb = mat_pix[6:19, left:right]
			list_im.append(symb)
			im = Image.fromarray(symb*255)
			im = im.convert('1')

			im.save("cap/" + str(i) + ".PNG")
			print numpy.dot(numpy.transpose(symb), symb)

		return list_im


ce = CreditExtractor()
ce.process()

im = Image.open("cap/e.png")
print numpy.array(im)