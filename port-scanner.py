import socket
import  threading

target = input("Enter target IP: ")

print("Scanning target:", target)

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port))

    if result == 0:
        print("Port", port, "is open")

    s.close()

for port in range(1, 1025):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
