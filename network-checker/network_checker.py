import socket
import subprocess
import platform

print("Network Checker")

host = input("Enter a host or website: ")

# DNS resolution
print("\n--- DNS Check ---")

try:
    ip_address = socket.gethostbyname(host)
    print("Host:", host)
    print("IP Address:", ip_address)

except socket.gaierror:
    print("DNS: FAILED")
    print("Unable to resolve host.")
    print("Network check stopped safely.")
    exit()

# Ping check
print("\n--- Ping Check ---")

ping_parameter = "-n" if platform.system().lower() == "windows" else "-c"

result = subprocess.run(
    ["ping", ping_parameter, "1", host],
    stdout=subprocess.DEVNULL
)

if result.returncode == 0:
    print("Ping: SUCCESS")
else:
    print("Ping: FAILED")

# Port 443 check
print("\n--- Port Check ---")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

port_result = sock.connect_ex((host, 443))

if port_result == 0:
    print("Port 443: OPEN")
else:
    print("Port 443: CLOSED or unreachable")

sock.close()