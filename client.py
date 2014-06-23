import socket

print "Client 1"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#This creates socket

while 1:
    data=raw_input("Message:")
    client_socket.sendto(data, ('127.0.0.1',6))
    print "Sending request"
    recv_data, addr = client_socket.recvfrom(256)
    print "Message<<Clent2>>",recv_data
client_socket.close()
