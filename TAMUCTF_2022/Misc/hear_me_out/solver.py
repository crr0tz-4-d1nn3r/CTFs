from scipy.io import wavfile as wav
from scipy.signal import spectrogram
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def isNumberInArray(array, number):
    offset = 5
    for i in range(number - offset, number + offset):
        if i in array:
            return True
    return False

def get1HzSpectrogram(data, sampleRate):
    freq, t, Sxx = spectrogram(data, fs = sampleRate, window = 'hann', nperseg=sampleRate)
    y = 10*np.log10(Sxx)
    return t, freq, y

def PlotSpectrogram(t,f,y):
     # Plot params
    plt.rcParams["font.family"] = "Times New Roman"
     # Set up plot
    fig = plt.figure(constrained_layout=True)
    gs = GridSpec(ncols=2, nrows=1, figure=fig, width_ratios=[50, 1])
    ax0 = fig.add_subplot(gs[0,0])
    ax1 = fig.add_subplot(gs[0,1])
    
    vmin = 20
    vmax = 80
    im = ax0.pcolormesh(t, f, y, shading='jet', vmin=vmin, vmax=vmax)
        
    # label axes
    ax0.set_ylabel('Frequency (Hz)\nΔf = ' + str(f[1]-f[0]) + 'Hz')
    ax0.set_xlabel('Time (s)')
    
    # plot legend
    cb = fig.colorbar(im, cax=ax1)
    cb.set_label('dB PSD')
    
    fig.set_size_inches(7, 4.5) 


DTMF_TABLE = {
    '1': [1209, 697],
    '2': [1336, 697],
    '3': [1477, 697],
    'A': [1633, 697],

    '4': [1209, 770],
    '5': [1336, 770],
    '6': [1477, 770],
    'B': [1633, 770],

    '7': [1209, 852],
    '8': [1336, 852],
    '9': [1477, 852],
    'C': [1633, 852],

    '*': [1209, 941],
    '0': [1336, 941],
    '#': [1477, 941],
    'D': [1633, 941],
} 



# reading 
rate, data = wav.read('hear-me-out.wav')


# Calculate fourier trasform of data
t, f, y = get1HzSpectrogram(data, rate)
PlotSpectrogram(t,f,y)

"""
# Detect and print pressed button
for char, frequency_pair in DTMF_TABLE.items():
    if (isNumberInArray(freqs, frequency_pair[0]) and
        isNumberInArray(freqs, frequency_pair[1])):
        print (char)
"""