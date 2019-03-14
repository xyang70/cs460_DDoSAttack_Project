import multiprocessing as mp
import threading
import UDP
import TCP_SYN_direct
from __future__ import print_function

#print(mp.cpu_count())

def start_attack_in_multithreading(method,ip):
	num_cpu = mp.cpu_count()
	#print(num_cpu)
	for _ in range(num_cpu):
		t = threading.Thread(target=attack,args=(method,ip,))
		#t.daemon = True
		#print("starting?")
		t.start()


#for worker to attack
def attack(method,ip):
	#print("called")
	#substitude with actual attack
	print("Attacking on %s on %s"%(ip,threading.current_thread().name))



start_attack_in_multithreading("192.168.1.1")
