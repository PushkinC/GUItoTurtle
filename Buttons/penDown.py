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
        Form.setObjectName("Form")
        Form.resize(120, 100)
        self.penDown = QtWidgets.QWidget(Form)
        self.penDown.setGeometry(QtCore.QRect(35, 10, 46, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.penDown.sizePolicy().hasHeightForWidth())
        self.penDown.setSizePolicy(sizePolicy)
        self.penDown.setMinimumSize(QtCore.QSize(51, 80))
        self.penDown.setStyleSheet("background-color: rgb(142, 255, 116);")
        self.penDown.setObjectName("penDown")
        self.label_8 = QtWidgets.QLabel(self.penDown)
        self.label_8.setGeometry(QtCore.QRect(5, 10, 41, 61))
        self.label_8.setStyleSheet("background-image: url(:/Forvard/v.png);")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("Pictures/penDown.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
