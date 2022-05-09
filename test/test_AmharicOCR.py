import sys, os

import pytesseract

currentDir = os.path.dirname(os.path.realpath(__file__))
parentDir = os.path.dirname(currentDir)
sys.path.append(parentDir)
from app.AmharicOCR import AmharicOCR
try:
    from PIL import Image
except ImportError:
    import Image
    
img = Image.open('test/amhTest2.JPG')

def test_transform():
    transform = pytesseract.image_to_string(Image.open('test/amhTest2.JPG'), lang='amh')
    assert type(transform) is str 