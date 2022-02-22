import socket
import random
from time import sleep

numbers=[]
host="159.203.81.45"
port=1235


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    for iteration in range(0,10000):
        try:
            number = numbers[iteration]
        except IndexError:
            number = roll()
        
        try:
            s.sendall(str(number).encode())
            sleep(1)
            data = s.recv(5000)
        except:
            print('connection error')
            print(output)
            return 0
        output = repr(data)
        if "Sorry, the roll I was looking for was" in output:
            output = output.split("for was ")[1].split("\\n")[0]
            numbers.insert(iteration,str(output))
            print(numbers)
            s.close()
            main()
        if "ts{" in output:
            print('flag:\t' + output.decode())
            return 0
        



def roll():
    return random.randint(1,20)


if __name__ == '__main__':
    main()