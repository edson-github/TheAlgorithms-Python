# server.py

import socket

HOST, PORT = '127.0.0.1', 1400

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#refer to client.py
s.bind((HOST, PORT))
s.listen(1)#listen for 1 connection

conn, addr = s.accept()#start the actual data flow

print('connected to:', addr)

while 1:
    if data := conn.recv(1024).decode('ascii'):
        conn.send(f'{data} [ addition by server ]'.encode('ascii'))

    else:
        break
conn.close()
