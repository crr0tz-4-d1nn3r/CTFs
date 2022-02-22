import socket
import random
from time import sleep

numbers=[]
host="167.71.170.188"
port=1234


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    for iteration in range(0,100):
        try:
            number = numbers[iteration]
        except IndexError:
            number = roll()
        
        try:
            s.sendall(str(number).encode())
            sleep(0.25)
            data = s.recv(5000)
        except:
            return 0
        output = data.decode()
        if "Sorry, the roll I was looking for was" in output:
            output = output.split("for was ")[1].split("\\n")[0].strip()
            numbers.insert(iteration,str(output))
            print(numbers)
            s.close()
            main()
        if "TS{" in output:
            print('flag:\t' + output)
            return 0

def roll():
    return random.randint(1,20)


if __name__ == '__main__':
    main()