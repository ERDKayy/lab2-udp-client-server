import sys
import socket

debug = True

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    packet = bytearray()

    for i in range(0, (sys.argv)):
        print("Printing arg #%d :" % (i), end=' ')
        print(sys.argv[i])

    print(" --- ---")
    if sys.argv[2] == "+":
        operator = 4
        operator = operator & 0x000000ff
        print("Operator is \" %s \"" % (sys.argv[2]))
    elif sys.argv[2] == "-":
        operator = 2
        operator = operator & 0x000000ff
        print("Operator is \" %s \"" % (sys.argv[2]))
    elif sys.argv[2] == "*":
        operator = 1
        operator = operator & 0x000000ff
        print("Operator is \" %s \"" % (sys.argv[2]))
    packet.append(operator)

    intCount = int(sys.argv[3])
    intCount += 4

    for j in range(4, intCount):
        value = int(sys.argv[j])
        value = value & 0x000000ff
        packet.append(value)



    print(" --- Packet array and assigned values --- ")
    for i in range(0, len(packet)):
        print("INDEX: %d VALUE:" % (i), end=' ')
        print(packet[i])


    #send to server
    if debug != True:
        s.sendto(packet, ("localhost", int(sys.argv[1])))

        #receive from server
        packet = bytearray(4)
        n = s.recv_into(packet)

        hostInteger = int.from_bytes(packet, byteorder="little", signed=True)

        print("hostInteger: %d" % hostInteger)
