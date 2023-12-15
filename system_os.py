import subprocess
import platform

def get_system_details():
  # """Gets system details including installed software names."""

  # Get the system/OS name
  system_name = platform.system()

  # Get the system's release version
  system_release = platform.release()

  # Get the OS, version, etc. together
  system_info = platform.platform()

  # Get the installed software names
  # software_names = subprocess.check_output(["apt", "list", "--installed"])

  return system_name, system_release, system_info, #software_names

# if __name__ == "__main__":
#     system_name, system_release, system_info, software_names = get_system_details()
print(get_system_details())
    # print("System name:", system_name)
    # print("System release:", system_release)
    # print("System info:", system_info)
    # print("Software names:", software_names)