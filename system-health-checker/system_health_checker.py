import platform
import socket
import psutil

print("System Health Checker")

computer_name = socket.gethostname()
operating_system = platform.system()
os_version = platform.version()
architecture = platform.machine()
local_ip = socket.gethostbyname(computer_name)

cpu_usage = psutil.cpu_percent(interval=1)

memory = psutil.virtual_memory()
ram_usage = memory.percent

disk = psutil.disk_usage("C:\\")
disk_usage = disk.percent

print("Computer Name:", computer_name)
print("Operating System:", operating_system)
print("OS Version:", os_version)
print("Architecture:", architecture)
print("Local IP:", local_ip)

print("CPU Usage:", cpu_usage, "%")
print("RAM Usage:", ram_usage, "%")
print("Disk Usage:", disk_usage, "%")