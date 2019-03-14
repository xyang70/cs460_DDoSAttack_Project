from __future__ import print_function
import sys
### Only use python 2 for this project...
def main():
	print("\n\nWelcome to DDoS Attack. This tool is developed by Stanley Yang from the University of Illinois at Urbana-Champaign."
	 "This tool is for educational purposes, abusively DDoSing publicly is a federal crime.")
	ip = input("\n Please enter the IP you want to attack:\n")
	method = int(input("\nYou are taking down {}, please select the attack method:"
		"\n 1.TCP_SYN"
		"\n 2.UDP Flood\n".format(ip)))
	ssh_option = input("\n DDoS or DoS?"
		"\n 1.DDoS"
		"\n 2.DoS\n")


	return 0








if __name__ == "__main__":
	main()