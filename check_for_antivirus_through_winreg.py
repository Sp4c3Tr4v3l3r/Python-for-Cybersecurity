## This code checks to see if any of the given antivirus programs are installed on the system
## It loops through the given registry paths and checks if the given antivirus is installed
## If it is, it prints out a message stating the antivirus is installed in the system

import winreg

reg_hive = winreg.HKEY_LOCAL_MACHINE
reg_paths = ["SOFTWARE\McAfee","SOFTWARE\Symantec", 
             "SOFTWARE\Trend Micro", "SOFTWARE\KasperskyLab", 
             "SOFTWARE\Avast Software", 
             "SOFTWARE\AVG Technologies", 
             "SOFTWARE\Bitdefender", "SOFTWARE\ESET"]

for reg_path in reg_paths:
    try: 
        key = winreg.OpenKey(reg_hive, reg_path, 0, 
                             access=winreg.KEY_READ)
        print(f"It appears that the {reg_path[9:]} antivirus is installed in this system")
    except:
        continue
