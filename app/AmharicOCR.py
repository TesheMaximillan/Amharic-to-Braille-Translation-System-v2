#!/usr/bin/python
# -*- coding: UTF-8 -*-


from app.UploadDocument import TARGET_IMG
import pytesseract
import os


# PIL from pillow's which import image class to open the image
# pytesseract to detect the string in the image
try:
    from PIL import Image
except ImportError:
    import Image


class AmharicOCR(object):
    def transform(self, img):
        """
        This function will handle the core OCR processing of images
        :param img:
        :return: text
        """
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        text = pytesseract.image_to_string(Image.open(img), lang='amh')
        return text

    def getImgFile(self):
        """@ReturnType string"""
        images = os.listdir('./static/data/uploadFile')
        return images

    def getConvertedText(self):
        """@ReturnType string"""
        errorMessage = "No Image File is Selected!!!"

        if os.path.isdir('./static/data/uploadFile'):
            images = self.getImgFile()
            extractedText = []
            for img in images:
                extractedText.append(self.transform('/'.join([TARGET_IMG, img])))
            return extractedText
        else:
            return errorMessage
            
    def __init__(self):
        self.___imgFile = None
        """@AttributeType string"""
        self.___tesseract = None
        """@AttributeType string"""
        self.___convertedText = None
        """@AttributeType string"""
        self._unnamed_ScannedDocument_ = None
        # @AssociationType Amharic Text to Braille Translation System.ScannedDocument
        # @AssociationMultiplicity 1..*
        self._unnamed_AmharicDocument_ = None
    # @AssociationType Amharic Text to Braille Translation System.AmharicDocument
    # @AssociationMultiplicity 1