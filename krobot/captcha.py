import os,sys
from PIL import Image
import numpy

LETTER_NB = 5
LETTER_SPACE = 1
LETTER_SIZE = 8
LETTER_LEFT = 10
LETTER_RIGHT = 16

class captchaSymbolExtractor(object):
	"""docstring for captchaSymbolExtractor"""
	def __init__(self):
		super(captchaSymbolExtractor, self).__init__()

	def extractSymbol(self, filename):

		# mat_pix is a numpy array
		mat_pix = self.openImage(filename)

		list_im = []
		for i in range(5):
			left  = LETTER_LEFT + i * (LETTER_SIZE + LETTER_SPACE)
			right = LETTER_LEFT + (i + 1) * (LETTER_SIZE + LETTER_SPACE) - 1
			symb = mat_pix[6:19, left:right]
			list_im.append(symb)
			im = Image.fromarray(symb*255)
			im = im.convert('1')

		return list_im

	def openImage(self, filename):

		pil_image = Image.open(filename)
		return numpy.array(pil_image)	


class CaptchaReader(object):
	"""docstring for CaptchaReader"""
	def __init__(self, folderDico):
		super(CaptchaReader, self).__init__()
		self.folderDico = folderDico + "/"

	def read(self, filename):
		
		# Extract symbol from targetted captcha
		symb_extractor = captchaSymbolExtractor()
		listSymb = symb_extractor.extractSymbol(filename)

		cap_string = ""
		nb_unread = 0
		for symb in listSymb:
			succes = False
			for f in os.listdir(self.folderDico):
				if f.endswith(".png"):
					pil_image = Image.open(self.folderDico + f)
					dic_symb = numpy.array(pil_image)
					if self.compare(symb, dic_symb):
						succes = True
						if f[0].isdigit():
							cap_string += f[0]
						else:
							cap_string += f[3]
						break
				
			if not succes:
				# If you go there, then the symbol has not been read
				Image.fromarray(symb).save("error/symb" + str(nb_unread) + ".png")
				nb_unread += 1


		#return the string
		return cap_string

	def compare(self, symb_np, im_dic):
		
		#print symb_np
		return numpy.array_equal(symb_np, im_dic/255)