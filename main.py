import requests
import subprocess
import os

# URL of the raw script on GitHub
SCRIPT_URL = 'https://raw.githubusercontent.com/yourusername/yourrepository/main/your_script.py'
LOCAL_FILE = 'your_script.py'

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
            with open(LOCAL_FILE, 'w') as file:
                file.write(remote_script)
            print('Update completed. Restarting...')
            restart_program()

    except Exception as e:
        print(f'Error checking for updates: {e}')

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

if __name__ == '__main__':
    check_for_updates()
    print('Hello, this is the main script!')
