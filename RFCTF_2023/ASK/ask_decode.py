
infile = 'extracted.csv'

data = []
with open(infile,'r') as fh:
    data = fh.read()
data=data.split(',')

ascii_len = 8
flag = ''
for idx in range(0, len(data), ascii_len):
    bit_str = ''.join(i for i in data[idx:idx+ascii_len])
    flag += chr(int(bit_str,2))

print(flag)
