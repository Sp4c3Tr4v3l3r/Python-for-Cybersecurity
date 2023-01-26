# Windows Registry - Autorun Keys Monitoring

### Problem:
You want to monitor the Windows Registry specifically the Autorun keys to identify any suspicious executables achieving persistence across reboots or user logouts.

### Solution:
Look for autoruns in the ```HKEY_CURRENT_USER``` and ```HKEY_LOCAL_MACHINE``` hives in the ```SOFTWARE\Microsoft\Windows\CurrentVersion\Run``` and ```SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce``` paths. Then, print the name and data of each autorun found.

#### autorun_keys_monitoring.py
```python
import winreg

HIVES = {
	"HKCU": winreg.HKEY_CURRENT_USER,
	"HKLM": winreg.HKEY_LOCAL_MACHINE
}
PATHS = [
	"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
	"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"
]

def autorun_keys_monitoring():
	# Loop over the hives in the HIVE dictionary
	for hive in HIVES:
		# Loop over the paths in the PATHS list
		for path in PATHS:
			autoruns = []
			try:
				# Open the key in the Windows Registry
				key = winreg.OpenKey(HIVES[hive], path)
				# Get the number of values in the key
				num_values = winreg.QueryInfoKey(key)[1]
			except:
				print("The specified path does not exist")
			for x in range(num_values):
				try:
					# Get the name and data for each value
					name, data, _ = winreg.EnumValue(key, x)
				except:
					continue
				# Check if the name is not empty
				if len(name) > 0:
					# If not empty, add the name and data to the autoruns list
					autoruns.append([name, data])
			if autoruns:
				print(f"\nAutoruns detected at {hive}\\{path}\n")
				for autorun in autoruns:
					print(f"\t{autorun[0]}: {autorun[1]}")

if __name__ == '__main__':
    autorun_keys_monitoring()
```
<br/>

##  [Inspired by Python for Cybersecurity](https://www.wiley.com/en-ie/Python+for+Cybersecurity:+Using+Python+for+Cyber+Offense+and+Defense-p-9781119850649)
<blockquote>
Inspired by Howard E. Poston III's book, "Python for Cybersecurity" (Wiley, 2020, ISBN 978-1-119-85064-9), the script 'autorun_keys_monitoring.py' was developed based on the code discussed in the "Maintaining Persistence" chapter, in the "Registry Monitoring for Defenders" topic.
</blockquote>
