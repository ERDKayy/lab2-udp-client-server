import sys
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", int(sys.argv[1])))
packet, address = s.recvfrom(2)
a = packet[0]
print("a was received as: %d" % a)

bit7 = 2**7
test_a = a & bit7
if test_a == bit7:
    #negative number
    a = a - 2**8
print("a is: %d" % a)

b = packet[1]
print("b was received as: %d" % b)

test_b = b & bit7
if test_b == bit7:
    #negative number
    b = b - 2**8
print("b is: %d" % b)
hostInteger = a + b
packet = hostInteger.to_bytes(4, byteorder="little", signed=True)

s.sendto(packet, address)

s.close()
