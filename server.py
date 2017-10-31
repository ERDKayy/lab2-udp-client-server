import sys
import socket

#start listening - initialize with listening on port argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", int(sys.argv[1])))
packet, address = s.recvfrom(4)

for i in range(0, len(packet)):
    print("Packet index %d is: " % (i), end=' ')
    print(packet[i])


a = packet[1]
print("a was received as: %d" % a)

bit7 = 2**7
test_a = a & bit7
if test_a == bit7:
    #negative number
    a = a - 2**8
print("a is: %d" % a)

b = packet[2]
print("b was received as: %d" % b)

test_b = b & bit7
if test_b == bit7:
    #negative number
    b = b - 2**8
print("b is: %d" % b)

sum = 0
if packet[0] == 4:

    for i in range(1, len(packet)):
        if packet[i] == len(packet):
            break
        sum += packet[i]
    hostInteger = sum
    print("operator received was \"+\"")
elif packet[0] == 2:
    for i in range(1, len(packet)):
        if packet[i] == len(packet):
            break
        sum -= packet[i]
    hostInteger = sum
    print("operator received was \"-\"")
elif packet[0] == 1:
    for i in range(1, len(packet)):
        if packet[i] == len(packet):
            break
        sum *= packet[i]
    hostInteger = sum
    print("operator received was \"*\"")




packet = hostInteger.to_bytes(4, byteorder="little", signed=True)

s.sendto(packet, address)

s.close()
