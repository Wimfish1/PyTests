import requests
import subprocess
import os
import sys
import time

# URL of the raw script on GitHub
SCRIPT_URL = 'https://raw.githubusercontent.com/Wimfish1/PyTests/main/main.py'
LOCAL_FILE = 'main.py'

def check_for_updates():
    try:
        response = requests.get(SCRIPT_URL)
        response.raise_for_status()

        # Read the remote script
        remote_script = response.text

        # Read the local script
        with open(LOCAL_FILE, 'r') as file:
            local_script = file.read()

        # Compare the scripts
        if remote_script != local_script:
            print('Update available. Updating...')
            time.sleep(5)
            with open(LOCAL_FILE, 'w') as file:
                file.write(remote_script)
            print('Update completed. Restarting...')
            time.sleep(2)
            restart_program()

    except Exception as e:
        print(f'Error checking for updates: {e}')

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

if __name__ == '__main__':
    print("---------------------------")
    print("Awaiting boot...")
    print("---------------------------")
    time.sleep(0.2)
    print("Checking for updates...")
    check_for_updates()
    time.sleep(0.6)
    print("Boot Finished.")
