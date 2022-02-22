#  A song...
10

I wrote this song

it seems I'm pretty bad at it, but hey! it could get you a flag :)


## Flag
```
brixelCTF{5667236346614}
```

## Solution

Wasn't sure what to make of this at first. But I recently watched a talk on the creation of an esoteric programming language "Rockstar". It's a pretty good talk if you haven't seen it, covers a bunch of other programming topics.
[https://www.youtube.com/watch?v=6avJHaC3C2U](https://www.youtube.com/watch?v=6avJHaC3C2U)

Parsing this program was a bit tedious, but doable. Read the docs:
[https://codewithrockstar.com/docs](https://codewithrockstar.com/docs)

There is also a way to just run the code on that same site.

Here's the basic idea. 
- Words like "Shout" and "Say" and "Scream" are print directives. So the first line 
  ```
  Shout "brixelCTF{" !!!
  ```
  Translates to 
  ```python
  print("brixelCTF{")
  ```
  in python.
  
- Words like "is" and "are" are variable asignements. This gets wierd as numerical values are interperted by counting the letters in the following words (mod 10). For example:
  ```
  Your skill is hopefully the best
  ```
  Translates to 
  ```python
  your_skill = 934
  ```
  because "hopefully" has 9 letters, "the" has 3 and "best" has 4. Thus 934.

I translated the song to python and was able to run the code and get the correct output.

