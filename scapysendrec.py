#! /usr/bin/env python

from scapy.all import *

#Send and recieve packets

#Where "sr()" is send/recieve function
#sr/sr1 functions reference layer 3, srp/srp1 reference layer 2 packets
ans,unans=sr(IP(dst="192.168.1.1",ttl=5)/ICMP())
ans.nsummary()
unans.nsummary()
p=sr1(IP(dst="192.168.1.1")/ICMP()/"XXXXXX")
p.show()
