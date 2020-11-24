# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
# Uncomment this line before running, it breaks sphinx-gallery builds
# from PyQt5 import QtCore, QtWidgets

import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from scipy import signal
import math
import copy

from TranscriptPlotTab import TranscriptPlotFrame   
from TranscriptEditorTab import TranscriptEditorFrame
from Render import Transcript, RenderSettings
from DSP import stft, FormatAxis, sound, normalize


class Ui_TranscriptEditor(QMainWindow):
    def setupUi(self, TranscriptEditor):
        TranscriptEditor.setObjectName("TranscriptEditor")
        TranscriptEditor.resize(1285, 853)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TranscriptEditor.sizePolicy().hasHeightForWidth())
        TranscriptEditor.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(TranscriptEditor)
        self.gridLayout.setObjectName("gridLayout")
        self.TabWidget = QtWidgets.QTabWidget(TranscriptEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabWidget.sizePolicy().hasHeightForWidth())
        self.TabWidget.setSizePolicy(sizePolicy)
        self.TabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.TabWidget.setAutoFillBackground(True)
        self.TabWidget.setObjectName("TabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OriginalChannelTabs = QtWidgets.QTabWidget(self.tab1)
        self.OriginalChannelTabs.setObjectName("OriginalChannelTabs")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.OldTransFrame = QtWidgets.QFrame(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OldTransFrame.sizePolicy().hasHeightForWidth())
        self.OldTransFrame.setSizePolicy(sizePolicy)
        self.OldTransFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.OldTransFrame.setAutoFillBackground(True)
        self.OldTransFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.OldTransFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OldTransFrame.setObjectName("OldTransFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.OldTransFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.oldwords = QtWidgets.QTextEdit(self.OldTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldwords.sizePolicy().hasHeightForWidth())
        self.oldwords.setSizePolicy(sizePolicy)
        self.oldwords.setObjectName("oldwords")
        self.gridLayout_3.addWidget(self.oldwords, 0, 0, 1, 2)
        self.OldSpecScrollBar = QtWidgets.QScrollBar(self.OldTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OldSpecScrollBar.sizePolicy().hasHeightForWidth())
        self.OldSpecScrollBar.setSizePolicy(sizePolicy)
        self.OldSpecScrollBar.setMaximumSize(QtCore.QSize(16777215, 200))
        self.OldSpecScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.OldSpecScrollBar.setObjectName("OldSpecScrollBar")
        self.gridLayout_3.addWidget(self.OldSpecScrollBar, 2, 0, 1, 2)
        self.oldspec_plot = QtWidgets.QWidget(self.OldTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldspec_plot.sizePolicy().hasHeightForWidth())
        self.oldspec_plot.setSizePolicy(sizePolicy)
        self.oldspec_plot.setObjectName("oldspec_plot")
        self.gridLayout_3.addWidget(self.oldspec_plot, 1, 0, 1, 2)
        self.gridLayout_8.addWidget(self.OldTransFrame, 0, 0, 1, 1)
        self.OriginalChannelTabs.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.OriginalChannelTabs, 0, 0, 1, 1)
        self.TabWidget.addTab(self.tab1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.EditTransFrame = QtWidgets.QFrame(self.frame_2)
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
        self.TranscriptWordBox = QtWidgets.QTextBrowser(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TranscriptWordBox.sizePolicy().hasHeightForWidth())
        self.TranscriptWordBox.setSizePolicy(sizePolicy)
        self.TranscriptWordBox.setTabStopDistance(88.0)
        self.TranscriptWordBox.setPlaceholderText("")
        self.TranscriptWordBox.setObjectName("TranscriptWordBox")
        self.gridLayout_7.addWidget(self.TranscriptWordBox, 8, 0, 1, 2)
        self.ShiftAsTimestampButton = QtWidgets.QCheckBox(self.EditTransFrame)
        self.ShiftAsTimestampButton.setObjectName("ShiftAsTimestampButton")
        self.gridLayout_7.addWidget(self.ShiftAsTimestampButton, 5, 1, 1, 1)
        self.DoOverlapButton = QtWidgets.QCheckBox(self.EditTransFrame)
        self.DoOverlapButton.setObjectName("DoOverlapButton")
        self.gridLayout_7.addWidget(self.DoOverlapButton, 4, 1, 1, 1)
        self.WordSelectStart = QtWidgets.QSpinBox(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WordSelectStart.sizePolicy().hasHeightForWidth())
        self.WordSelectStart.setSizePolicy(sizePolicy)
        self.WordSelectStart.setObjectName("WordSelectStart")
        self.gridLayout_7.addWidget(self.WordSelectStart, 1, 1, 1, 1)
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
        self.gridLayout_7.addWidget(self.ApplyShiftButton, 6, 1, 1, 1)
        self.ChannelSelectBox = QtWidgets.QSpinBox(self.EditTransFrame)
        self.ChannelSelectBox.setMaximum(0)
        self.ChannelSelectBox.setObjectName("ChannelSelectBox")
        self.gridLayout_7.addWidget(self.ChannelSelectBox, 0, 1, 1, 1)
        self.DescriptionBox = QtWidgets.QTextBrowser(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DescriptionBox.sizePolicy().hasHeightForWidth())
        self.DescriptionBox.setSizePolicy(sizePolicy)
        self.DescriptionBox.setObjectName("DescriptionBox")
        self.gridLayout_7.addWidget(self.DescriptionBox, 0, 0, 8, 1)
        self.RenderButton = QtWidgets.QPushButton(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RenderButton.sizePolicy().hasHeightForWidth())
        self.RenderButton.setSizePolicy(sizePolicy)
        self.RenderButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.RenderButton.setIconSize(QtCore.QSize(18, 18))
        self.RenderButton.setObjectName("RenderButton")
        self.gridLayout_7.addWidget(self.RenderButton, 7, 1, 1, 1)
        self.gridLayout_9.addWidget(self.EditTransFrame, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_2, 1, 0, 1, 1)
        self.TabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.RenderSettingsFrame = QtWidgets.QFrame(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RenderSettingsFrame.sizePolicy().hasHeightForWidth())
        self.RenderSettingsFrame.setSizePolicy(sizePolicy)
        self.RenderSettingsFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RenderSettingsFrame.setAutoFillBackground(True)
        self.RenderSettingsFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.RenderSettingsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RenderSettingsFrame.setObjectName("RenderSettingsFrame")
        self.PauseShorteningFrame = QtWidgets.QFrame(self.RenderSettingsFrame)
        self.PauseShorteningFrame.setGeometry(QtCore.QRect(12, 12, 341, 131))
        self.PauseShorteningFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PauseShorteningFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PauseShorteningFrame.setObjectName("PauseShorteningFrame")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.PauseShorteningFrame)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.PauseShorteningText = QtWidgets.QTextEdit(self.PauseShorteningFrame)
        self.PauseShorteningText.setObjectName("PauseShorteningText")
        self.gridLayout_10.addWidget(self.PauseShorteningText, 0, 0, 1, 1)
        self.PauseShorteningButton = QtWidgets.QRadioButton(self.PauseShorteningFrame)
        self.PauseShorteningButton.setChecked(False)
        self.PauseShorteningButton.setObjectName("PauseShorteningButton")
        self.gridLayout_10.addWidget(self.PauseShorteningButton, 1, 0, 1, 1)
        self.PauseShortenAmountBox = QtWidgets.QDoubleSpinBox(self.PauseShorteningFrame)
        self.PauseShortenAmountBox.setObjectName("PauseShortenAmountBox")
        self.gridLayout_10.addWidget(self.PauseShortenAmountBox, 2, 0, 1, 1)
        self.BackgrundNoiseFillFrame = QtWidgets.QFrame(self.RenderSettingsFrame)
        self.BackgrundNoiseFillFrame.setGeometry(QtCore.QRect(360, 10, 241, 121))
        self.BackgrundNoiseFillFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackgrundNoiseFillFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackgrundNoiseFillFrame.setObjectName("BackgrundNoiseFillFrame")
        self.BackGroundNoiseFillerText = QtWidgets.QTextEdit(self.BackgrundNoiseFillFrame)
        self.BackGroundNoiseFillerText.setGeometry(QtCore.QRect(10, 20, 191, 31))
        self.BackGroundNoiseFillerText.setObjectName("BackGroundNoiseFillerText")
        self.BackgroundNoiseFillButton = QtWidgets.QRadioButton(self.BackgrundNoiseFillFrame)
        self.BackgroundNoiseFillButton.setGeometry(QtCore.QRect(10, 60, 191, 19))
        self.BackgroundNoiseFillButton.setObjectName("BackgroundNoiseFillButton")
        self.WindowingEnableFrame = QtWidgets.QFrame(self.RenderSettingsFrame)
        self.WindowingEnableFrame.setGeometry(QtCore.QRect(610, 10, 291, 81))
        self.WindowingEnableFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WindowingEnableFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WindowingEnableFrame.setObjectName("WindowingEnableFrame")
        self.CrossfadeEnableText = QtWidgets.QTextEdit(self.WindowingEnableFrame)
        self.CrossfadeEnableText.setGeometry(QtCore.QRect(10, 10, 271, 31))
        self.CrossfadeEnableText.setObjectName("CrossfadeEnableText")
        self.CrossfadeEnableButton = QtWidgets.QRadioButton(self.WindowingEnableFrame)
        self.CrossfadeEnableButton.setGeometry(QtCore.QRect(10, 50, 231, 19))
        self.CrossfadeEnableButton.setObjectName("CrossfadeEnableButton")
        self.frame = QtWidgets.QFrame(self.RenderSettingsFrame)
        self.frame.setGeometry(QtCore.QRect(10, 150, 331, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ProfanityFilterText = QtWidgets.QTextEdit(self.frame)
        self.ProfanityFilterText.setGeometry(QtCore.QRect(10, 20, 319, 31))
        self.ProfanityFilterText.setObjectName("ProfanityFilterText")
        self.ProfanityFilterButton = QtWidgets.QRadioButton(self.frame)
        self.ProfanityFilterButton.setGeometry(QtCore.QRect(10, 70, 171, 19))
        self.ProfanityFilterButton.setObjectName("ProfanityFilterButton")
        self.gridLayout_12.addWidget(self.RenderSettingsFrame, 0, 0, 1, 1)
        self.TabWidget.addTab(self.tab_3, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.RenderedChannelTabs = QtWidgets.QTabWidget(self.tab2)
        self.RenderedChannelTabs.setObjectName("RenderedChannelTabs")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.NewTransFrame = QtWidgets.QFrame(self.tab_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewTransFrame.sizePolicy().hasHeightForWidth())
        self.NewTransFrame.setSizePolicy(sizePolicy)
        self.NewTransFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NewTransFrame.setAutoFillBackground(True)
        self.NewTransFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.NewTransFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NewTransFrame.setObjectName("NewTransFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.NewTransFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.newspec_plot = QtWidgets.QWidget(self.NewTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newspec_plot.sizePolicy().hasHeightForWidth())
        self.newspec_plot.setSizePolicy(sizePolicy)
        self.newspec_plot.setObjectName("newspec_plot")
        self.gridLayout_4.addWidget(self.newspec_plot, 2, 0, 1, 2)
        self.NewSpecScrollBar = QtWidgets.QScrollBar(self.NewTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewSpecScrollBar.sizePolicy().hasHeightForWidth())
        self.NewSpecScrollBar.setSizePolicy(sizePolicy)
        self.NewSpecScrollBar.setMaximumSize(QtCore.QSize(16777215, 200))
        self.NewSpecScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.NewSpecScrollBar.setObjectName("NewSpecScrollBar")
        self.gridLayout_4.addWidget(self.NewSpecScrollBar, 3, 0, 1, 2)
        self.SetOriginalButton = QtWidgets.QPushButton(self.NewTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SetOriginalButton.sizePolicy().hasHeightForWidth())
        self.SetOriginalButton.setSizePolicy(sizePolicy)
        self.SetOriginalButton.setIconSize(QtCore.QSize(18, 18))
        self.SetOriginalButton.setObjectName("SetOriginalButton")
        self.gridLayout_4.addWidget(self.SetOriginalButton, 0, 1, 1, 1)
        self.newwords = QtWidgets.QTextEdit(self.NewTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newwords.sizePolicy().hasHeightForWidth())
        self.newwords.setSizePolicy(sizePolicy)
        self.newwords.setObjectName("newwords")
        self.gridLayout_4.addWidget(self.newwords, 1, 0, 1, 2)
        self.gridLayout_11.addWidget(self.NewTransFrame, 0, 0, 1, 1)
        self.RenderedChannelTabs.addTab(self.tab_6, "")
        self.gridLayout_5.addWidget(self.RenderedChannelTabs, 0, 0, 1, 1)
        self.TabWidget.addTab(self.tab2, "")
        self.gridLayout.addWidget(self.TabWidget, 0, 0, 1, 1)

        self.retranslateUi(TranscriptEditor)
        self.TabWidget.setCurrentIndex(1)
        self.OriginalChannelTabs.setCurrentIndex(0)
        self.RenderedChannelTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TranscriptEditor)

    def retranslateUi(self, TranscriptEditor):
        _translate = QtCore.QCoreApplication.translate
        TranscriptEditor.setWindowTitle(_translate("TranscriptEditor", "Dialog"))
        self.OriginalChannelTabs.setTabText(self.OriginalChannelTabs.indexOf(self.tab_2), _translate("TranscriptEditor", "Main Channel"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab1), _translate("TranscriptEditor", "Original Transcription"))
        self.ShiftAsTimestampButton.setText(_translate("TranscriptEditor", "Amount = time"))
        self.DoOverlapButton.setText(_translate("TranscriptEditor", "Overlap Shifts"))
        self.ApplyShiftButton.setText(_translate("TranscriptEditor", "Apply Shift"))
        self.DescriptionBox.setHtml(_translate("TranscriptEditor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Speaker number selection:</p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Word selection starting index:</p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Word selection ending index:</p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Word segment shift amount (seconds):</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- overlap shifts: non insert method</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- amount = time: start time of first word = amount, shift calculated from this </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Format of transcript:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Speaker #&lt;channel number&gt;: [ &lt;first word index&gt;, &lt;timestamp of first word&gt;]   word, next word, next next word, ... [ &lt;last word index&gt;, &lt;timestamp of last word&gt;]</p></body></html>"))
        self.RenderButton.setText(_translate("TranscriptEditor", "Render"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab), _translate("TranscriptEditor", "Transcript Editor"))
        self.PauseShorteningText.setHtml(_translate("TranscriptEditor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Pause Shortening:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter max pause amount in slider. Any pauses &gt; amount gets shortened to amount</p></body></html>"))
        self.PauseShorteningButton.setText(_translate("TranscriptEditor", "Enable Pause Shorterning"))
        self.BackGroundNoiseFillerText.setHtml(_translate("TranscriptEditor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Background Noise Filler:</span></p></body></html>"))
        self.BackgroundNoiseFillButton.setText(_translate("TranscriptEditor", "Enable Background Noise Filler"))
        self.CrossfadeEnableText.setHtml(_translate("TranscriptEditor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Crossfade start/ends of sliced semgents:</span></p></body></html>"))
        self.CrossfadeEnableButton.setText(_translate("TranscriptEditor", "Enable Crossfade on edited segments"))
        self.ProfanityFilterText.setHtml(_translate("TranscriptEditor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Profanity Filter:</span></p></body></html>"))
        self.ProfanityFilterButton.setText(_translate("TranscriptEditor", "Enable Profanity Filter"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_3), _translate("TranscriptEditor", "Render Settings"))
        self.SetOriginalButton.setText(_translate("TranscriptEditor", "Set as Original"))
        self.RenderedChannelTabs.setTabText(self.RenderedChannelTabs.indexOf(self.tab_6), _translate("TranscriptEditor", "Main Channel"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab2), _translate("TranscriptEditor", "Rendered Transcription"))



    ### ADD CUSTOM FUNCTIONS BELOW THIS LINE AUTO GENERATED ABOVE ###

    # Called after Render button
    # Need to add audio file things eventually maybe
    def doRender(self):
        # read rendersettings to send as er parameter
        print('Starting Rendering...')
        rendersettings = self.readRenderSettings() 

        # order timestamps for rendering optimizatons
        for i in range(self.numchannels):
            self.oldTranscripts[i].quicksort( (0, self.oldTranscripts[i].wordCount - 1) )

        
        if(rendersettings.profanityFilterEnable):
            self.oldTranscripts[0].profanityFilter(self.oldTranscripts, rendersettings)
            self.oldTranscripts[1].profanityFilter(self.oldTranscripts, rendersettings)
        
        # prelim setup based on render settings
        if(rendersettings.pauseShortenEnable):
            for i in range(self.numchannels):
                self.oldTranscripts[i].findPauses()

            self.oldTranscripts[0].findOverlappingPauses(self.oldTranscripts, rendersettings)
            self.oldTranscripts[1].findOverlappingPauses(self.oldTranscripts, rendersettings)

        render = self.oldTranscripts[self.numchannels - 1].RenderTranscription(rendersettings)
        for i in range(self.numchannels - 1):
            newrender = self.oldTranscripts[i].RenderTranscription(rendersettings)
            # pad to length w/Stereo/Mono checks
            if(newrender.shape[1] > render.shape[1]):
                if(render.shape[0] == 2):
                    pad = newrender.shape[1] - render.shape[1]
                    render = np.hstack((render, np.zeros(pad*2).reshape(2,pad)))
                else:
                    render = np.hstack((render, np.zeros(newrender.shape[1] - render.shape[1])))
            elif(newrender.shape[1] < render.shape[1]):
                if(render.shape[0] == 2):
                    pad = render.shape[1] - newrender.shape[1]
                    newrender= np.hstack((newrender, np.zeros(pad*2).reshape(2,pad)))
                else:
                    newrender = np.hstack((newrender, np.zeros(render.shape[1] - newrender.shape[1])))

            render += newrender
        
        print('Rendered, check next tab') 
        #flatten to mono for spectrogram (resulting audio isnt flattened)
        if(render.shape[0] > 1):
            ins = render.sum(axis=0) / 2
            f, t, spec = signal.spectrogram(ins.transpose(), self.oldTranscripts[0].sr)
        else:
            f, t, spec = signal.spectrogram(render, self.oldTranscripts[0].sr)
    
        self.plotNewSpec(spec, t, f)
        
        maintrans = Transcript()
        maintrans.MainFromOthers(self.oldTranscripts)
        self.setNewTranscriptText(maintrans)

        self.blockSetAsOriginal = False

        sound(render, self.oldTranscripts[0].sr, 'Rendered Sound')

    # creates a RenderSettings class and fills out parameters based on user inputs
    def readRenderSettings(self):
        rendersettings = RenderSettings()
        # just go through rendersettings tab
        rendersettings.pauseShortenEnable = self.PauseShorteningButton.isChecked()
        rendersettings.pauseShortenAmount = self.PauseShortenAmountBox.value()
        rendersettings.backgroundFillEnable = self.BackgroundNoiseFillButton.isChecked()
        rendersettings.crossfadeEnable = self.CrossfadeEnableButton.isChecked()
        rendersettings.profanityFilterEnable = self.ProfanityFilterButton.isChecked()
        #print('readsettigns: ', rendersettings.pauseShortenEnable, rendersettings.pauseShortenAmount, rendersettings.backgroundFillEnable)

        return rendersettings

    # function for when Apply Shift button is pressed in the transcript editor
    def doApplyShift(self):        
        #get active/visible editor tab
        activeIdx = self.ChannelSelectBox.value() - 1
        #activeWidget =  self.editorChannelArray[activeIdx]
        activeTranscript = self.oldTranscripts[activeIdx]

        # get select ranges, clip values to 0 and wordCount-1
        selectstart = max(self.WordSelectStart.value()-1, 0)
        selectend = min(self.WordSelectEnd.value()-1, activeTranscript.wordCount -1) 
        shiftamt = self.WordShiftAmount.value()

        # check buttons 
        if(self.ShiftAsTimestampButton.isChecked()):
            # find shiftamt 
            shiftamt = shiftamt - activeTranscript.timestamps[selectstart][0] 

        # quick check to make sure we cant shift into negative times, if this happends then change timeshift to move all things to 0
        if(activeTranscript.timestamps[selectstart][0] + shiftamt < 0):
            shiftamt = -activeTranscript.timestamps[selectstart][0]

        # do nothing checks
        if(selectstart > selectend or shiftamt == 0.00):
            return

        if(self.DoOverlapButton.isChecked()):
            self.doShiftOverlap(selectstart, selectend, shiftamt, activeIdx)
        else:
            self.doShiftInsert(selectstart, selectend, shiftamt, activeIdx)

        # resort orders and visibly update transcript editor
        self.updateTranscriptEditorText()
                 
        print('shift applied')
        
        self.WordSelectEnd.setValue(0)
        self.WordSelectStart.setValue(0)
        self.WordShiftAmount.setValue(0.00)

    def doShiftInsert(self, selectstart, selectend, shiftamt, activeIdx):
        # find starting timestamps to update
        aTrans = self.oldTranscripts[activeIdx]
        N = aTrans.timestamps[selectend][1] - aTrans.timestamps[selectstart][0]
        newstart_t = aTrans.timestamps[selectstart][0] + shiftamt
        newend_t = aTrans.timestamps[selectend][1] + shiftamt
        oldstart_t = aTrans.timestamps[selectstart][0]
        oldend_t = aTrans.timestamps[selectend][1]
            
        newshiftamt = shiftamt
        # loop through each transcript, find newstart index and do shifts
        newmarks = [0] * self.numchannels
        oldmarks = [0] * self.numchannels
        for ti in range(self.numchannels):
            t = self.oldTranscripts[ti]
            # find marker idx
            for i in range(t.wordCount-1):
                times = t.timestamps[i]
                # find newstart idx
                # test clipping
                if(times[0] <= newstart_t and times[1] >= newstart_t):
                    if(shiftamt > 0):
                        newshiftamt = min(newshiftamt, + shiftamt + (times[1] - newstart_t))
                    else:
                        newshiftamt = max(newshiftamt, shiftamt + (times[1] - newstart_t))

                #find markers based on shift
                if(shiftamt > 0):
                    # find oldend
                    if(times[1] <= oldend_t and t.timestamps[i+1][0] >= oldend_t):
                        oldmarks[ti] = i + 1
                    elif(times[0] <= oldend_t and times[1] >= oldend_t):
                        oldmarks[ti] = i
                    # find newend mark 
                    # test clipping
                    if(times[0] <= newend_t and times[1] >= newend_t):
                        newmarks[ti] = i
                    elif(times[1] <= newend_t and t.timestamps[i+1][0] >= newend_t):
                        newmarks[ti] = i
                else:
                    # find oldstart
                    if(times[1] <= oldstart_t and t.timestamps[i+1][0] >= oldstart_t):
                        oldmarks[ti] = i 
                    elif(times[0] <= oldstart_t and times[1] >= oldstart_t):
                        oldmarks[ti] = i - 1
                    # test clipping
                    if(times[0] <= newstart_t and times[1] >= newstart_t):
                        newmarks[ti] = i
                    elif(times[1] <= newstart_t and t.timestamps[i+1][1] >= newstart_t):
                        newmarks[ti] = i + 1
            
            # check last word
            #find markers based on shift
            i = t.wordCount-1;
            if(shiftamt > 0):
                # find oldend
                if(times[0] <= oldend_t and times[1] >= oldend_t):
                    oldmarks[ti] = i
                # find newend mark 
                # test clipping
                if(times[0] <= newend_t and times[1] >= newend_t):
                    newmarks[ti] = i
            else:
                # find oldstart
                if(times[0] <= oldstart_t and times[1] >= oldstart_t):
                    oldmarks[ti] = i - 1
                # test clipping
                if(times[0] <= newstart_t and times[1] >= newstart_t):
                    newmarks[ti] = i
                
            # check for edges
            if(shiftamt>0):
                if(oldmarks[ti]==-1):
                    oldmarks[ti] = 0
            else:
                if(newmarks[ti] == -1):
                    newmarks[ti] = 0

        print('shiftamt: ', shiftamt)
        print('oldmarks: ', oldmarks)
        print('newmarks: ', newmarks)

        shiftamt = newshiftamt
        # apply shifts 
        for ti in range(self.numchannels):   
            if(newmarks[ti] != oldmarks[ti]):
                if(shiftamt > 0):
                    for i in range(oldmarks[ti], newmarks[ti]+1):
                        tup = self.oldTranscripts[ti].timestamps[i]
                        self.oldTranscripts[ti].timestamps[i] = (tup[0] - N, tup[1] - N)
                        self.oldTranscripts[ti].shifts[i] -= N
                else:
                    for i in range(newmarks[ti], oldmarks[ti]+1):
                        tup = self.oldTranscripts[ti].timestamps[i]
                        self.oldTranscripts[ti].timestamps[i] = (tup[0] + N, tup[1] + N)
                        self.oldTranscripts[ti].shifts[i] += N
            
        # apply shift to selected region
        for i in range(selectstart, selectend+1):
            tup = self.oldTranscripts[activeIdx].timestamps[i]
            #print(self.oldTranscripts[activeIdx].words[i])
            self.oldTranscripts[activeIdx].timestamps[i] = (tup[0] + shiftamt, tup[1] + shiftamt)
            self.oldTranscripts[activeIdx].shifts[i] += shiftamt

        self.unsortedTranscripts = True


    def doShiftOverlap(self, selectstart, selectend, shiftamt, activeTranscript):
         # apply shift to timestamps and keep track of shifts in shift array
        i = selectstart
        while i <= selectend:
            tup = activeTranscript.timestamps[i]
            activeTranscript.timestamps[i] = (tup[0] + shiftamt, tup[1] + shiftamt)
            activeTranscript.shifts[i] += shiftamt
            i += 1
        self.unsortedTranscripts = True


    def updateTranscriptEditorText(self):
        if(self.unsortedTranscripts):
            for i in range(self.numchannels):
                self.oldTranscripts[i].quicksort( (0, self.oldTranscripts[i].wordCount - 1) )
        self.initTranscriptEditor(self.oldTranscripts, self.numchannels)

        
    def doSetAsOriginal(self):
        # delete tabs to be replaced
        # remove all but main channels
        if(self.blockSetAsOriginal):
            return 

        for i in range(self.numchannels):
            self.OriginalChannelTabs.removeTab(1)
        
        # set oldtranscript audio to newrenders
        for i in range(self.numchannels):
            self.oldTranscripts[i].setAudioAsRender()


        self.launchInit(self.oldTranscripts, self.numchannels)
        self.blockSetAsOriginal = False

    def plotNewSpec(self, spec, t, f):

        if(self.newSpecLayer.count() > 0):
            self.newSpecLayer.removeWidget(self.newSpecWidget)

        m = MplCanvas(self.newspec_plot, width=5, height=4)
        m.plotSpec(spec, t, f)
        self.newSpecWidget = m

        self.newSpecLayer.addWidget(m)

        self.show()
        
    # 0 = main, 1-any = channel # 
    def plotOldSpec(self, transcripts, channel):
        if(channel == 0):
            if(self.Mainl == None):
                # init mpl
                self.Mainl = QtWidgets.QVBoxLayout(self.oldspec_plot)
            
                if(self.Mainl.count() > 0):
                    self.Mainl.removeWidget(self.oldSpecWidget)

                self.Mainm = MplCanvas(self.oldspec_plot, width=5, height=4)

                self.oldSpecWidget = self.Mainm
                self.Mainl.addWidget(self.Mainm)
                self.show()
            
            # plot main channel
            # mono/stero handle
            if(self.oldTranscripts[self.numchannels-1].isStereo):
                render = self.oldTranscripts[self.numchannels-1].audio.sum(axis=1) / 2
            else:
                render = copy.deepcopy(self.oldTranscripts[self.numchannels-1].audio)
            for i in range(self.numchannels - 1):
                # mono/stero handle
                if(self.oldTranscripts[i].isStereo):
                    newrender = self.oldTranscripts[i].audio.sum(axis=1) / 2
                else:
                    newrender = self.oldTranscripts[i].audio

                # combine renders
                if(len(newrender) > len(render)):
                    render = np.hstack((render, np.zeros(len(newrender) - len(render))))
                render = np.add(newrender, render)

            f, t, spec = signal.spectrogram(render, self.oldTranscripts[0].sr)

            self.Mainm.plotSpec(spec, t, f)

        if(channel > 0):
            frame = self.oldChannelArray[channel-1]
            l = QtWidgets.QVBoxLayout(frame.oldspec_plot)

            if(l.count() > 0):
                l.removeWidget(frame.oldSpecWidget)
            m = MplCanvas(frame.oldspec_plot, width=5, height=4)

            spec, t, f = self.oldTranscripts[channel-1].getSpec()
            m.plotSpec(spec, t, f)
            frame.oldSpecWidget = m
            l.addWidget(m)
            self.show()


    #param: words - transcript.words array
    def setOldTranscriptText(self, transcripts, numchannels):
        self.oldTranscripts = []
      

        # create new tabs and fill in
        if(numchannels >= 1):
            # create new tabs for each channel and add its transcription
            # aarray holds frames
            self.oldChannelArray = []
            self.oldTranscripts = []
            for i in range(numchannels):
                # duplicate frame, create new tab and place
                tabname = "Speaker " + str(i+1)
    
                newtab = QtWidgets.QWidget()
                newframe = TranscriptPlotFrame(self.OriginalChannelTabs)
                newframe.setupUi(newframe)

                gridlayout = QtWidgets.QGridLayout(newtab)
                gridlayout.addWidget(newframe, 0, 0, 1, 1)
                
                # TODO, fix layout to grid !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!              

                self.OriginalChannelTabs.addTab(newtab, tabname) 
                self.oldChannelArray.append(newframe)

                # setup words  
                transcript = transcripts[i]    

                text = ""
                words = transcript.words
                for k in range(len(words)):
                    text += words[k] + ' ' 

                newframe.oldwords.setText(text)
                self.oldTranscripts.append(transcripts[i])

        # fills in main, This needs to be redone to include all transcripts
        transcript = Transcript()
        transcript.MainFromOthers(transcripts)

        text = self.compileTranscriptsTexts(self.oldTranscripts, self.numchannels)
        self.oldwords.setText(text)
        self.oldTranscripts.append(transcripts[0])
                
        self.OriginalChannelTabs.setCurrentIndex(0)
        self.ChannelSelectBox.setMinimum(1)
        self.ChannelSelectBox

    ## happens only when original transcription is set and on first transcript
    def initTranscriptEditor(self, transcripts, numchannels):
        # fill word box in chronological order of speaker words

        text = self.compileTranscriptsTexts(transcripts, numchannels)

        self.TranscriptWordBox.setText(text)
        self.ChannelSelectBox.setMinimum(1)
        self.ChannelSelectBox.setMaximum(numchannels)
        self.WordSelectStart.setMinimum(1)
        self.WordSelectStart.setMaximum(999999)
        self.WordSelectEnd.setMinimum(1)
        self.WordSelectEnd.setMaximum(999999)
        self.ApplyShiftButton.clicked.connect(self.doApplyShift)

    def compileTranscriptsTexts(self, transcripts, numchannels):
        done = False
        nextwords = [0] * numchannels # array to keep track of last seen words in each channel
        lastChannel = -1
        text = ""
        while not(done):
            # go through each channel, get next word, use next upcoming word
            nextTimes = [0] * numchannels
            for i in range(numchannels):
                wordIdx = nextwords[i]
                if(wordIdx > transcripts[i].wordCount-1):
                    nextTimes[i] = 999999999999 # finished this array, sentinel value to never pass
                else:
                    nextTimes[i] = transcripts[i].timestamps[wordIdx][0] # only care about start times

            minTimeIdx = nextTimes.index(min(nextTimes))
            #minTimeIdx = channel with next upcoming spoken word

            word = transcripts[minTimeIdx].words[nextwords[minTimeIdx]]
            if(minTimeIdx == lastChannel):
                # spoken word is by same person as last
                text += " " + word
            else:
                # new speaker, add text for that
                # first add timestamp and word idx to end of prev word
                if(lastChannel != -1):
                    text += "  [" + str(nextwords[lastChannel]) + ", " + str(round(transcripts[lastChannel].timestamps[nextwords[lastChannel] - 1][1], 2)) + "]\n\n"
                text += "Speaker #" + str(minTimeIdx + 1) + ": " + "[" + str(nextwords[minTimeIdx]+1) + ", " + str(round(transcripts[minTimeIdx].timestamps[nextwords[minTimeIdx]][0], 2)) + "]  " 
                text += " " + word
            
            lastChannel = minTimeIdx
            nextwords[minTimeIdx] += 1

            # check if done
            done = True 
            for i in range(numchannels):
                if(nextwords[i] < transcripts[i].wordCount):
                    done = False
                    i = numchannels - 1

        text += "  [" + str(nextwords[lastChannel]) + ", " + str(round(transcripts[lastChannel].timestamps[nextwords[lastChannel] - 1][1], 2)) + "]"   
        
        return text

    def setNewTranscriptText(self, transcript):
        # TODO, Main channels should show all words of each channel
        text = self.compileTranscriptsTexts(self.oldTranscripts, self.numchannels)
        self.newwords.setText(text)


    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    ## for hooking up buttons and stuff keep at bottom for function reading
    def setupUiManual(self):
        self.RenderButton.clicked.connect(self.doRender)
        self.newSpecLayer = QtWidgets.QVBoxLayout(self.newspec_plot) 
        #self.oldSpecLayer = QtWidgets.QVBoxLayout(self.oldspec_plot)
        self.SetOriginalButton.clicked.connect(self.doSetAsOriginal)
        
        self.unsortedTranscripts = False
        self.blockSetAsOriginal = True
        self.Mainl = None
        self.TabWidget.setFocus()
        self.setCentralWidget(self.TabWidget)
    
    # transcripts = array of transcripts, len(transcripts) = number of channels
    def launchInit(self,transcripts, numchannels):
        self.numchannels = numchannels
        self.setOldTranscriptText(transcripts, numchannels)

        for i in range(numchannels+1):
            self.plotOldSpec(transcripts, i)

        self.initTranscriptEditor(transcripts, numchannels)

        # do prelim feature stuff, e.g. sample background noise
        for i in range(self.numchannels):
            self.oldTranscripts[i].findPauses()
            self.oldTranscripts[i].sampleBackgroundNoise()

            



## matplotlib canvas widget class thing
class MplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

    def plotSpec(self, spec, t, f):
        self.axes.clear()
        self.axes.cla()
        self.axes.pcolormesh(t, f, abs(spec)**0.3) # n^0.3 to 'normalize' 
        self.axes.set_xlabel('time (seconds)')
        self.axes.set_ylabel('Frequency (Hz)')
        self.draw()

    

    ### just to test plot ####
    def plotexample(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TranscriptEditor = QtWidgets.QDialog()
    ui = Ui_TranscriptEditor()
    ui.setupUi(TranscriptEditor)
    TranscriptEditor.show()
    sys.exit(app.exec_())

