Encodings
==================
To reverse the encoding, only the algoritm needs be be known - there is no key or secret required. Some common encoding schemes include base32, base64. Typically, challenges have involved multiple encoding schemes being used in a single challenge.


`Droid (Brixel, 2020) <../../brixel_2020/Crypto/Droid/README.md>`_
-------------------------------------------------------------------------

A messenger droid was caught during the intergalactic war. Upon investigating his memory banks, we found this message:

.. code-block:: shell

    MDExMTAxMDAgMDExMDEwMDAgMDExMDAxMDEgMDAxMDAwMDAgMDExMDAxMTAgMDExMDExMDAgMDExMDAwMDEgMDExMDAxMTEgMDAxMDAwMDAgMDExMDEwMDEgMDExMTAwMTEgMDAxMDAwMDAgMDExMDAwMTAgMDExMTAwMTAgMDExMDEwMDEgMDExMTEwMDAgMDExMDAxMDEgMDExMDExMDAgMDEwMDAwMTEgMDEwMTAxMDAgMDEwMDAxMTAgMDExMTEwMTEgMDExMTAwMTAgMDExMDExMTEgMDExMDAwMTAgMDExMDExMTEgMDExMDAwMTEgMDExMDExMTEgMDExMTAwMDAgMDExMTExMDE=


We are lucky we found him, he was only 64 parsecs from his base


Solution
^^^^^^^^^^^
"64 parsecs" => base64? Also, lots of repeated data. 

.. code-block:: shell

    ┌──(kali㉿kali)-[~]
    └─$ echo "MDExMTAxMDAgMDExMDEwMDAgMDExMDAxMDEgMDAxMDAwMDAgMDExMDAxMTAgMDExMDExMDAgMDExMDAwMDEgMDExMDAxMTEgMDAxMDAwMDAgMDExMDEwMDEgMDExMTAwMTEgMDAxMDAwMDAgMDExMDAwMTAgMDExMTAwMTAgMDExMDEwMDEgMDExMTEwMDAgMDExMDAxMDEgMDExMDExMDAgMDEwMDAwMTEgMDEwMTAxMDAgMDEwMDAxMTAgMDExMTEwMTEgMDExMTAwMTAgMDExMDExMTEgMDExMDAwMTAgMDExMDExMTEgMDExMDAwMTEgMDExMDExMTEgMDExMTAwMDAgMDExMTExMDE=" | base64 -d

    01110100 01101000 01100101 00100000 01100110 01101100 01100001 01100111 00100000 01101001 01110011 00100000 01100010 01110010 01101001 01111000 01100101 01101100 01000011 01010100 01000110 01111011 01110010 01101111 01100010 01101111 01100011 01101111 01110000 01111101  


Looks like binary. For even more fun with one-liners (thanks to `<https://unix.stackexchange.com/questions/98948/ascii-to-binary-and-binary-to-ascii-conversion-tools>`_) pipe the output to Perl
with the command ```perl -lape '$_=pack"(B8)*",@F'```

.. code-block:: shell
    
    ┌──(kali㉿kali)-[~]
    └─$ echo "MDExMTAxMDAgMDExMDEwMDAgMDExMDAxMDEgMDAxMDAwMDAgMDExMDAxMTAgMDExMDExMDAgMDExMDAwMDEgMDExMDAxMTEgMDAxMDAwMDAgMDExMDEwMDEgMDExMTAwMTEgMDAxMDAwMDAgMDExMDAwMTAgMDExMTAwMTAgMDExMDEwMDEgMDExMTEwMDAgMDExMDAxMDEgMDExMDExMDAgMDEwMDAwMTEgMDEwMTAxMDAgMDEwMDAxMTAgMDExMTEwMTEgMDExMTAwMTAgMDExMDExMTEgMDExMDAwMTAgMDExMDExMTEgMDExMDAwMTEgMDExMDExMTEgMDExMTAwMDAgMDExMTExMDE=" | base64 -d | perl -lape '$_=pack"(B8)*",@F'
    the flag is brixelCTF{robocop}


Flag: brixelCTF{robocop}


