#! /usr/bin/env python

from scapy.all import *

#Send and recieve packets

#Where "sr()" is send/recieve function
#sr/sr1 functions reference layer 3, srp/srp1 reference layer 2 packets
ans,unans=srp(Ether()/IP(dst="192.168.1.1",ttl=(1,4)),iface="enxa0cec805c395")
ans.nsummary()
unans.nsummary()
p=srp1(Ether()/IP(dst="192.168.1.1",ttl=(1,4)),iface="enxa0cec805c395")
p.show()
