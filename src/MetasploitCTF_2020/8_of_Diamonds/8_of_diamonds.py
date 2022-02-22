import socket
import re

host='172.15.41.117'
port=5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, int(port)))
data = b'some data'

move_right = b'C\r\n'
move_left = b'D\r\n'

hostile_indx = [-33,-20]
player_indx = [-16, -3]

while len(data) > 1:
    data = s.recv(5000)
    print(data[6:].decode())
    hostile = data[hostile_indx[0]:hostile_indx[1]].decode()
    player = data[player_indx[0]:player_indx[1]].decode()
    pi = player.find('^')
    if '0' in hostile:
        # see if we need to dodge
        hi = [m.start() for m in re.finditer('0', hostile)]     
        if pi in hi:
            if pi < 12: 
                if pi+1 not in hi:
                    s.sendall(move_right)
                else:
                    s.sendall(move_left)
            else:
                s.sendall(move_left)
    # get away from the walls
    else:
        if pi == 0:
            s.sendall(move_right)
        if pi == 12:
            s.sendall(move_left)