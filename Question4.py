from datetime import datetime

def find_peak_usage(logs):
    # Create a list to store the number of logins for each hour
    hourly_counts = [0] * 24

    # Process each timestamp
    for log in logs:
        timestamp = datetime.fromisoformat(log)
        hour = timestamp.hour
        hourly_counts[hour] += 1

    # Find the hour with the highest number of logins
    peak_hour = hourly_counts.index(max(hourly_counts))

    return peak_hour

logs = [
    "2026-08-04T13:21:18",
    "2026-08-04T13:45:10",
    "2026-08-04T09:15:30",
    "2026-08-04T13:55:42",
    "2026-08-04T09:30:12",
    "2026-08-04T18:20:05"
]

print("Peak usage hour:", find_peak_usage(logs))