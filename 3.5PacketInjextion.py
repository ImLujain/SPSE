#/usr/bin/python

#3.5 packet injection

import socket
import struct 


rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

packet = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x00')

rawSocket.send(packet + "Hi :)")

# to monitor the NW to check if your packet hasbeen sent using tcpdump , tcpdump -vv -XX 
