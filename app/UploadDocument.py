#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import shutil
from flask import request


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, "static\\data")
ALLOWED_EXTS_IMG = {'jpeg', 'jpg', 'png'}
TARGET_IMG = os.path.join(APP_ROOT, '../static/data/uploadFile')

ALLOWED_EXTS_TXT = {'txt', 'doc'}
TARGET_TXT = os.path.join(APP_ROOT, '../static/data/importFile')

def checkImgFileType(file):
    return '.' in file and file.rsplit('.', 1)[1].lower() in ALLOWED_EXTS_IMG

def checkTxtFileType(file):
    return '.' in file and file.rsplit('.', 1)[1].lower() in ALLOWED_EXTS_TXT

    

class UploadFile(object):

    def uploadImageFile():
        if os.path.isdir(TARGET_IMG):
            shutil.rmtree(TARGET_IMG)

        if not os.path.isdir(TARGET_IMG):
            os.mkdir(TARGET_IMG)

        if request.method == 'POST':
            fileNameError = 'No file name'
            fileNotSupportedError = 'file is not supported'
            for upload in request.files.getlist("file"):
                filename = upload.filename   

                # verfiy files are supported or not

                if filename == '':
                    return fileNameError
                elif not checkImgFileType(filename):
                    return fileNotSupportedError
                else:
                    destinationPath = "/".join([TARGET_IMG, filename])
                    upload.save(destinationPath)        
        return os.listdir('./static/data/uploadFile')

    def uploadTextFile():
        if os.path.isdir(TARGET_TXT):
            shutil.rmtree(TARGET_TXT)

        if not os.path.isdir(TARGET_TXT):
            os.mkdir(TARGET_TXT)

        if request.method == 'POST':
            file = request.files['file']
            filename = file.filename
            fileNameError = 'No file name'
            fileNotSupportedError = 'file is not supported'
            if filename == '':
                return fileNameError
            elif not checkTxtFileType(filename):
                return fileNotSupportedError
            else:
                destinationPath = "/".join([TARGET_TXT, filename])
                file.save(destinationPath)
                file.seek(0)
                print("File saved")
                content = file.read()
                content = str(content, 'utf-8')
                return content  

    def sendImage(self):
        pass

    def __init__(self):
        self.___uploadFolder = None
        """@AttributeType string"""
        self.___allowedExtension = None
        """@AttributeType set"""
        self.___targetFolder = None
        """@AttributeType string"""
        self.___filename = None
        """@AttributeType string"""
        self.___errorMessage = None
        """@AttributeType string"""
        self.___destinationPath = None
        """@AttributeType string"""
        self.___imageNames = None
        """@AttributeType string"""
        self._unnamed_AmharicOCR_ = None
    # @AssociationType Amharic Text to Braille Translation System.AmharicOCR
    # @AssociationMultiplicity 1