# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untdditled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_l2(object):
    def setupUi(self, l2):
        l2.setObjectName("l2")
        l2.resize(552, 470)
        self.e1 = QtWidgets.QTextEdit(l2)
        self.e1.setGeometry(QtCore.QRect(10, 50, 531, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.e1.setFont(font)
        self.e1.setObjectName("e1")
        self.horizontalLayoutWidget = QtWidgets.QWidget(l2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.r1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.r1.setChecked(True)
        self.r1.setObjectName("r1")
        self.horizontalLayout.addWidget(self.r1)
        self.r2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.r2.setObjectName("r2")
        self.horizontalLayout.addWidget(self.r2)
        self.r3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.r3.setObjectName("r3")
        self.horizontalLayout.addWidget(self.r3)
        self.f = QtWidgets.QLineEdit(l2)
        self.f.setGeometry(QtCore.QRect(340, 10, 191, 31))
        self.f.setObjectName("f")
        self.label_2 = QtWidgets.QLabel(l2)
        self.label_2.setGeometry(QtCore.QRect(250, 9, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn4 = QtWidgets.QPushButton(l2)
        self.btn4.setGeometry(QtCore.QRect(460, 420, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.label = QtWidgets.QLabel(l2)
        self.label.setGeometry(QtCore.QRect(20, 420, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(l2)
        self.splitter.setGeometry(QtCore.QRect(10, 280, 531, 131))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.btn1 = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn3 = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn2 = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn1.raise_()
        self.e1.raise_()
        self.horizontalLayoutWidget.raise_()
        self.r2.raise_()
        self.f.raise_()
        self.label_2.raise_()
        self.btn2.raise_()
        self.btn3.raise_()
        self.btn4.raise_()
        self.label.raise_()

        self.retranslateUi(l2)
        QtCore.QMetaObject.connectSlotsByName(l2)

    def retranslateUi(self, l2):
        _translate = QtCore.QCoreApplication.translate
        l2.setWindowTitle(_translate("l2", "text to mp3"))
        self.e1.setPlaceholderText(_translate("l2", "Enter the text here"))
        self.r1.setText(_translate("l2", "AR"))
        self.r2.setText(_translate("l2", "EN"))
        self.r3.setText(_translate("l2", "FR"))
        self.f.setPlaceholderText(_translate("l2", "Ex:nameFile.mp3"))
        self.label_2.setText(_translate("l2", "  File name:"))
        self.btn4.setText(_translate("l2", "CLOSE"))
        self.label.setText(_translate("l2", "  by: BELLAHNA Boubker \"bbellahna@gmail.com\""))
        self.btn1.setText(_translate("l2", "SAVE MP3"))
        self.btn3.setText(_translate("l2", "PLAY"))
        self.btn2.setText(_translate("l2", "CLEAR"))

