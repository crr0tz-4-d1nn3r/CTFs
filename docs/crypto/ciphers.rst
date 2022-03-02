Ciphers
================
Encryption takes a message (plaintext) of arbitrary length, a secret key, and an encryption function to produce the encrypted message (ciphertext). These work on the principle that encrypting is easy, and decryption is very difficult without the key. 

`Merda (Brixel, 2020) <../../brixel_2020/Crypto/Merda/README.md>`_
-------------------------------------------------------------------------
An Italian messenger was caught during the war

He was carrying a piece of paper that read:

.. code-block:: shell

    ymj kqfl nx gwncjqHYK{uneefsfutqn}

Upon torturing the messenger for an explaination, he gestured a V with his fingers. The english guard took it as an insult and killed him right on the spot.

Maybe he just wanted some peace?

Solution
^^^^^^^^^^^
Clues abound in the flavor text of this problem. Fist the reference to Italian. My guess is potentially a Ceasar (because Italian) cipher. A Ceaser cipher uses a shift (or rotation) on an alphabet.

.. list-table:: Ceasar Cipher
    :header-rows: 1
    :stub-columns: 1

    * - Shift Value
      - a
      - b
      - c 
      - ... 
      - x 
      - y 
      - z 
    * - 1
      - b 
      - c 
      - d 
      - ...
      - y 
      - z 
      - a
    * - 2
      - c  
      - d  
      - e 
      - ...
      - z  
      - a 
      - b


The ciphertext contains only characters a - z, and the symbols '{' and '}' seem to be in place for the flag. We need to know a number for how much to rotate. The gesture, "V" could be a reference to two or five. 

We could compute the whole table for both shift values, but ... well, we could also use a tool, like `CyberChef ROT13 <https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,5)>`_. CyberChefs ROT13 will allow the user to set the amount of rotation. For this problem, -5 works (negative to rotate left).  Shift the cipher text left by 5 each letter.

The message decodes to 

.. code-block:: shell
    
    the flag is brixelCTF{pizzanapoli}

Flag: brixelCTF{pizzanapoli}
