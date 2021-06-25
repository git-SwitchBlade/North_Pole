import subprocess

networks = subprocess.check_output(["netsh", "wlan", "show", "all"])
decode = networks.decode('ascii')
print(decode)
