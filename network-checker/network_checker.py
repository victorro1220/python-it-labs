import socket

print("Network Checker")

host = input("Enter a host or website: ")

ip_address = socket.gethostbyname(host)

print("Host:", host)
print("IP Address:", ip_address)