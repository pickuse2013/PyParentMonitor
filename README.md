# Python Parent Process Monitor (PyParentMonitor)

PyParentMonitor is a Python script designed to continuously monitor the status of its parent process (such as Node.js or others). Its main function is to remember the parent process ID (PID) and routinely check if the parent process is still running.

## Main Features

- **Parent Process Tracking**: Once this script is initiated from another process, it will identify and remember the parent process ID.

- **Status Check**: Regularly checks if the parent process is still active.

- **Auto Termination**: In case the parent process is no longer running, PyParentMonitor will automatically terminate itself, freeing up system resources.

This script is especially useful in scenarios where the parent process may terminate unexpectedly and you want to ensure that no orphaned child processes are left running.

Please note: This script is intended to be used on a single machine, as it requires the ability to signal the parent process. If you want to use it over a network or without such permissions, modifications will be necessary.
