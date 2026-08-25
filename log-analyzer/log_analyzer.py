log_file = "log-analyzer/sample_log.txt"

info_count = 0
warning_count = 0
error_count = 0

with open(log_file, "r") as file:
    for line in file:

        if "ERROR" in line:
            error_count += 1

        elif "WARNING" in line:
            warning_count += 1

        elif "INFO" in line:
            info_count += 1

print("Log Analyzer")
print("\n--- Summary ---")

print("INFO:", info_count)
print("WARNING:", warning_count)
print("ERROR:", error_count)