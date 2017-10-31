import sys
import socket

debug = False

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    packet = bytearray()

    if sys.argv[2] == "+":
        operator = 4
        operator = operator & 0x000000ff
    elif sys.argv[2] == "-":
        operator = 2
        operator = operator & 0x000000ff
    elif sys.argv[2] == "*":
        operator = 1
        operator = operator & 0x000000ff
    packet.append(operator)

    for i in range(3, len(sys.argv)):
        value = int(sys.argv[i])
        value = value & 0x000000ff
        packet.append(value)


    #send to server
    if debug != True:
        s.sendto(packet, ("localhost", int(sys.argv[1])))

        #receive from server
        packet = bytearray(4)
        n = s.recv_into(packet)

        hostInteger = int.from_bytes(packet, byteorder="little", signed=True)

        print("hostInteger: %d" % hostInteger)
