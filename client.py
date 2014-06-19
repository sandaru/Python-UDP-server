import socket

print "Client 1"
client_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)    #This creates socket

while 1:
    data=raw_input("Message:")
    client_socket.sendto(data, ('fe80::8f6:5e7d:833:fea6%14',116))
    print "Sending request"
    recv_data, addr = client_socket.recvfrom(256)
    print "Message<<Clent2>>",recv_data
client_socket.close()
