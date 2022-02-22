# Lost evidence
30

A buddy of mine is in serious trouble. He works for the feds and accidentally deleted a pendrive containing crucial evidence

Can you get it back and tell us what the evidence is?

We need to know what the suspect bought


The flag is in this format: brixelCTF{name_of_product_bought}

[evidence.zip](evidence.zip)

## Flag
```
brixelCTF{cocaine}
```

## Solution

Download the zip. Extract. It's a .img file of the drive. Tried ```foremost``` as a hunch while I looked up how to rebuild a partition table. But there was no need, ```foremost`` came through with two files. Both are wav files of a phone tap. DTMF tones are clear. A portion of the phone cacll has a message being input. Used Audacity to create a wav of just the message.

[message.wav](message1.wav)

Feed it to [http://dialabc.com/sound/detect/index.html](http://dialabc.com/sound/detect/index.html). Got the following values:

```
8449903336667770844330222666222244466330227778844
```

Used a T9/multitap decoder at [https://www.dcode.fr/multitap-abc-cipher](https://www.dcode.fr/multitap-abc-cipher) to translate:
```
THX FOR THE COCAINE BRUH
```