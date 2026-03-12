failed_count = 0

with open("auth_log.txt", "r") as log:
    for line in log:
        if "failed" in line:
            failed_count += 1

print("Failed login attempts:", failed_count)

if failed_count >= 3:
    print("⚠ ALERT: Possible brute-force attack detected!")