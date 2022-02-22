import socket
import random
from time import sleep

host="167.71.170.188"
port=1236


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    number=18
    s.sendall(str(number).encode())
    sleep(0.5)
    data=s.recv(4000)
    output=repr(data)
    print(output[1915:])
    if "Sorry, the correct roll was" in output:
        main()
    else:
        number = 16
        s.sendall(str(number).encode())
        sleep(0.5)
        data = s.recv(4000)
        output = repr(data)
        print(output[1915:])
        if "Sorry, the correct roll was" in output:
            main()
        else:
            print(output)




def roll():
    return random.randint(1,20)


if __name__ == '__main__':
    main()