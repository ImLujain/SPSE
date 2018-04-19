#!/usr/bin/python

import socket
import struct
import binascii

#PF_PACKET = use packet interface
#SOCK.RAW = to indicate that it's a raw socket
#htons, 0x0800 = tells th kernel which protocol we are interested in 
# we can find the protocols in /usr/include/linux/if_ether.h 


rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

#recvfrom = to read a packet
pkt = rawSocket.recvfrom(2048)

#parse the packet 
ethernetHeader = pkt[0][0:14]

#first 6 bytes are dest MAC address and the next are the source and the last 2 are the ethernet bytes

eth_hdr  =struct.unpack("!6s6s2s", ethernetHeader)

#conver the output to hex

binascii.hexlify(eth_hdr[0])
binascii.hexlify(eth_hdr[1])
binascii.hexlify(eth_hdr[2])

IPHeader = pkt[0][14:34]

ip_hdr= struct.unpack("12s4s4s", IPHeader)

#ntoa = network to ascii

print "Source ip adress : " + socket.inet_ntoa(ip_hdr[1])

print "Destination ip adress : " + socket.inet_ntoa(ip_hdr[2])

#unpack and find the ports 

tcpHeader = pkt[0][34:54]

tcp_hdr = struct.unpack("!HH16s", tcpHeader)
sport = str(tcp_hdr[0])
dport = str(tcp_hdr[1])

print "Source Port : ", sport
print "Destination port: ", dport


