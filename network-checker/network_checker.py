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

# Ask for port
print("\n--- Port Check ---")

try:
    port = int(input("Enter a port to check: "))

    if port < 1 or port > 65535:
        print("Invalid port. Use a number between 1 and 65535.")
        exit()

except ValueError:
    print("Invalid input. Port must be a number.")
    exit()

# Port check
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

port_result = sock.connect_ex((host, port))

if port_result == 0:
    print(f"Port {port}: OPEN")
else:
    print(f"Port {port}: CLOSED or unreachable")

sock.close()