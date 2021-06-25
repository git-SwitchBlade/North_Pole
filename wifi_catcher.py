import subprocess

networks = subprocess.check_output(["netsh", "wlan", "show", "network"])
decode = networks.decode('ascii')
print(decode)
