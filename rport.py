import random

#return a random port
def randomize_port():
	return random.randint(0,65535)
def random_seq():
	return random.randint(1000,9000)
def spoof_ipv4():
	ipv4 = list()
	#initial 3 bits
	ipv4.append(random.randint(0,128))
	for i in range(3):
		ipv4.append(random.randint(0,128))
	addr = str(ipv4[0])+ "." + str(ipv4[1]) + "." + str(ipv4[2]) + "." + str(ipv4[3])
	return addr

#for i in range(100):
#	print(spoof_ipv4())