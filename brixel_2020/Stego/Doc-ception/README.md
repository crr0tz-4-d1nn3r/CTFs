# Doc-ception
10

Need to hide something? why not a word document?

You need to dig deeper

This flag is not in the usual format, you can enter it with or without the brixelCTF{flag} format

## Flag
```
openxml
```

## Solution
Using ```foremost``` [https://tools.kali.org/forensics/foremost](https://tools.kali.org/forensics/foremost) almost feels like cheating sometimes.

Download the docx, run ```foremost```. It finds a zip file. Not suprising as docx is just a type of zip archive. Inside the  archive is another docx... funny.

Run foremost again. Get another archive, extract it. And, while I expected another docx, I was suprised to find the flag.
