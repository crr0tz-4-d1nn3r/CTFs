## Flag:
```flag

```

## Solution
Download ranblings and message. Based on title and some hints - pretty sure this is bifid (https://en.wikipedia.org/wiki/Bifid_cipher).

If "cleaning up the ramblings" means removing punctuation and spaces - that makes 20 of the lines have 26 characters.

Classically - "I" and "J" share posistion in the square - so I go rid of all "J" or "j" in the ramblings. That left 20 ramblings of 25 characters...

What is "perfect"? I did a search of one of the rambling "Crwth vox zaps qi gym fjeld bunk" and found this https://medium.com/@FallingForFallacies/all-perfect-pangrams-of-english-8c8d0f621bee

Originally I tried this problem with sympy.crypto.crypto module decipher_bifid5 and it did not work had nothing but garbage. Switched to pycipher module Bifid and what do you know ...

```python
from pycipher import Bifid

msg = 'snbwmuotwodwvcywfgmruotoozaiwghlabvuzmfobhtywftopmtawyhifqgtsiowetrksrzgrztkfctxnrswnhxshylyehtatssukfvsnztyzlopsv'
keys = ['mrocktvquizphdbagsfewlynx',
'ocknymphswaqfdrugvexblitz',
'crwthvoxzapsqigymfeldbunk',
'hmfordwaltzcinqbuskpyxveg',
'phavfyxbugstonqmilkzdcrew',
'hesaidbcfgklmnopqrtuvwxyz',
'enqvahlbidgumkrwcfpostxyz',
'emilyqungschwarzkopfxtvbd',
'ohnfezcamrwsputyxigkqblvd',
'qtipforsuvnzxylemdcbaghwk',
'umblingvextfrowzyhackspdq',
'qvandzstruckmybigfoxwhelp',
'lumpydrabcgqvzinksfoxthew',
'heyiamnopqrstuvwxzbcdfgkl',
'quizvbmwlynxstockderpaghf',
'pledbigczarunksmyvwfoxthq',
'waltzgbquickfordsvexnymph',
'qwertyuioplkhgfdsazxcvbnm',
'zyxwvutsrqponmlkihgfedcba',
'aquickbrownfxmpsvethlzydg',
]

for i in range(len(keys)):
    key = keys[len(keys)-i-1]
    msg = Bifid(rambl,5).decipher(msg)
    print(str.lower(msg).replace('x', ' '))
```

So for some reason (mabe common practice??) we have to replace 'x' with ' ' and fill in the missing 'j's to make it "readable".
```shell
 ust some unnecessary te t that holds absolutely no meaning whatsoever and bears no significance to you in any way
 ```
 
 No flag captured.