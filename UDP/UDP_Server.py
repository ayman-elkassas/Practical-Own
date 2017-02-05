import socket
#determine ip type ( IPv4,IPv6 ) and transimision protocol type ( TCP OR UDP )
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("127.0.0.1",3000)) #bind means join or connect
data,address=sock.recvfrom(1024)
text = data.decode('ascii')