"""
Time-based effects (AKA spatial effects) are audio effects that operate 
on the time domain of an audio signal rather than the frequency domain. 
They include effects such as reverb, delay, and echo, which create 
a sense of space and time in the mix by adding echoes and reflections 
of the original sound.
"""

from pedalboard import Compressor, Gain, Phaser, Reverb, Bitcrush, Chorus, Delay, Resample, Reverb

"""
DELAY:
A delay audio effect plug-in records the input signal, waits for however
long you want it to, and then plays it back. In the natural world, you can 
hear a type of delay called an “echo” in open spaces where the reflective 
surface is far enough away that the reflection will sound separated from 
the original.
"""
delay = Delay(
    delay_seconds=2.5,
    # feedback=100,
)

"""
REVERB:
Reverb simulates the natural echo and decay of sound in a room or space, 
adding depth and space to a sound. Sound waves move through space, and when 
they meet a physical impediment, they either bounce back in a series of 
reflections or get absorbed to some degree. We hear this series of reflections 
as a single, continuous sound, which we call "reverb."

Like an echo/delay, but much shorter and scattered.

Reverb is ideally added after recording. Get a dry recording, because if you 
get it with reverb in it, then the reverb scatters the frequencies around. 
If you process it dryly, then you can remove any unwanted frequencies and 
sounds first and then add reverb.
"""
reverb = Reverb(
    room_size=1.0,
    damping=.1,
    wet_level=.9,
    dry_level=.2,
    width=1.0,
    freeze_mode=0
)