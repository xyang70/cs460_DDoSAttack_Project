import socket
import pickle

def send_TCP_PACKET(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip, port))
    msg_byte = pickle.dumps(message)
    s.close()

send_TCP_PACKET("192.168.200.5",31337,20000,"xyang70")
