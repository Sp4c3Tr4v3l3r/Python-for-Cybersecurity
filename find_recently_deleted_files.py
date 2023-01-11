## This code searchs the $Recycle.Bin folder on a Windows system to find recently deleted files.
## It looks for folders with a SID (Security Identifier) as their name and then look up the username associated with that SID.
## It then prints the list of deleted files and the username of the user who deleted them.

import os
import win32security

def find_recently_deleted_files(path):
    try:
        directory_list = os.listdir(path)
        for sid in directory_list:
            files = os.listdir(path + sid)
            try:
                sidtosid = win32security.ConvertStringSidToSid(sid)
                username, domain, type = win32security.LookupAccountSid(None, sidtosid)
            except Exception:
                continue
            print(f"\nFiles deleted by: {username}\n\tFiles found:")
            for file in files:
                print(f"\t- {file}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    find_recently_deleted_files("C:\\$Recycle.Bin\\")
