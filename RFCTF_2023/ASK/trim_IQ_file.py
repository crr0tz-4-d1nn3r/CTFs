
infile = 'ask1.bin'
outfile = 'ask1_trim.bin'

start_seconds = 1.71
len_seconds = 0.17
samp_rate = 96000
samp_size = 4

skip = int(start_seconds * samp_rate * samp_size * 2)
count = int(len_seconds * samp_rate * samp_size * 2)

with open(outfile, 'wb') as fo:
    with open(infile, 'rb') as fi:
        fi.seek(skip, 0)
        fo.write(fi.read(count))

