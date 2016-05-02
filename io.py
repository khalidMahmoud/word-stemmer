__author__ = 'khalid'
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot

#Start GUI declarations
app = QApplication(sys.argv)
w = QWidget()
btn = QPushButton("Steam", w)
label1 = QLabel(w)
resultLabel = QLabel(w)
result = QLabel(w)
#Start mainTarget declarations
#word starts with any of these prefixes.
prefixes = ['contra', 'hetero', 'circum', 'hyper',  'extra', 'inter', 'trans', 'super', 'intra', 'macro', 'micro', 'mono'
            , 'anti', 'post', 'ante', 'omni', 'homo', 'auto', 'com','sub', 'syn', 'con', 'dis', 'uni', 'tri', 'non', 'pre'
            , 'pro', 'de', 'en', 'ex', 'il', 'im', 'in', 'ir', 'co', 'un', 'an', 'eco']
#word ends with any of these suffixes.
suffixes = ['ination', 'able', 'ation', 'ible', 'ing', 'al', 'ial', 'ed', 'en', 'er', 'or', 'est', 'ful', 'ic', 'ion', 'tion',
            'ition', 'ity', 'ty', 'ive', 'ative', 'itive', 'less', 'ly', 'ment', 'ness', 'ous', 'eous', 'ious', 'ies',
            'es', 'um', 's']
#other words will not be streamed
otherWords = ['computer', 'increment', 'table', 'multiply', 'ear', 'string']

#Window handling
w.resize(320, 200)
w.setWindowTitle("Steaming")
#steam button handling
btn.setToolTip("Steam")
btn.resize(btn.sizeHint())
btn.move(110, 100)
#input textBox handling
textBox = QLineEdit(w)
textBox.move(60, 50)
textBox.resize(200, 40)
#Enteryour word label
label1.setText("Enter your word")
label1.move(100, 25)
#result label
resultLabel.setText("Result: ")
resultLabel.move(100, 140)
result.move(150, 140)
result.resize(100, 20)
#start Delete prefix
def deletePrefix(word):
    for pref in prefixes:
        if word.startswith(pref):
            word = word.replace(pref, "")
    return word
#end Delete prefix
#start deletesuffixes
def deleteSuffix(word):
    for suff in suffixes:
        if word.endswith(suff):
            if suff in "ies":
                word2 = word.replace ('ies', 'y')  #hoppies , movies will give error string
                return word2
            elif suff in "ation":
                word3 = word.replace('ation', 'e') #Organization
                return word3
            else:
                word = word.replace(suff, "")
    return word
#end deletesuffixes
#end deletesuffixes
@pyqtSlot()
def on_click():
    commingWord = str(textBox.text())
    if commingWord in otherWords:
        result.setText(commingWord)
    else:
        commingWord = deletePrefix(commingWord)
        commingWord = deleteSuffix(commingWord)
        result.setText(commingWord)
btn.clicked.connect(on_click)
w.show()
sys.exit(app.exec_())