from pedalboard import Phaser, Chorus

"""
PHASER:
TLDR: copy the signal and take some of the frequencies in the copy
and slightly adjust their timings, then add the copy back to the original.

Signal is duplicated and the duplicate is delayed by a varying amount.
What makes the phaser different than a flanger is that the copy signal is
processed through filters, meaning some frequencies are delayed at 
different rates than others. Compared to a Flanger, there will be fewer
"cancellation valleys", so it will sound less harsh and distorted.


This audio effect can be controlled with standard phaser parameters: 
the speed and depth of the LFO controlling the frequency response, a mix 
control, a feedback control, and the centre frequency of the modulation.
"""
phaser = Phaser(
    rate_hz=500.0,
    depth=.5,
    centre_frequency_hz=1300,
    feedback=0.0,
)


"""
CHORUS:
Meant to simulate the subtle pitch and timing differences that occur 
when multiple musicians or vocalists play the same note, but vary 
slightly in pitch and timing.


This audio effect can be controlled via the speed and depth of the LFO 
controlling the frequency response, a mix control, a feedback control, 
and the centre delay of the modulation.

Note: To get classic chorus sounds try to use a centre delay time around 
7-8 ms with a low feeback volume and a low depth. This effect can also be 
used as a flanger with a lower centre delay time and a lot of feedback, 
and as a vibrato effect if the mix value is 1.
"""
chorus = Chorus(
    rate_hz=1.0,
    depth=.25,
    centre_delay_ms=7.0,
    feedback=0.0,
)
