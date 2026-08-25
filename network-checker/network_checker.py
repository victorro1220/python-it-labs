import socket
import subprocess
import platform


def resolve_dns(host):
    print("\n--- DNS Check ---")

    try:
        ip_address = socket.gethostbyname(host)
        print("Host:", host)
        print("IP Address:", ip_address)

        return ip_address

    except socket.gaierror:
        print("DNS: FAILED")
        print("Unable to resolve host.")

        return None


def ping_host(host):
    print("\n--- Ping Check ---")

    ping_parameter = "-n" if platform.system().lower() == "windows" else "-c"

    result = subprocess.run(
        ["ping", ping_parameter, "1", host],
        stdout=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print("Ping: SUCCESS")
        return "SUCCESS"

    else:
        print("Ping: FAILED")
        return "FAILED"


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

    port_results = []

    for port, service in ports.items():

        if check_port(host, port):
            status = "OPEN"
        else:
            status = "CLOSED or unreachable"

        print(f"Port {port} ({service}): {status}")

        port_results.append(
            f"Port {port} ({service}): {status}"
        )

    return port_results


def save_report(host, ip_address, ping_status, port_results):

    report_path = "network-checker/network_report.txt"

    with open(report_path, "w") as report:

        report.write("Network Checker Report\n")
        report.write("======================\n\n")

        report.write(f"Host: {host}\n")
        report.write(f"IP Address: {ip_address}\n\n")

        report.write(f"Ping: {ping_status}\n\n")

        report.write("Common Ports:\n")

        for result in port_results:
            report.write(result + "\n")

    print(f"\nReport saved to: {report_path}")


print("Network Checker")

host = input("Enter a host or website: ")

ip_address = resolve_dns(host)

if ip_address:

    ping_status = ping_host(host)

    port_results = check_common_ports(host)

    save_report(
        host,
        ip_address,
        ping_status,
        port_results
    )

else:
    print("Network check stopped safely.")