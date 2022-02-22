import subprocess

enc_file = '8_of_hearts.enc'
out_png = '8_of_hearts.png'

with open(enc_file,'rb') as infh:
    with open(out_png,'wb') as outfh:
        byte = infh.read(1)
        while byte != b'':
            xor = int.from_bytes(byte,'big') ^ 0x41
            outfh.write(bytes([xor]))
            byte = infh.read(1)

subprocess.run(["md5sum", out_png])