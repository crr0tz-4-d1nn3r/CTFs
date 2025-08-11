# HAM_SSTV_1
50

Slow Scan TV. Try port 6566

## Solution
Use QSSTV to decode to the images

Followed-ish (outdated) tutorial
[https://ourcodeworld.com/articles/read/956/how-to-convert-decode-a-slow-scan-television-transmissions-sstv-audio-file-to-images-using-qsstv-in-ubuntu-18-04](https://ourcodeworld.com/articles/read/956/how-to-convert-decode-a-slow-scan-television-transmissions-sstv-audio-file-to-images-using-qsstv-in-ubuntu-18-04)

Installed the following - basically using steps 1 - 3 as a guide
```
sudo apt install pavucontrol
sudo apt install libhamlib-dev
sudo apt install qsstv
```

Configured QSSTV like the tutorial. 

```
pactl load-module module-null-sink sink_name=virtual-cable
pavucontrol
```

Verifying that the Sink Output exists. Start QSSTV 

QSSTV-> Configuration: Set Input device to pulse. Set clock frequency to match the recording at 96k.

In pavucontrol window, set QSSTV recording to monitor sink.

Play audio from command line with
```
paplay -d virtual-cable youraudiofile.wav
```

![solution](sstv1.png)

Unload sink
```
pactl list short modules
pactl unload-module ## Number of the null-sink 
```


## Flag
```
SSTV Flag:
Prototype Coupe with big wheels and trunk space!
```