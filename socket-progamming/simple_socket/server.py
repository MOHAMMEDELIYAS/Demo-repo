import socket

#udp protocol
myp = socket. SOCK_DGRAM
#net address family : ipv4
afn = socket.AF_INET

s = socket.socket(myp , afn)
ip = "192.168.172.130"
port = 1234

s.bind((ip,port))

while True:

  x = s.recvfrom(1024)
  clientip = x[1][0]
  data = x[0].decode()
  print(data + " " + clientip) 

