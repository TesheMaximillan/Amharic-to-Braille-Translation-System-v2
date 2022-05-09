from app.BrailleDocument import BrailleDocument
from app.AmharicDocument import AmharicDocument
from flask.helpers import send_file
from app.AmharicToBrailleTranslator import AmharicToBrailleTranslator
from app.AmharicOCR import AmharicOCR
from app.UploadDocument import UploadFile


from flask import render_template, send_from_directory

def configure_routes(app):
    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('layout/home.html')

    @app.route('/scannedDocument/<filename>')
    def sendImage(filename):
        return send_from_directory('./static/data/uploadFile', filename)

    @app.route('/scannedDocument', methods=['POST', 'GET'])
    def upload():
        imageNames = UploadFile.uploadImageFile()
        if imageNames == 'No file name':
            return render_template('layout/scannedDocument.html', imageFileError=imageNames)
        elif imageNames == 'file is not supported':
            return render_template('layout/scannedDocument.html', imageFileError=imageNames)
        elif len(imageNames) > 0:
            return render_template('layout/scannedDocument.html', imageNames = imageNames)
        else:
            return render_template('layout/scannedDocument.html')


    @app.route('/amharicDocument/<source>', methods=['GET', 'POST'])
    def amharic(source):
        if source == 'uploadFile':
            amharicOCR = AmharicOCR()
            extractedText = amharicOCR.getConvertedText()
            if extractedText != 'No Image File is Selected!!!':
                return render_template('layout/amharicDocument.html', extractedText=extractedText)
            else:
                return render_template('layout/amharicDocument.html', error=extractedText)
        elif source == 'newFile':
            return render_template('layout/amharicDocument.html', newFile=1)
        elif source == 'importFile':
            content = UploadFile.uploadTextFile()
            return render_template('layout/amharicDocument.html', importFile=content)
        else:
            return render_template('layout/home.html')


    @app.route('/brailleDocument', methods=['GET', 'POST'])
    def braille():
        amharicToBrailleTranslator = AmharicToBrailleTranslator()
        translatedFile = amharicToBrailleTranslator.translate()

        if translatedFile != "No Amharic Text is Found!!!":
            return render_template('layout/brailleDocument.html', translatedFile=translatedFile)
        else:
            return render_template('layout/brailleDocument.html', error=translatedFile)

    @app.route('/saveAmharic', methods=['GET', 'POST'])
    def saveAmharic():
        amharicDocument = AmharicDocument()
        savedFile = amharicDocument.saveAmharicText()

        return render_template('common/saveAmharic.html', message=savedFile)

    @app.route('/saveBraille', methods=['GET', 'POST'])
    def saveBraille():
        brailleDocument = BrailleDocument()
        savedFile = brailleDocument.saveBrailleCharacter()

        return render_template('common/saveBraille.html', message=savedFile)

    @app.route('/downloadBraille')
    def downloadBraille():
        return send_file('./static/data/savedFile/BrailleFile.txt', as_attachment=True)

    @app.route('/downloadAmharic')
    def downloadAmharic():
        return send_file('./static/data/savedFile/AmharicFile.txt', as_attachment=True)
