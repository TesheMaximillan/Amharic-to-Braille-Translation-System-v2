#!/usr/bin/python
# -*- coding: UTF-8 -*-


from app.AmharicDocument import AmharicDocument
from static.data.dictionary import Dictionary



class AmharicToBrailleTranslator(object):
    def translate(self):
        errorMessage = "No Amharic Text is Found!!!"
        amharicDocument = AmharicDocument()
        amharicFile = amharicDocument.getAmharicText()


        try:
            brailleFile = []
            for amharicTextInPage in amharicFile:
                brailleCharactersInPage = []
                for text in amharicTextInPage:
                    brailleCharacters = []
                    for char in text:
                        brailleCharacters.append(Dictionary.get(char, ''))
                    brailleCharactersInPage.append(''.join(brailleCharacters))
                brailleFile.append(brailleCharactersInPage)


            return brailleFile
        except:
            return errorMessage
            
    def setBrailleFile(self, aBrailleFile):
        """@ParamType aBrailleFile array
		@ReturnType void"""
        self.___brailleFile = aBrailleFile

    def setUnnamed_AmharicDocument_(self, aUnnamed_AmharicDocument_):
        """@ParamType aUnnamed_AmharicDocument_ Amharic Text to Braille Translation System.AmharicDocument
		@ReturnType void"""
        self._unnamed_AmharicDocument_ = aUnnamed_AmharicDocument_

    def getUnnamed_AmharicDocument_(self):
        """@ReturnType Amharic Text to Braille Translation System.AmharicDocument"""
        return self._unnamed_AmharicDocument_

    def setUnnamed_BrailleDocument_(self, aUnnamed_BrailleDocument_):
        """@ParamType aUnnamed_BrailleDocument_ Amharic Text to Braille Translation System.BrailleDocument
		@ReturnType void"""
        self._unnamed_BrailleDocument_ = aUnnamed_BrailleDocument_

    def getUnnamed_BrailleDocument_(self):
        """@ReturnType Amharic Text to Braille Translation System.BrailleDocument"""
        return self._unnamed_BrailleDocument_

    def __init__(self):
        self.___amharicText = None
        """@AttributeType string"""
        self.___brailleCharacter = None
        """@AttributeType array"""
        self.___errorMessage = None
        """@AttributeType string"""
        self.___brailleFile = None
        """@AttributeType array"""
        self.___amharicCharacter = None
        """@AttributeType char"""
        self._unnamed_AmharicDocument_ = None
        # @AssociationType Amharic Text to Braille Translation System.AmharicDocument
        # @AssociationMultiplicity 1
        self._unnamed_BrailleDocument_ = None
    # @AssociationType Amharic Text to Braille Translation System.BrailleDocument
    # @AssociationMultiplicity 1