#!/bin/bash

for cipher in $(cat ciphers.txt); do
        cipher=${cipher%$'\n'}
        openssl enc $cipher -d -a -salt -in encrypted_file -k onionshavelayers -out enc.1 2>/dev/null

        if base64 -d enc.1 | grep -q "Salted"; then
            echo $cipher
            cat enc.1
            break
        fi    
done

for cipher in $(cat ciphers.txt); do
        cipher=${cipher%$'\n'}
        openssl enc $cipher -d -a -salt -in enc.1 -k onionshavelayers -out enc.2 2>/dev/null
        output=$(file enc.2)
        echo $cipher $output
done
