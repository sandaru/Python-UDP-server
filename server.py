import socket

addressBar = list()#list of active users
#function to get free port from the host
def get_free_port(socket_in_use):
    initial_port_number = 1
    success = False
    while(not success and initial_port_number < 10):
        try:
            socket_in_use.bind(('0.0.0.0',initial_port_number))
            success = True
            #socket_in_use.close()
        except Exception:
            success = False
            initial_port_number=initial_port_number+1
    return initial_port_number

#function to initial handshake
def initiate(address):
    addressBar.append(address)
    #request related data from the database
    #match and send the data


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(get_free_port(server_socket))
try:
    print "UDPServer Waiting for client on port ",port
    while True:
        dataFromClient, address = server_socket.recvfrom(256)
        if(address not in addressBar):
                    initiate(address)
        print dataFromClient
        if(len(addressBar)>1):
                    for add in addressBar:
                            if(address != add ):
                                    server_socket.sendto(dataFromClient, add)
        else:
            server_socket.sendto("No any connected devices", address)
        print addressBar

except Exception, e:
    print "Port in use Error: ", e




