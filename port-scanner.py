import socket
import  threading

target = "127.0.0.1"

services = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    130: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        service = service.get(port, "Unknown Service")
        print(f"Port {port} is OPEN -> {service}")

    s.close()

for port in range(1, 1025):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
