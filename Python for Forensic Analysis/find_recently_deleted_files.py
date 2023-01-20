# Find Recently Deleted Files in Windows

# Inspired by TJ O'Connor's book, "Violent Python: A Cookbook for Hackers, Forensic Analysts, Penetration Testers and Security Engineers" (Syngress, 2012, ISBN 978-1-59749-957-6), the script 'find_recently_deleted_files.py' was developed based on the code discussed in the chapter "Using Python to Recover Deleted Items in the Recycle Bin".

"""
Problem:
- You want to find recently deleted files in the Windows Recycle Bin, and print the username associated with those files.

Solution:
- Search the $Recycle.Bin folder on a Windows system.
- Iterate through the directories and look up the user account associated with the SID (security identifier) of the directory.
- Print the username and list of files deleted by the user.
"""

import os
import win32security

def find_recently_deleted_files(path):
    try:
        # Get list of directories
        directory_list = os.listdir(path)
        # Iterate through the directories
        for sid in directory_list:
            # Get list of files in directory
            files = os.listdir(path + sid)
            try:
                # Convert SID to valid SID
                sidtosid = win32security.ConvertStringSidToSid(sid)
                # Look up account SID
                username, domain, type = win32security.LookupAccountSid(None, sidtosid)
            except Exception:
                continue
            # Print user and list of files deleted
            print(f"\nFiles deleted by: {username}\n\tFiles found:")
            for file in files:
                print(f"\t- {file}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    find_recently_deleted_files("C:\\$Recycle.Bin\\")
