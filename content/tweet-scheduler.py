import time
import datetime
import schedule

def print_current_time():
    """Print the current time."""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Current time: {current_time}")

# Schedule the tasks
schedule.every().day.at("09:30").do(print_current_time)
schedule.every().day.at("12:00").do(print_current_time)
schedule.every().day.at("20:00").do(print_current_time)

print("Scheduler started. Waiting for scheduled times...")
print("Scheduled times: 9:30 AM, 12:00 PM, and 8:00 PM")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
