# Network Checker

A simple Python networking tool for IT support and troubleshooting.

## Features

- DNS resolution
- Ping connectivity check
- Common TCP port checks
- Automatic text report generation
- Basic error handling

## Common ports checked

- 22 - SSH
- 53 - DNS
- 80 - HTTP
- 443 - HTTPS
- 3389 - RDP

## How to run

```bash
python network_checker.py
```

## Example output

```text
Host: google.com
IP Address: 142.251.214.174

Ping: SUCCESS

Port 22 (SSH): CLOSED or unreachable
Port 53 (DNS): CLOSED or unreachable
Port 80 (HTTP): OPEN
Port 443 (HTTPS): OPEN
Port 3389 (RDP): CLOSED or unreachable
```

## What I learned

- Python variables and user input
- Functions
- `if` / `else` conditions
- `try` / `except` error handling
- Loops and dictionaries
- TCP sockets
- DNS resolution
- Running system commands with `subprocess`
- Reading and writing files
- Git and GitHub workflow
