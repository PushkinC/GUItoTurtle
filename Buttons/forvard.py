# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forvard.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("forvard")
        Form.resize(120, 100)
        self.forvard = QtWidgets.QGroupBox(Form)
        self.forvard.setGeometry(QtCore.QRect(10, 10, 100, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forvard.sizePolicy().hasHeightForWidth())
        self.forvard.setSizePolicy(sizePolicy)
        self.forvard.setMinimumSize(QtCore.QSize(100, 80))
        self.forvard.setStyleSheet("\n"
"background-color: rgb(115, 115, 255);")
        self.forvard.setTitle("")
        self.forvard.setObjectName("forvard")
        self.label_5 = QtWidgets.QLabel(self.forvard)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 41, 61))
        self.label_5.setStyleSheet("background-image: url(:/Forvard/v.png);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Pictures/v.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.labelForvard = QtWidgets.QLabel(self.forvard)
        self.labelForvard.setGeometry(QtCore.QRect(40, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelForvard.setFont(font)
        self.labelForvard.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.labelForvard.setAlignment(QtCore.Qt.AlignCenter)
        self.labelForvard.setObjectName("labelForvard")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelForvard.setText(_translate("Form", "10"))
