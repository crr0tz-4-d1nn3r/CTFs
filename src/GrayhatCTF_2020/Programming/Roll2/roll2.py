import socket
import random
from time import sleep

numbers=['15', '3', '11', '10', '20', '3', '4', '3', '16', '7', '1', 
'12', '7', '10', '7', '12', '8', '8', '19', '20', '12', '1', '13', '7', 
'2', '10', '2', '13', '7', '10', '1', '8', '7', '17', '4', '3', '5', '14', 
'13', '3', '14', '16', '8', '10', '4', '14', '15', '17', '17', '5', '7', '11', 
'10', '20', '18', '19', '3', '11', '15', '16', '17', '14', '20', '4', '17', '4', 
'2', '3', '16', '1', '4', '4', '4', '15', '17', '17', '11', '2', '14', '1', '1', '17', 
'13', '12', '17', '18', '10', '18', '2', '6', '8', '14', '12', '18', '5', '8', '3', '17', 
'5', '18']
host="167.71.170.188"
port=1235


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    for iteration in range(0,1000):
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
        if "{" in output:
            print('flag:\t' + output)
            return 0

def roll():
    return random.randint(1,20)


if __name__ == '__main__':
    main()