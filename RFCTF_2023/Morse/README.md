# Morse Code Challenges

There was a set of five morse code challenges. Four were available online, and one was on site only. Challenges use basically the same set techniques to solve.

- [Morse Code Challenges](#morse-code-challenges)
  - [Acquire](#acquire)
  - [Playback](#playback)
  - [Decode](#decode)
    - [Manual Decode](#manual-decode)
    - [Fldigi](#fldigi)
  - [Flags](#flags)
  - [References](#references)


## Acquire
See [Acquiring the signal](../Acquisition/README.md#Acquisition)

## Playback

See [Playback of signal](../Acquisition/README.md#Playback)

You will want something to play back the capture. Of course there is gnuradio. I had trouble getting good audio signal from gnuradio. Probably because I don't know what I'm doing yet.

Gqrx works well with the IQ files produced by gnuradio. Audacity can handle the IQ files, just have to import them as raw data (File -> Import -> Raw Data). MAke sure to set the sample rate to 96000. Also, since this is complex32 data samples, set the sample type to float32, and select 2 channels for input.

![Audacity setup](audacity_import.png)

The nice thing about  using audacity is you can trim the collection to just the signal - leave a couple seconds on either end. You can also scrub forward and backward through the signal. I also mixed the two channel stereo down to mono and exported thje result to a wav file.

## Decode

If you know morse code, excellent!

Otherwise, you can manually decode the dits and dahs by inspection, or use something like multimon-ng or fldigi.

### Manual Decode

To manually decode, I find Audacity to work well. That - along with concentration and an online decoder tool.

![morse decode example](morse_decode_example.png)


1. Delete channel marker part so that 0:00 is start of morse signal
2. Zoom in to scale of 1/10th of a second
3. Read . (dit) and - (dah)
4. Convert to uppercase ascii, then drop the challenge ID

For example, Morse 4 would look like this:
![](2023_RFCTF/Morse/morse4-audacity.png)

### Fldigi

Fldigi was very usefull for many of the challenges. It takes some tuning to get right, but worked well.  For these challenges, you need to set the words per minute (WPM).

Start by opening the capture for playback. I used both Gqrx and Audacity with success. For this write up I use Audacity.

Notice in the picture above that one word takes about 10 seconds to transmit. That means you'll have somewhere between 4 to 6 WPM.

Open fldigi. You need to set the filter to CW.

![fldigi CW mode](fldigi_cw_mode.png)

Set the WPM to 5 (the loweest setting it seems).

![fldigi 5 WPM](fldigi_wpm.png)

Move the target box to contain the CW signal.

![fldigi signal](fldigi_signal.png)

And profit??

![Showing workflow for decode](toolchain.png)

## Flags

```bash
MORSE 3: BSIDESLV POOL PARTY IS LIT  
```
```bash
00:00  -- --- .-. ... . ....- ---...
02.60  .--. .-. --- - --- -.
04.70 -... . .- -- ...
06.05  -.-. .-. . .- - .
07.50 .-
07.80 -.. .- --.. --.. .-.. .. -. --.
10.45   .-.. .. --. .... -
11.90  ... .... --- .-- .-.-.-

MORSE 4: PROTON BEAMS CREATE A DAZZLING LIGHT SHOW.
```

## References

- [https://gnuradio.org/](https://gnuradio.org/)
- [https://www.audacityteam.org/](https://www.audacityteam.org/)
- [https://gqrx.dk/](https://gqrx.dk/)
- [https://morsedecoder.com/](https://morsedecoder.com/)
