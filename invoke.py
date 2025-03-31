import subprocess
import threading
import platform
import psutil
import sys
import os

def monitor_child_processes(parent_pid):
    parent = psutil.Process(parent_pid)
    last_children = set(parent.children(recursive=True))
    while True:
        current_children = set(parent.children(recursive=True))
        new_children = current_children - last_children
        if new_children:
            for child in new_children:
                print(f"PID: {child.pid}, {child.cmdline()}")
        last_children = current_children

if __name__ == '__main__':
    process = subprocess.Popen(sys.argv[1:], shell=True, text=True)
    monitor_thread = threading.Thread(target=monitor_child_processes, args=(process.pid,))
    monitor_thread.daemon = True
    monitor_thread.start()
    process.wait()
