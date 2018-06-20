#! /usr/bin/env python

import sys 
from scapy.all import sr1,IP,ICMP

#where sys.argv[1] lets us specify the destination address at the command line
#i.e. >>sudo ./scapysr.py 192.168.1.1
p=sr1(IP(dst=sys.argv[1])/ICMP())
if p:
	p.show()
