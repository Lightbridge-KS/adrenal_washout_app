# Run This Script from Project Root (Dev Only)
import os
from sys import platform
import subprocess

from pathlib import Path


print(os.getcwd()) # Project root

os.chdir("src") 

print(os.getcwd())

app_name = "AdrenalWashout"


if platform == "darwin":
    print("On Mac")
    # Run on Mac
    cmd_mac_str = f"""
pyinstaller --noconfirm --onedir -n '{app_name}_macos' --windowed --add-data "/Users/kittipos/opt/miniconda3/lib/python3.9/site-packages/customtkinter:customtkinter/" app.py
tar -czf dist/{app_name}_macos.tar.gz dist/{app_name}_macos.app
"""
    subprocess.run(cmd_mac_str, shell=True)
else:
    print("On Windows")
    # Run on Win
    cmd_win_str = f"""
pyinstaller --noconfirm --onefile -n '{app_name}_win' --windowed --add-data "C:\\Users\\prach\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\customtkinter;customtkinter/" app.py
"""
    subprocess.run(cmd_win_str, shell=True)

