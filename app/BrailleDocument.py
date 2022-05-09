#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import request

class BrailleDocument(object):
    def getBrailleCharacter(self):
        brailleChar = []
        try:
            braille = [request.form['char']]            
            brailleChar.append(braille)
            return brailleChar
        except:
            return brailleChar

    def saveBrailleCharacter(self):
        """@ReturnType array"""
        with open('./static/data/savedFile/BrailleFile.txt','w', encoding="utf-8") as file:
            brailleCharacter = self.getBrailleCharacter()
            for braille in brailleCharacter:
                for char in braille:
                    file.write(char)

        return "Temporarily Saved!!!"

    def __init__(self):
        self.___brailleFile = None
        """@AttributeType array"""
        self.___pageNumber = None
        self._unnamed_AmharicToBrailleTranslator_ = None
    # @AssociationType Amharic Text to Braille Translation System.AmharicToBrailleTranslator
    # @AssociationMultiplicity 1