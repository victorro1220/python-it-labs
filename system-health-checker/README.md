\# System Health Checker



A simple Python tool for checking basic system health information on a Windows computer.



\## Features



\- Computer name detection

\- Operating system information

\- System architecture detection

\- Local IP detection

\- CPU usage monitoring

\- RAM usage and capacity

\- Disk usage and free space

\- Health status classification

\- Timestamp generation

\- Automatic text report generation



\## Health status levels



\- OK: below 70%

\- WARNING: 70% to 84.9%

\- CRITICAL: 85% or higher



\## How to run



```bash

python system\_health\_checker.py

```



\## Example output



```text

System Health Checker

Computer Name: Victor

Operating System: Windows

OS Version: 10.0.26200

Architecture: AMD64

Local IP: 192.168.100.21



CPU Usage: 3.1 % -> OK

RAM: 6.5 GB / 7.8 GB -> 84.3% -> WARNING

Disk: 40.4 GB / 476.1 GB -> 8.5% -> OK

Disk Free: 435.6 GB



Check Time: 2026-08-25 14:25:10

Report saved to: system-health-checker/system\_health\_report.txt

```



\## Requirements



This project uses:



```bash

pip install psutil

```



\## What I learned



\- Python variables

\- Functions

\- `if`, `elif`, and `else`

\- Working with percentages

\- Converting bytes to gigabytes

\- Using the `platform` module

\- Using the `socket` module

\- Using the `psutil` library

\- Working with date and time

\- Writing data to files

\- Using `.gitignore`

\- Git and GitHub workflow

