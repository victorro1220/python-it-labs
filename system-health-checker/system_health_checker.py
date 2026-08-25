import platform
import socket

print("System Health Checker")

computer_name = socket.gethostname()
operating_system = platform.system()
os_version = platform.version()
architecture = platform.machine()
local_ip = socket.gethostbyname(computer_name)

print("Computer Name:", computer_name)
print("Operating System:", operating_system)
print("OS Version:", os_version)
print("Architecture:", architecture)
print("Local IP:", local_ip)