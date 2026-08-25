import platform
import socket
import psutil
from datetime import datetime

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
check_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

report_path = "system-health-checker/system_health_report.txt"

with open(report_path, "w") as report:
    report.write("System Health Checker Report\n")
    report.write("============================\n\n")

    report.write(f"Check Time: {check_time}\n")
    report.write(f"Computer Name: {computer_name}\n")
    report.write(f"Operating System: {operating_system}\n")
    report.write(f"OS Version: {os_version}\n")
    report.write(f"Architecture: {architecture}\n")
    report.write(f"Local IP: {local_ip}\n\n")

    report.write(
        f"CPU Usage: {cpu_usage}% -> {health_status(cpu_usage)}\n"
    )

    report.write(
        f"RAM: {ram_used_gb:.1f} GB / {ram_total_gb:.1f} GB "
        f"-> {ram_usage}% -> {health_status(ram_usage)}\n"
    )

    report.write(
        f"Disk: {disk_used_gb:.1f} GB / {disk_total_gb:.1f} GB "
        f"-> {disk_usage}% -> {health_status(disk_usage)}\n"
    )

    report.write(f"Disk Free: {disk_free_gb:.1f} GB\n")

print("\nCheck Time:", check_time)
print("Report saved to:", report_path)