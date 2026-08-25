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


# Function to check a port
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    result = sock.connect_ex((host, port))

    sock.close()

    return result == 0


# Common ports
ports = {
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3389: "RDP"
}

print("\n--- Common Port Check ---")

for port, service in ports.items():
    if check_port(host, port):
        print(f"Port {port} ({service}): OPEN")
    else:
        print(f"Port {port} ({service}): CLOSED or unreachable")