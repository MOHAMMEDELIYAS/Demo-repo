
import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.connect(("192.168.172.130",1234))

x = s.recv(1024)
s.send(b"data from sender")
#x = s.recv(1024)
print(x)


s.close()	
