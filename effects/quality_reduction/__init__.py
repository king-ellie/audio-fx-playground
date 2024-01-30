from pedalboard import Bitcrush, Resample
import enum

"""
RESAMPLE:
Resample an audio signal to a different sample rate, then upsample it
back to the original sample rate.
"""
resample = Resample(
    target_sample_rate=500,
    quality=
        # Resample.Quality.ZeroOrderHold # The lowest quality & fastest method
        # Resample.Quality.Linear
        # Resample.Quality.CatmullRom
        # Resample.Quality.Lagrange
        Resample.Quality.WindowedSinc # Highest quality & slowest method
)

"""
BITCRUSH:
A plugin that reduces the signal to a given bit depth, giving the audio 
a lo-fi, digitized sound. Floating-point bit depths are supported.

Bitcrushing changes the amount of “vertical” resolution used for an 
audio signal (i.e.: how many unique values could be used to represent 
each sample). For an effect that changes the “horizontal” resolution
(i.e.: how many samples are available per second), see pedalboard.Resample.
"""
bitcrush = Bitcrush(bit_depth=4)
