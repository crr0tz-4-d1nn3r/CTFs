"""
A Musical Mix-up
One of our guys found a strange midi file 
lying around on our servers. We think there
might be some hidden data in it. See if you 
can help us out!
<challenge.mid
"""

# midi file can be opened with Audacity
# Midi file format primer: 
# http://www.ccarh.org/courses/253/handout/smf/
# First I though it might be in the notes:
# https://www.wavosaur.com/download/midi-note-hex.php
# looked for python libraries that could read and decode
# https://morioh.com/p/144a98b4ab3a
# Message was not in the notes, but in the velocity of the notes

from mido import MidiFile

mid = MidiFile('challenge.mid')

# message in the non-zero velocity info
flag = ''
for msg in mid.tracks[0]:
    if msg.type == 'note_on':
        if msg.velocity != 0:
            flag+= chr(msg.velocity)
            if chr(msg.velocity) == '}':
                break

print(flag)
    
    