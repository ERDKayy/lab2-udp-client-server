import sys
import socket


hostInteger = int()

#start listening - initialize with listening on port argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", int(sys.argv[1])))
packet, address = s.recvfrom(15)
intNum = packet[1]
sum = packet[2]

if packet[0] == 1:
    for i in range(3, len(packet)):
        print("in the + loop")
        sum += packet[i]
    hostInteger = sum
    print("operator received was \"+\"")

elif packet[0] == 2:
    for i in range(3, len(packet)):
        print("in the - loop")
        sum -= packet[i]
    hostInteger = sum
    print("operator received was \"-\"")

elif packet[0] == 4:
    for i in range(3, len(packet)):
        print("in the * loop")
        sum *= packet[i]
    hostInteger = sum
    print("operator received was \"*\"")

packet = hostInteger.to_bytes(4, byteorder="little", signed=True)
s.sendto(packet, address)
s.close()
