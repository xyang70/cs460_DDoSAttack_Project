import paramiko

def connect_and_execute(ip,usr,pwd):
	ssh = paramiko.SSHClient()
	#to avoid unkown host exception
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip,username = usr, password = pwd)
	ssh_stdin, ssh_stdout,ssh_stderr = ssh.exec_command("ls")

	for line in ssh_stdout:
		print('... ' + line.strip('\n'))
	#close client after connected and have used command
	ssh.close()
