# Simple log analysis: detect repeated failed logins

log_file = "sample.log"

failed_logins = {}

with open(log_file, "r") as file:
    for line in file:
        if "failed" in line.lower():
            ip = line.split()[-1]
            failed_logins[ip] = failed_logins.get(ip, 0) + 1

for ip, count in failed_logins.items():
    if count > 2:
        print(f"[ALERT] {ip} have {count} attempts login failed ")
