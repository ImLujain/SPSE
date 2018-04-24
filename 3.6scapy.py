#/usr/bin/python

#3.6 scapy

import scapy
from scapy.all import *

#ls() dump all the protocols that scapy support 

#conf show different configration options

#lsc() list command options

#sniff on eth1 and number of packets to sniff is 3 

pkts = sniff(iface="eth0", filter="icmp", count=3)

#tp print packets captured 
print pkts

print pkts[0]
print pkts[0].show() #pretty output :D

# to dump packets in hex we use hexdump
print hexdump(pkts[1])


# to write packets into a file 


wrpcap("demo.pcap", pkts) # filename, list of packets to write 

# to read from pcap file 

read_pkts = rdpcap("demo.pcap")


#to print while capturing we use lambda 

pktss = sniff(iface="eth0", filter="icmp", count=30, prn=lambda x: x.summary()) # or x.show()

#we can export the packet we captured to string 

icmp_str=str(pkts[0])


#in order to reconstruct a packet out of this string we have to know what's the outermost protocol, in this case it's ethernet



recon = Ether(icmp_str)

print recon 

#convert packet to base64 format by exporting it 

export_object(icmp_str)

#import packet from Base64

newPkt = import_object()

Ether(newPkt)

