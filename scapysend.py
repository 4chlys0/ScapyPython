#! /usr/bin/env python

from scapy.all import *

# where send transmits packets at Layer 3
send(IP(dst="192.168.1.1")/ICMP())
# where sendp transmits packets at Layer 2
sendp(Ether()/IP(dst="192.168.1.1",ttl=(1,4)),iface="enxa0cec805c395")
