## This code monitors a folder and detects any changes made to it, such as the creation, deletion, modification, and renaming of files.
## It then outputs the change that was made and the filename of the file that was changed.

import os
import win32con
import win32file

def check_for_file_changes(path):
    dir = win32file.CreateFile(path, 0x0001, win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE, None, win32con.OPEN_EXISTING, win32con.FILE_FLAG_BACKUP_SEMANTICS, None)
    while True:
        try:
            results = win32file.ReadDirectoryChangesW(dir, 1024, True, win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES | win32con.FILE_NOTIFY_CHANGE_DIR_NAME | win32con.FILE_NOTIFY_CHANGE_FILE_NAME | win32con.FILE_NOTIFY_CHANGE_LAST_WRITE | win32con.FILE_NOTIFY_CHANGE_SECURITY | win32con.FILE_NOTIFY_CHANGE_SIZE, None, None)
            for change, file in results:
                file_name = os.path.join(path, file)
                if change == 1:
                    print(f"Created:\t {file_name}")
                elif change == 2:
                    print(f"Deleted:\t {file_name}")
                elif change == 3:
                    print(f"Modified:\t {file_name}")
                elif change == 4:
                    print(f"Renamed from:\t {file_name}")
                elif change == 5:
                    print(f"Renamed to:\t {file_name}")
        except Exception:
            pass

if __name__ == '__main__':
    folder_path = input("Please enter the folder path to supervise: ")
    check_for_file_changes(folder_path)
