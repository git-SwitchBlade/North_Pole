import platform
import os


identify = platform.system()

if identify == "Windows":
    print(f"Your Operating Platform Is {identify}")
    os.system("netsh wlan show networks mode=BSSID")

elif identify == "Linux":
    print(f"Your Operating Platform Is {identify}")
    os.system("nmcli -f SSID,BSSID,ACTIVE dev wifi list")


else:
    print("Unsupported For Your Operating System/\.")
