import os,sys
from PIL import Image
import numpy

website = "http://reservation.crous-lille.fr:82/index.php"
LETTER_NB = 5
LETTER_SPACE = 1
LETTER_SIZE = 8
LETTER_LEFT = 10
LETTER_RIGHT = 16

class CapchkaLetterExtractor(object):
	"""docstring for CapchkaLetterExtractor"""

	def __init__(self):
		super(CapchkaLetterExtractor, self).__init__()

	def process(self, filename):
		
		capfile = Image.open(filename)
		mat_pix = self.openImage(capfile)
		list_symb = self.extractSymbol(mat_pix)

		#for i in range(len(list_symb)):
		#	self.save(capfile.copy(), list_symb[i], str(i))

	def openImage(self, pil_image):
		
		return numpy.array(pil_image)

	def extractSymbol(self, mat_pix):

		list_im = []
		for i in range(5):
			left  = LETTER_LEFT + i * (LETTER_SIZE + LETTER_SPACE)
			right = LETTER_LEFT + (i + 1) * (LETTER_SIZE + LETTER_SPACE) - 1
			symb = mat_pix[6:19, left:right]
			list_im.append(symb*255)
			im = Image.fromarray(symb*255, mode='P').convert('L')

			im.save("cap/zz" + str(i) + ".png")
			#print numpy.dot(numpy.transpose(symb), symb)

		return list_im

	def save(self, copyIm, numpyImg, name):
		copyIm = copyIm.resize(numpyImg.shape)
		for i in range(numpyImg.shape[0]):
			for j in range(numpyImg.shape[1]):
				copyIm.putpixel((i, j), numpyImg[i, j])

		copyIm.save('cap/' + name + '.png')
		#print copyIm.mode

# L O 0


ce = CapchkaLetterExtractor()
ce.process("cap/cap.php-5.png")
