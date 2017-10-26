import sys
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    packet = bytearray(2)

    value = int(sys.argv[2])
    value = value & 0x000000ff
    packet[0] = value
    value = int(sys.argv[3])
    value = value & 0x000000ff
    packet[1] = value
    s.sendto(packet, ("localhost", int(sys.argv[1])))
    packet = bytearray(4)
    n = s.recv_into(packet)

    hostInteger = int.from_bytes(packet, byteorder="little", signed=True)

    print("hostInteger: %d" % hostInteger)
