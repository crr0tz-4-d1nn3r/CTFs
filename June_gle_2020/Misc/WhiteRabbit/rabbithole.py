
import os
import magic

filename = "rabbithole"
while True:
    filetype = magic.from_file(filename)
    print(filetype)
    if "gzip" in filetype:
        os.system("mv "+filename+" "+filename+".gz &&"+"gzip -d "+filename+".gz")
    if "bzip2" in filetype:
        os.system("bzip2 -d "+filename+" && mv "+filename+".out "+filename)