# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TranscriptEditorTab.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class TranscriptEditorFrame(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1169, 718)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.EditTransFrame = QtWidgets.QFrame(Form)
        self.EditTransFrame.setGeometry(QtCore.QRect(30, 20, 1500, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EditTransFrame.sizePolicy().hasHeightForWidth())
        self.EditTransFrame.setSizePolicy(sizePolicy)
        self.EditTransFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EditTransFrame.setAutoFillBackground(True)
        self.EditTransFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.EditTransFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EditTransFrame.setObjectName("EditTransFrame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.EditTransFrame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.WordSelectEnd = QtWidgets.QSpinBox(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WordSelectEnd.sizePolicy().hasHeightForWidth())
        self.WordSelectEnd.setSizePolicy(sizePolicy)
        self.WordSelectEnd.setObjectName("WordSelectEnd")
        self.gridLayout_7.addWidget(self.WordSelectEnd, 2, 1, 1, 1)
        self.ApplyShiftButton = QtWidgets.QPushButton(self.EditTransFrame)
        self.ApplyShiftButton.setObjectName("ApplyShiftButton")
        self.gridLayout_7.addWidget(self.ApplyShiftButton, 4, 1, 1, 1)
        self.DescriptionBox = QtWidgets.QTextBrowser(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DescriptionBox.sizePolicy().hasHeightForWidth())
        self.DescriptionBox.setSizePolicy(sizePolicy)
        self.DescriptionBox.setObjectName("DescriptionBox")
        self.gridLayout_7.addWidget(self.DescriptionBox, 1, 0, 4, 1)
        self.WordShiftAmount = QtWidgets.QDoubleSpinBox(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WordShiftAmount.sizePolicy().hasHeightForWidth())
        self.WordShiftAmount.setSizePolicy(sizePolicy)
        self.WordShiftAmount.setMinimum(-9999999.0)
        self.WordShiftAmount.setMaximum(9999999.0)
        self.WordShiftAmount.setObjectName("WordShiftAmount")
        self.gridLayout_7.addWidget(self.WordShiftAmount, 3, 1, 1, 1)
        self.WordSelectStart = QtWidgets.QSpinBox(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WordSelectStart.sizePolicy().hasHeightForWidth())
        self.WordSelectStart.setSizePolicy(sizePolicy)
        self.WordSelectStart.setObjectName("WordSelectStart")
        self.gridLayout_7.addWidget(self.WordSelectStart, 1, 1, 1, 1)
        self.TranscriptWordBox = QtWidgets.QTextBrowser(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TranscriptWordBox.sizePolicy().hasHeightForWidth())
        self.TranscriptWordBox.setSizePolicy(sizePolicy)
        self.TranscriptWordBox.setTabStopDistance(88.0)
        self.TranscriptWordBox.setPlaceholderText("")
        self.TranscriptWordBox.setObjectName("TranscriptWordBox")
        self.gridLayout_7.addWidget(self.TranscriptWordBox, 5, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ApplyShiftButton.setText(_translate("Form", "Apply Shift"))
        self.DescriptionBox.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
