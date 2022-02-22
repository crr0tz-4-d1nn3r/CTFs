# Goodbye old friend
15

On 31/12/2020 support for flash will end

Therefor we made you a farewell animation

Can you get the flag?

Beware headphone users! the music is loud.

## Flag
```
brixelCTF{n0_m0r3_5upp0rt}
```

## Solution
Created a docker file to install gnash and run the file. Used it tutorial to do it [https://raymii.org/s/tutorials/Running_gnash_on_Ubuntu_20.04.html](https://raymii.org/s/tutorials/Running_gnash_on_Ubuntu_20.04.html)

Basically - create a folder and write your Dockerfile:
```
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y sudo
RUN apt-get update && apt-get install -y gnash

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

COPY goodbye.swf /home/developer/goodbye.swf
USER developer
ENV HOME /home/developer
CMD /usr/bin/gnash /home/developer/goodbye.swf
```
Replace the uid and gid with your own. Build the container
```
docker build -t gnash .
```
and run it
```
docker run -ti --rm -e DISPLAY=$DISPLAY --net=host -v /tmp/.X11-unix:/tmp/.X11-unix gnash
```

The flag is outputed as a TRACE:
```
33420 TRACE: Goodbye flash old friend, you gave me loads of entertainment. The flag is brixelCTF{n0_m0r3_5upp0rt}
```
