# This code will allow a forensics analyst to find out what USB devices have been connected to the system previously. It uses the Windows registry to query for the "FriendlyName" of the USBSTOR devices and prints out the names of each device that has been connected before.

import winreg

def find_previously_connected_usb_devices():
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    key = winreg.OpenKey(reg, r'SYSTEM\ControlSet001\Enum\USBSTOR')

    for i in range(winreg.QueryInfoKey(key)[0]):
        try:
            subkey_name = winreg.EnumKey(key, i)
            subkey = winreg.OpenKey(key, subkey_name)
            for j in range(winreg.QueryInfoKey(subkey)[0]):
                subkey2 = winreg.OpenKey(subkey, winreg.EnumKey(subkey, j))
                friendly_name = winreg.QueryValueEx(subkey2,"FriendlyName")
                print(f'Previously Connected USB Device: {friendly_name[0]}')
        except:
            pass
    winreg.CloseKey(key)

if __name__ == '__main__':
    find_previously_connected_usb_devices()
