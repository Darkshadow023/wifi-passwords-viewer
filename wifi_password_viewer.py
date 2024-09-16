import subprocess

# Function to get the list of Wi-Fi profiles
def get_wifi_profiles():
    # Running the command to get Wi-Fi profiles
    command_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    
    # Extracting profile names from the command output
    profiles = [line.split(":")[1][1:-1] for line in command_output if "All User Profile" in line]
    return profiles

# Function to get the Wi-Fi password for each profile
def get_wifi_password(profile):
    # Running the command to get profile details including the password
    profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
    
    # Extracting the password from the profile details
    password = [line.split(":")[1][1:-1] for line in profile_info if "Key Content" in line]
    return password[0] if password else None

# Main code to display Wi-Fi profiles and passwords
def main():
    profiles = get_wifi_profiles()
    
    for profile in profiles:
        password = get_wifi_password(profile)
        if password:
            print("{:<30}|  {:<}".format(profile, password))
        else:
            print("{:<30}|  {:<}".format(profile, "No password found"))

    # Wait for user input before exiting
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
