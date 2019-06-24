# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 16:14:40 2019

@author: boubker BELLAHNA "bbellahna@gmail.com"
"""
import matplotlib.pyplot as plt
import sys
from PyQt5 import QtWidgets
from windomain import Ui_l2
from gtts import gTTS
import os
from PyQt5.QtWidgets import QMessageBox

class main(QtWidgets.QWidget, Ui_l2):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.btn1.clicked.connect(self.aff1)
        self.btn2.clicked.connect(self.deltte)
        self.btn3.clicked.connect(self.play)
        self.btn4.clicked.connect(self.closeEvent)

    def play(self):
        self.aff1()
        os.system('mp3file.mp3')

    def aff1(self):
        #self.check()
        self.mytext = self.e1.toPlainText()
        if self.r1.isChecked():
            tts = gTTS(self.mytext, lang='ar')
            tts.save('mp3file.mp3')

        elif self.r2.isChecked():
            tts = gTTS(self.mytext, lang='en')
            tts.save('mp3file.mp3')
        else:
            tts = gTTS(self.mytext, lang='fr')
            tts.save('mp3file.mp3')



    def deltte(self):
        self.e1.clear()
    def check(self):
        pass
    def closeEvent(self, event):

        reply =  QtWidgets.QMessageBox.question(self, "Message","Are you sure you want to quit txt2mp3?",
            QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            app.quit()
        elif reply == QtWidgets.QMessageBox.No:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = main()
    mainWindow.show()

    sys.exit(app.exec_())





