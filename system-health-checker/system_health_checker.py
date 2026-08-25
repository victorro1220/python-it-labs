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

ram_total_gb = memory.total / (1024 ** 3)
ram_used_gb = memory.used / (1024 ** 3)
ram_usage = memory.percent

disk = psutil.disk_usage("C:\\")

disk_total_gb = disk.total / (1024 ** 3)
disk_used_gb = disk.used / (1024 ** 3)
disk_free_gb = disk.free / (1024 ** 3)
disk_usage = disk.percent

def health_status(value):
    if value < 70:
        return "OK"
    elif value < 85:
        return "WARNING"
    else:
        return "CRITICAL"

print("Computer Name:", computer_name)
print("Operating System:", operating_system)
print("OS Version:", os_version)
print("Architecture:", architecture)
print("Local IP:", local_ip)

print("CPU Usage:", cpu_usage, "% ->", health_status(cpu_usage))
print(
    f"RAM: {ram_used_gb:.1f} GB / {ram_total_gb:.1f} GB "
    f"-> {ram_usage}% -> {health_status(ram_usage)}"
)

print(
    f"Disk: {disk_used_gb:.1f} GB / {disk_total_gb:.1f} GB "
    f"-> {disk_usage}% -> {health_status(disk_usage)}"
)

print(f"Disk Free: {disk_free_gb:.1f} GB")