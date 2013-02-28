import alsaaudio, wave, numpy
from time import time

def initialize(file_name):

    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
    inp.setchannels(1)
    inp.setrate(44100)
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    inp.setperiodsize(1024)

    w = wave.open(file_name, 'w')
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(44100)

    return inp, w

def record(seconds=20, file_name="untitled.wav"):

    inp, w = initialize(file_name)
    started = time()

    while time() < started + seconds:

        l, data = inp.read()
        a = numpy.fromstring(data, dtype='int16')
        w.writeframes(data)