Hashes
================

A hash function takes an arbitrary message of arbitrary length and creates an output (a hash) of a fixed length. They are considered one-way functions (it is easy to compute the hash; given the hash, it is difficult to compute the message). The usually attack is to use a rainbow table or to try and find a collision.

`Flawed (Brixel, 2020) <../../brixel_2020/Crypto/Flawed/README.md>`_
-------------------------------------------------------------------------
Our l33t hackers hacked a bulletin board and gained access to the database. We need to find the admin password.

The user's database info is:

.. code-block:: shell

    Username:admin

    Passwordhash:d269ce15f9c44bc3992a5f4e5f273e06


The flag is the plaintext password

This flag is not in the usual format, you can enter it with or without the brixelCTF{flag} format.

Solution
^^^^^^^^^^^
There are a couple tools available for cracking hashes. This looks like MD5 (length = 16 Bytes) and likely unsalted (length + no ':' or '.'). Before getting fancy, try `CrackStation <https://crackstation.net/>`_. On this problem, that was all that was needed.

This problem really illustrates the need to use better passwords, salting passwords, and using a better hash function when storing passwords.

Flag: notsecure