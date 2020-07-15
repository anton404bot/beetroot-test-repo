import socket

sock = socket.socket()
sock.connect(('', 6666))
print('connected')

sock.send(b'privet server, ne perepisyvai menia capsom pls')
print('sent')

while True:
    data = sock.recv(1024)
    print('first data')
    if not data:
        break
    print(data)
    sock.close()

print('connected')