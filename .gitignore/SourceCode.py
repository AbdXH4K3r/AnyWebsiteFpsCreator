import socket
import threading
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print"""\033[93m
+==========================+==========================+
|              CODED BY ABDXSLAYER                    |
|          E-MAIL : AS8APPLE@GMAIL.COM                |
+==========================+==========================+\033[0m"""
file = raw_input("Choose A File Directory (html,php...): ")
bind_ip   = "0.0.0.0"
bind_port = 80
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)
print "[+] Listening on %s:%d" % (bind_ip,bind_port)
# this is our client-handling thread

def handle_client(client_socket):
# print out what the client sends
    request = client_socket.recv(1024)
    print "[+] Received: %s" % request
    # send back a packet
    f = open(file,'r')
    name = f.read()
    client_socket.send(name)
    client_socket.close()
while True:
    client,addr = server.accept()
    print "[+] Accepted connection from: %s:%d" % (addr[0],addr[1])
    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
    
    
