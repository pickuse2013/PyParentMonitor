import os
import time

# Get the PID of the parent process
parent_pid = os.getppid()

# Check interval (in seconds)
interval = 5

print("Parent process ID is:", parent_pid)
print("Checking if parent process is still running... with interval of", interval, "seconds")

while True:
	try:
		# Try to send a signal 0 (which doesn't affect anything) to the parent process,
		# if it exists. If the process doesn't exist, an OSError will be raised.
		os.kill(parent_pid, 0)
		print("It's look like parent process is still running...")
	except OSError:
		# If an OSError is raised, the parent process doesn't exist
		print("parent process does not exist. Exiting...")
		exit(0)

	# Wait for a period of time
	time.sleep(interval)
