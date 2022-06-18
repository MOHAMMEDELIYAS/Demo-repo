import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

ip = "192.168.172.130"
port = 1234

s.bind((ip,port))

s.listen()


# any sender connect : i accept and memorize : maintain connection by accept function
#c , addr = s.accept()

#c.send()
while True:
    c , addr = s.accept()
    #x = c.recv(1024)
    #print(x)
    c.send(b"hi from reciver")
    x = c.recv(1024)
    print(x)
#c.close()
