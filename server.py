import socket


addressBar = list();
server_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)   
server_socket.bind(('fe80::8f6:5e7d:833:fea6%14', 116))              
print "UDPServer Waiting for client on port 900"

while True:
    dataFromClient, address = server_socket.recvfrom(256)
    if(address not in addressBar):
                addressBar.append(address)
    print dataFromClient
    if(len(addressBar)>1):
                for add in addressBar:
                        if(address != add ):
                                server_socket.sendto(dataFromClient, add)
    print addressBar
    
