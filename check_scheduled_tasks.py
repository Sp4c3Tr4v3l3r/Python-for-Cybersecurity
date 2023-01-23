## This code checks which scheduled tasks are running on the computer.
## It loops through each task and checks if the creator name associated with the task is trusted (in this case, the trusted creators are NVIDIA, Microsoft, and Mozilla).
## It also checks if any of the tasks have an extension that is suspicious (in this case, .exe, .dll, and .py)
## If the task is not from a trusted creator and has a suspicious extension, it prints out the name of the task, the task name, and the creator name

import os, pathlib, subprocess

schtasks = [x.split(',') for x in str(subprocess.check_output("schtasks /query /v /fo csv /nh", shell=True)).split("\\r\\n")]
creator_i_trust = ['NVIDIA', 'Microsoft', 'Mozilla']
extensions_i_suspect_of = ['.exe', '.dll','.py']

for schtask in schtasks:
    values = [y.strip("\"") for y in schtask]
    if len(values) > 8:
        task_name = values[1]
        creator_name = values[7]
        task = values[8]
        trusted_creator = [creator_name for z in creator_i_trust if creator_name.startswith(z)]
        executable_filename = [task for ext in extensions_i_suspect_of if ext in task]
        if not trusted_creator:
            if executable_filename:
                print(f"Task: {task}\n\t Task Name: {task_name}\n\t Creator Name: {creator_name}")
