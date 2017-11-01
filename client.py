import sys
import socket

debug = False

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    packet = bytearray()
    intCount = 0
    for i in range(3, len(sys.argv)):
        intCount += 1


    if sys.argv[2] == "+":
        operator = 1
        operator = operator & 0x000000ff
        operator = operator << 4
    elif sys.argv[2] == "-":
        operator = 2
        operator = operator & 0x000000ff
        operator = operator << 4
    elif sys.argv[2] == "*":
        operator = 4
        operator = operator & 0x000000ff
        operator = operator << 4
    packet1 = operator | intCount
    packet.append(packet1)


    if (intCount % 2 == 0):
        for i in range(3, len(sys.argv), 2):
            value = int(sys.argv[i])
            value = value & 0x000000ff
            value = value << 4
            value2 = int(sys.argv[i+1])
            value = value | value2
            packet.append(value)
    else:
        for i in range(3, len(sys.argv), 2):
            if i == len(sys.argv) - 1:
                value = int(sys.argv[i])
                packet.append(value)
            else:
                value = int(sys.argv[i])
                value = value << 4
                value2 = int(sys.argv[i+1])
                value = value | value2
                packet.append(value)


    #send to server
    if debug != True:
        s.sendto(packet, ("localhost", int(sys.argv[1])))

        #receive from server
        packet = bytearray(4)
        n = s.recv_into(packet)

        hostInteger = int.from_bytes(packet, byteorder="little", signed=True)

        print("hostInteger: %d" % hostInteger)
