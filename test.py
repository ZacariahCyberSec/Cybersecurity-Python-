logins = [
    "success",
    "failed",
    "failed",
    "success",
    "failed",
    "failed",
    "failed"
]

failed_count = 0

for login in logins:
    if login == "failed":
        failed_count += 1

print("Failed login attempts:", failed_count)

if failed_count >= 3:
    print("⚠ ALERT: Possible brute-force attack detected!")