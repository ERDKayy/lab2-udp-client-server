import sys
import socket

debug = False

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    packet = bytearray(3)

    for i in range(0, len(sys.argv)):
        print("Printing arg #%d :" % (i), end=' ')
        print(sys.argv[i])

    print(" --- Entering if statements ---")
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

    packet[0] = operator
    print(" --- Beginning masking --- ")
    value = int(sys.argv[3])
    value = value & 0x000000ff
    mask = bin(value)
    print("argv (3) value is the binary # of " + mask + " after mask...")
    packet[1] = value

    value = int(sys.argv[4])
    value = value & 0x000000ff
    mask = bin(value)
    print("argv (4) value is the binary # of " + mask + " after mask...")
    packet[2] = value

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
