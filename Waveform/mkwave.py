import math

import numpy as np

note_frequency = 256 # Hz


note_duration = 65536/(note_frequency**2) # second



def gen_sine_wave(freq, t):
    # return y (height)
    return math.sin(freq * 2 * math.pi * t)
    
    
def gen_sine_wave_arr(freq, t):
    global note_duration
    # return y (height)
    return np.sin(freq*np.arange(0, int(note_duration*44100))/44100*2*math.pi)





def gen_cos_wave(freq, t):
    # return y (height)
    return math.cos(freq * 2 * math.pi * t)
    
def gen_cos_wave_arr(freq, t):
    global note_duration
    # return y (height)
    return np.cos(freq*np.arange(0, int(note_duration*44100))/44100*2*math.pi)
    
def gen_wave_af_freq_old(freq, t, note_duration, mult):
    return gen_sine_wave(freq*mult, t) * gen_cos_wave(mult/note_duration/2, t)
    
def gen_wave_af_freq(freq, t, note_duration, mult):
    return gen_sine_wave(freq*mult, t) * gen_cos_wave(mult/note_duration/2, t) / 10**(math.log(mult+1)/2)
    
    
    
def gen_wave_af_freq(freq, t, note_duration, mult):
    return np.multiply(gen_sine_wave_arr(freq*mult,t), gen_cos_wave_arr(mult/note_duration/2, t)) / 10**(math.log(mult+1)/2)
    #return gen_sine_wave(freq*mult, t) * gen_cos_wave(mult/note_duration/2, t) / 10**(math.log(mult+1)/2)
    
def gen_wave_af_freq_sub(freq, t, note_duration, mult):
    return gen_sine_wave(freq*mult, t) * gen_cos_wave(mult/note_duration/2, t) / 10**(math.log(mult)/2) / 2**(4.5)
    
    
    
    
    
    
from tqdm import tqdm








arr = np.array([0.0 for t in range(0, int(note_duration*44100))])

print(44100/2/2/note_frequency)
for i in tqdm(range(1, int(44100/2/2/note_frequency)*2+5, 2)):
    if (note_frequency * i < 44100//2):
        arr += gen_wave_af_freq(note_frequency, None, note_duration, i)
        #arr += np.array([gen_wave_af_freq(note_frequency, t/44100, note_duration, i)+0*gen_wave_af_freq_sub(note_frequency,t/44100, note_duration, i+1) for t in range(0, int(note_duration*44100))])
    else:
        break
        





 
import numpy as np
from scipy.io.wavfile import write

rate = 44100
#data = np.random.uniform(-1, 1, rate) # 1 second worth of random samples between -1 and 1
scaled = np.int16(arr / np.max(np.abs(arr)) * 32767)
write('test2.wav', rate, scaled)
    
    