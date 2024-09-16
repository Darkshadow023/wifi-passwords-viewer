# Wi-Fi Password Viewer

This script retrieves the list of Wi-Fi profiles stored on your Windows machine and displays the associated passwords (if available). It uses the Windows command-line tool `netsh` to access Wi-Fi profile information and extract the password details for each profile.

## Prerequisites
- This script works on **Windows** machines.
- Python 3.x must be installed.
- The script must be run with **administrator privileges** to access Wi-Fi profiles and passwords.

## How It Works
1. **Get Wi-Fi Profiles**: The `get_wifi_profiles()` function executes the command `netsh wlan show profiles` to retrieve the list of saved Wi-Fi profiles on your system.
   
2. **Get Wi-Fi Passwords**: The `get_wifi_password(profile)` function runs the command `netsh wlan show profile [profile name] key=clear` to extract the password (if available) for each profile.

3. **Display Profiles and Passwords**: In the `main()` function, the script lists all profiles and their corresponding passwords in a formatted output.

## Usage
1. Clone or download the script to your local machine.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with administrator privileges:
   ```bash
   python wifi_password_viewer.py
   ```
4. The script will display each Wi-Fi profile along with its password (if available).

## Example Output

```
WiFi_Network_1               |  password123
WiFi_Network_2               |  No password found
```

The script waits for the user to press **Enter** before closing.

## Notes
- This script **only works on Windows** due to the use of `netsh`.
- It requires **administrator privileges** to retrieve the passwords.
- The passwords will only be displayed if they were saved when the Wi-Fi connection was created.