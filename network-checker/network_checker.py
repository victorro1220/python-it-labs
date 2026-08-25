import socket
import subprocess
import platform


def resolve_dns(host):
    print("\n--- DNS Check ---")

    try:
        ip_address = socket.gethostbyname(host)
        print("Host:", host)
        print("IP Address:", ip_address)
        return True

    except socket.gaierror:
        print("DNS: FAILED")
        print("Unable to resolve host.")
        return False


def ping_host(host):
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


def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    result = sock.connect_ex((host, port))

    sock.close()

    return result == 0


def check_common_ports(host):
    print("\n--- Common Port Check ---")

    ports = {
        22: "SSH",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS",
        3389: "RDP"
    }

    for port, service in ports.items():
        if check_port(host, port):
            print(f"Port {port} ({service}): OPEN")
        else:
            print(f"Port {port} ({service}): CLOSED or unreachable")


print("Network Checker")

host = input("Enter a host or website: ")

if resolve_dns(host):
    ping_host(host)
    check_common_ports(host)
else:
    print("Network check stopped safely.")