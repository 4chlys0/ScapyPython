#! /usr/bin/env python
from scapy.all import *

#Sniff 10 packets
a=sniff(count=10)
#Print Summary
a.nsummary()
