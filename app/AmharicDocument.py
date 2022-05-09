#!/usr/bin/python
# -*- coding: UTF-8 -*-
from app.AmharicOCR import AmharicOCR
from flask.globals import request



class AmharicDocument(object):
    def getAmharicText(self):
        """@ReturnType string"""
        amharicFiles = []
        page = 1
        try:
            if request.form['text']:
                amharicText = [request.form['text']]
                if len(amharicText[0]) > 0:
                    amharicFiles.append(amharicText)
                    return amharicFiles

            if request.form['error']:
                return amharicFiles            
        except:
            try:
                amharicOcr = AmharicOCR()
                totalFiles = amharicOcr.getImgFile()
                for file in totalFiles:
                    amharicTextInPage = [request.form['text' + str(page)]]
                    amharicFiles.append(amharicTextInPage)
                    page = page + 1
                
                return amharicFiles
            except:
                return amharicFiles


    def saveAmharicText(self):
        """@ParamType aAmharicText string
		@ReturnType void"""
        with open('./static/data/savedFile/AmharicFile.txt','w', encoding="utf-8") as file:
            amharicFile = self.getAmharicText()
            for amharicTextInPage in amharicFile:
                for text in amharicTextInPage:
                    file.write(text)

        return "Temporarily Saved!!!"



    def __init__(self):
        self.___errorMessage = None
        """@AttributeType string"""
        self.___sourceFolder = None
        """@AttributeType string"""
        self.___fileExtension = None
        """@AttributeType string"""
        self.___imageNames = None
        """@AttributeType string"""
        self.___pageNumber = None
        """@AttributeType string"""
        self._unnamed_AmharicOCR_ = []
        # @AssociationType Amharic Text to Braille Translation System.AmharicOCR[]
        # @AssociationMultiplicity 1..*
        self._unnamed_AmharicToBrailleTranslator_ = None
    # @AssociationType Amharic Text to Braille Translation System.AmharicToBrailleTranslator
    # @AssociationMultiplicity 1