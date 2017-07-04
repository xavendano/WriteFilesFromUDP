import socket
import datetime
UDP_IP = "127.0.0.1"
UDP_PORT = 9999
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(("", UDP_PORT))
print("Escuchando...")
while True:
    data, addr = sock.recvfrom(4096) # buffer size is 1024 bytes
    t = datetime.datetime.now()
    f = open(t.strftime('%Y%m%d%H%M%S')+".json", 'w')
    data = str(data).replace("'","").replace("b","")
    f.write(str(data))  # python will convert \n to os.linesep
    print(data)
    f.close()