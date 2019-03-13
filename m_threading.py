import multiprocessing as mp
import threading 


#print(mp.cpu_count())

def start_attack_in_multithreading(ip):
	num_cpu = mp.cpu_count()
	#print(num_cpu)
	for _ in range(num_cpu):
		t = threading.Thread(target=attack,args=(ip,))
		t.daemon = True
		#print("starting?")
		t.start()



def attack(ip):
	#print("called")
	#substitude with actual attack
	print("Attacking on %s on %s"%(ip,threading.current_thread().name))



start_attack_in_multithreading("192.168.1.1")
