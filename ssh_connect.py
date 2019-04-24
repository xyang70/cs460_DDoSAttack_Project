import paramiko

def connect_and_execute(ip,usr,pwd):
	ssh = paramiko.SSHClient()
	#to avoid unkown host exception
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(ip,username = usr, password = pwd)
	except:
		print("Connection failed to {}".format(ip))
		exit(1)
	ssh.close()