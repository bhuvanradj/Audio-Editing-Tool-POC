### REAL POC CELL ##

#"""
#Created on Mon Feb 10 16:36:55 2020
#No stealy 
#@author: ecouv
#"""
# Qt5 related stuff
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon

from PyQt5 import QtWidgets

import sys
sys.path.insert(0, 'UserInterface/')
from GUI import Ui_TranscriptEditor
import Render


# transcription library stuff
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg') # for QT5

# stuff
import math
import numpy as np
import time
import speech_recognition as sr
import os
from pathlib import Path
import copy
from DSP import sound

## run this cell if you want to update your IBM transcripts

fp= 'RawAudio/djstep_himself_1min.mp3'
fpp='RawAudio/djstep_Tim_1min.mp3'


# translate API transcript to one easier to use
print('Transcribing audio file # 1...')
transcript1 = Render.Transcript()
transcript1.ibm_recog('djstep_himself_1min.mp3',fp)

print('Transcribing audio file # 2...')
transcript2 = Render.Transcript()
transcript2.ibm_recog('djstep_Tim_1min.mp3',fpp)

#print(transcript1.sr, transcript2.sr)

print('Transcription finished')

## run this if you want to keep transcripts same as last run

# GUI TESTING
print('Launching UI')
qApp = QtWidgets.QApplication(sys.argv)

# aw = ApplicationWindow, currently using TranscriptEditor from qtdesign
aw = Ui_TranscriptEditor()
aw.setupUi(aw)
aw.setupUiManual()

tarray = [transcript1, transcript2]
#tarray = [transcript1]

# sound widgets
main = np.empty
mainlen = 0
for i in range(len(tarray)):
    if(mainlen == 0):
        main = copy.deepcopy(tarray[i].audio)
        mainlen = 1
    else:
        #print(tarray[i].audio.shape, main.shape)
        leng = tarray[i].audio.shape[0]-1
        main[:leng,:] += tarray[i].audio[:main.shape[0]-1,:]
            
    #sound(tarray[i].audio.transpose(), tarray[i].sr, 'Raw Sound #' + str(i))
#sound(main.transpose(), tarray[i].sr, 'Raw Main Sound')
    
aw.launchInit(tarray, len(tarray))

aw.show()
sys.exit(qApp.exec_())