## This program checks for autoruns in the Windows registry.
## It looks for autoruns in the HKEY_CURRENT_USER and HKEY_LOCAL_MACHINE hives in the SOFTWARE\Microsoft\Windows\CurrentVersion\Run and SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce paths.
## If any autoruns are found, the program will print the name and data of each autorun it finds

import winreg

HIVES = {
	"HKCU": winreg.HKEY_CURRENT_USER,
	"HKLM": winreg.HKEY_LOCAL_MACHINE
}
PATHS = [
	"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
	"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"
]

def check_autoruns():
	for hive in HIVES:
		for path in PATHS:
			autoruns = []
			try:
				key = winreg.OpenKey(HIVES[hive], path)
				num_values = winreg.QueryInfoKey(key)[1]
			except:
				print("The specified path does not exist")
			for x in range(num_values):
				try:
					name, data, _ = winreg.EnumValue(key, x)
				except:
					continue
				if len(name) > 0:
					autoruns.append([name, data])
			if autoruns:
				print(f"\nAutoruns detected at {hive}\\{path}\n")
				for autorun in autoruns:
					print(f"\t{autorun[0]}: {autorun[1]}")
if __name__ == '__main__':
    check_autoruns()
