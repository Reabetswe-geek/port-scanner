import socket

target = input("Enter target IP: ")

print("Scanning target:", target)

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = s.connect_ex((target, port))

    if result == 0:
        print("Port", port,"is open")

    s.close()
