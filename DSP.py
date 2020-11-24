### THIS FILE IS JUST FOR 3RD PARTY FUNCTIONS ### 
# transcription library stuff
from scipy.io import wavfile
from scipy import signal

# stuff
import math
import numpy as np
import time

import copy

def sound( x, rate=8000, label=''):
    from IPython.display import display, Audio, HTML
    if label is '':
        display( Audio( x, rate=rate))
    else:
        display( HTML( 
        '<style> table, th, td {border: 0px; }</style> <table><tr><td>' + label + 
        '</td><td>' + Audio( x, rate=rate)._repr_html_()[3:] + '</td></tr></table>'
        ))


# returns segments of active audio, segments delivered as tuples of indexes to slice
def VAD_separate(audio, cutoff, sr):
    # filter at cutoff
    w = cutoff / (sr / 2)
    b, a = signal.butter(2, w, 'lowpass')
    newaudio = audio**2
    
    VAD = abs(signal.filtfilt(b, a, newaudio))
    threshold = .00045
    
    # trim segments above threshold
    segments = []
    currentsegment = []
    start = 0
    end = 0
    offset = int(0.2*sr)
    for i in range(len(VAD)):
        sample = VAD[i]
        
        if(sample > threshold):
            # check if this is same as before 
            if(i>0):
                if(VAD[i-1]<threshold):
                    start = i
        else:
            if(i>0):
                if(VAD[i-1] > threshold):
                    end = i
                    segments.append((max(0,start-offset),min(end+offset, len(audio)-1)))
                    
    segments = np.asarray(segments)
    return segments

def stft( input_sound, dft_size, hop_size, zero_pad, window=1.0):
    length = len(input_sound)
    
    # Part1. splitting into frames
    FrameAmount = math.ceil((length) / hop_size) + 1
    slices = np.arange(dft_size * FrameAmount).reshape(dft_size, FrameAmount)
    # set slices into array
    for i in range(FrameAmount):
        start = i * hop_size
        end = start + dft_size
        
        data = input_sound[start:end]
        
        # input too short... need to zero padd end
        if(data.shape[0] < dft_size):
            zero_padd = np.zeros(dft_size - data.shape[0])
            data = np.hstack((data, zero_padd))
           
        slices[:,i] = data * window
        
    #  Part2. Do fft of input slices        
    size = dft_size+zero_pad   
    if(size%2 ==0):
        NumBins = ((size) // 2) + 1
    else:
        NumBins = ((size) + 1) // 2
    
    NumBins = int(NumBins)
    f = np.arange(NumBins * FrameAmount, dtype=np.complex_).reshape(NumBins, FrameAmount)   
    f[:,:] = 0. + 0.j
    
    for i in range(FrameAmount):
        f[:,i] = np.fft.rfft(slices[:,i], size)      

    # Return a complex-valued spectrogram (frequencies x time)
    return f

def FormatAxis(specArray, sr, time):
    length = specArray.shape[1]
    numbins = specArray.shape[0]
    timeline = np.linspace(0, time, length)
    freqline = np.linspace(0, sr/2, numbins)
    #freqline = np.fft.fftfreq(numbins, d=1./sr)
    return timeline, freqline

def time2sample(time, sr):
    return round(time*sr)

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v/norm

