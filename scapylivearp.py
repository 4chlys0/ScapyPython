#! /usr/bin/env python

from scapy.all import *

def arp_monitor_callback(pkt):
#if packet is ARP and operation mode is "who-has" or "is-at"
#Assuming "op" references the arp operation field, modes 3 and 4 are for reverse arp
#source: http://www.erg.abdn.ac.uk/users/gorry/course/inet-pages/arp.html 
#https://en.wikipedia.org/wiki/Reverse_Address_Resolution_Protocol
	if ARP in pkt and pkt[ARP].op in (1,2):
#return source IP/MAC 
		return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")

sniff(prn=arp_monitor_callback, filter="arp", store=0)
