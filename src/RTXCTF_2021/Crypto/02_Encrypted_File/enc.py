
enc_file = 'enc.zip.enc'
out_png = 'enc.zip'

with open(enc_file,'rb') as infh:
    with open(out_png,'wb') as outfh:
        byte = infh.read(1)
        while byte != b'':
            xor = int.from_bytes(byte,'big') ^ 0xDE
            outfh.write(bytes([xor]))
            byte = infh.read(1)

