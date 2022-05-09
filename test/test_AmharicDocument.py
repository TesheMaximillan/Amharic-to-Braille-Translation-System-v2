import sys, os

currentDir = os.path.dirname(os.path.realpath(__file__))
parentDir = os.path.dirname(currentDir)
sys.path.append(parentDir)
from app.AmharicDocument import AmharicDocument

def test_getAmharicText():
    amharicDocument = AmharicDocument().getAmharicText()
    assert type(amharicDocument) is list 


def test_SaveAmharicText():
    amharicDocument = AmharicDocument().saveAmharicText()
    assert type(amharicDocument) is str 
