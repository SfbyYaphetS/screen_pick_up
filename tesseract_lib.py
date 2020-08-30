import numpy as np
import pyscreenshot as ImageGrab
import pytesseract


class read_text():
    def __init__(self, coor=None):
        self.coor = coor
        pass

    def tes_read(self):
        screen = np.array(ImageGrab.grab(bbox=self.coor))
        path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.pytesseract.tesseract_cmd = path
        text = pytesseract.pytesseract.image_to_string(screen, lang="eng")
        return text
