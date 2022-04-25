import os
import ctypes
import platform

trigger = 0
ipaddress = "127.0.0.1"
if platform.system() == "Windows" or platform.system() == "windows" or platform.system() == "WINDOWS":
    while trigger == 0 or input() == input():
        ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
        os.system(f"ping {ipaddress}")
        os.system(f"ping {ipaddress}")
        os.system(f"ping {ipaddress}")
        os.system(f"ping {ipaddress}")
else:
    while trigger == 0 or input() == input():
        os.system(f"ping {ipaddress}")
        os.system(f"ping {ipaddress}")
        os.system(f"ping {ipaddress}")
        os.system(f"ping {ipaddress}")
        os.system(f"ping {ipaddress}")
