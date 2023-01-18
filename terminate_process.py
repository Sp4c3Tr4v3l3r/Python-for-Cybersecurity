## This code takes a user input of a process name and then search the list of active processes for that process name.
## If it finds the process it terminates it using the SIGTERM signal

import psutil,os,signal

def close_process(processes_to_terminate):
    for process in psutil.process_iter():
        if processes_to_terminate in process.name():
            try:
                print(f"\nProcess named {processes_to_terminate} with PID {process.pid} was terminated")
                os.kill(process.pid, signal.SIGTERM)
            except:
                continue

if __name__ == '__main__':
    processes_to_terminate = input("Input the name of the application you want to close: ")
    close_process(processes_to_terminate)
