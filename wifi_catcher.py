import subprocess
import platform


identify = platform.system()

if identify == "Windows":
    print(f"Your Operating Platform Is {identify}")
    networks = subprocess.check_output(["netsh", "wlan", "show", "networks","mode=BSSID"])
    decode = networks.decode('ascii')
    print(decode)
else:
    print("Unsupported For Your Operating System/\.")
