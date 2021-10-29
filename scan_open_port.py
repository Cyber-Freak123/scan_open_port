#!/bin/python

import sys
import socket
import datetime
import threading

target = ''

def check_port(port):
    ''' to check whether the port is open'''
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(5)
    result = s.connect_ex((target,port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()









# just input check
if (len(sys.argv) == 2):
    target = socket.gethostbyname(sys.argv[1]) # translate to ipv4 address
else:
    print("need input to run")
    print("syntax python3 scan_open_port.py <ip> <start-port> <end-port>")
    sys.exit()

#decoartion to script
print("-"*50)
print("scanning port: "+target)
print("Time started: "+str(datetime.time()))
print("-"*50)

try:
    if( len(sys.argv)>4):
        start_port = int(sys.argv[3]) if sys.argv[3] else 0
    else:
        start_port = 0
    if ( len(sys.argv)>5):
        end_port = int(sys.argv[4]) if sys.argv[4] else 65535
    else:
        end_port = 65535
    print(f"scanning start from port {start_port} to {end_port}")
    for port in range(start_port, end_port):
        t= threading.Thread(target=check_port,args=(port,))
        t.start()
except KeyboardInterrupt:
    print("Exiting the Program.....")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("server not reachable")
    sys.exit()
#!/bin/python

import sys
import socket
import datetime
import threading

target = ''

def check_port(port):
    ''' to check whether the port is open'''
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(5)
    result = s.connect_ex((target,port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()









# just input check
if (len(sys.argv) == 2):
    target = socket.gethostbyname(sys.argv[1]) # translate to ipv4 address
else:
    print("need input to run")
    print("syntax python3 scan_open_port.py <ip> <start-port> <end-port>")
    sys.exit()

#decoartion to script
print("-"*50)
print("scanning port: "+target)
print("Time started: "+str(datetime.time()))
print("-"*50)

try:
    if( len(sys.argv)>4):
        start_port = int(sys.argv[3]) if sys.argv[3] else 0
    else:
        start_port = 0
    if ( len(sys.argv)>5):
        end_port = int(sys.argv[4]) if sys.argv[4] else 65535
    else:
        end_port = 65535
    print(f"scanning start from port {start_port} to {end_port}")
    for port in range(start_port, end_port):
        t= threading.Thread(target=check_port,args=(port,))
        t.start()
except KeyboardInterrupt:
    print("Exiting the Program.....")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("server not reachable")
    sys.exit()
