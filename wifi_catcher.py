import subprocess
import platform

identify = platform.system()

print(f"Your Operating Platform Is {identify}")

if identify  == "Windows":
    cmd = ["netsh", "wlan", "show", "networks", "mode=BSSID"]
    networks = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, errors = networks.communicate()
    print(output.decode("utf-8"))
    data = output.decode("utf-8")
    f = open("output.txt", "a+")
    f.write(data)
    f.write("\n----------------------------------------------------------------------------")
    f.close()

elif identify == "Linux":
    cmd = ["nmcli", "-f",  "SSID,BSSID,ACTIVE", "dev", "wifi", "list"] 
    networks = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, errors = networks.communicate()
    print(output.decode("utf-8"))
    data = output.decode("utf-8")
    f = open("output.txt", "a+")
    f.write(data)
    f.write("\n----------------------------------------------------------------------------")
    f.close()
else:
    print("Unsupported For Your Operating System/\.")
