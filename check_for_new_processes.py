## This code monitors for any new processes that are launched on the system and prints out information about them including the Process ID, Executable Path, and Command Line.

import os
import sys
import collections
import wmi

def check_for_new_processes():
    processes = collections.defaultdict(list)
    listener = wmi.WMI().Win32_Process.watch_for('creation')
    while True:
        try:
            new_process = listener()
            cmdline = new_process.CommandLine
            executable = new_process.ExecutablePath
            pid = new_process.ProcessId
            processes[pid].append(executable)
            if len(processes[pid]) == 1:
                print(f"PID: {pid}\tExecutable: {executable}\tCommandLine: {cmdline}")
        except Exception:
            pass

if __name__ == "__main__":
    check_for_new_processes()
