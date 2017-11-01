import sys
import socket



while True:
#start listening - initialize with listening on port argv[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", int(sys.argv[1])))
    packet, address = s.recvfrom(15)


    hostInteger = int()
    operator = packet[0]

    operator = operator >> 4
    mask = 2**3 - 1
    intCount = operator & mask

    if operator == 1:
        for i in range(1, len(packet)):
            lsb = packet[i] >> 4
            hostInteger = hostInteger + lsb
            mask = (2**4) - 1
            msb = packet[i] & mask
            hostInteger = hostInteger + msb

    elif operator == 2:
        for i in range(1, len(packet)):
            if i == 1:
                hostInteger = packet[i] >> 4
                mask = 2**4 - 1
                msb = packet[i] & mask
                hostInteger = hostInteger - msb
            else:
                lsb = packet[i] >> 4
                hostInteger = hostInteger - lsb
                mask = (2**4) - 1
                msb = packet[i] & mask
                hostInteger = hostInteger - msb

    elif operator == 4:
        for i in range(1, len(packet)):
            if i == 1:
                hostInteger = packet[i] >> 4
                mask = 2**4 - 1
                msb = packet[i] & mask
                hostInteger = hostInteger * msb
            elif i == len(packet) - 1:
                msb = packet[i] % mask
                hostInteger = hostInteger * msb
            else:
                lsb = packet[i] >> 4
                hostInteger = hostInteger * lsb
                mask = (2**4) - 1
                msb = packet[i] & mask
                hostInteger = hostInteger * msb


    packet = hostInteger.to_bytes(4, byteorder="little", signed=True)
    s.sendto(packet, address)
s.close()
