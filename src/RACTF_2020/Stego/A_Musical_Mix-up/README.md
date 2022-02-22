# A Musical Mix-up
200 points

One of our guys found a strange midi file lying around on our servers. We think there might be some hidden data in it. See if you can help us out!

(challenge.mid)

#### References and Tools
http://www.ccarh.org/courses/253/handout/smf/
https://www.wavosaur.com/download/midi-note-hex.php
https://morioh.com/p/144a98b4ab3a
https://www.audacityteam.org/

#### Flag
```shell
ractf{f50c13ty_l3vel_5t3g!}
```

#### Solution
Midi file can be opened with Audacity. First I though it might be in the notes. Looked for python libraries that could read and decode. Message was not in the notes, but in the velocity of the notes.
```python
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
```
