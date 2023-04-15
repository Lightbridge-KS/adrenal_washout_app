# Run This Script from Project Root (Dev Only)
import os
import subprocess
from sys import platform
from pathlib import Path

app_name = "AWC"



print(os.getcwd()) # Project root

os.chdir("src") 

print(os.getcwd())

home_dir = str(Path.home()) # User Home Directory


if platform == "darwin":
    print("On Mac")
    # Run on Mac
    cmd_mac_str = f"""
pyinstaller --noconfirm --onedir -n '{app_name}' --windowed --add-data "{home_dir}/opt/miniconda3/lib/python3.9/site-packages/customtkinter:customtkinter/" --icon="assets/app.ico" app.py
cd dist
tar -czf {app_name}-macos.tar.gz {app_name}.app
"""
    subprocess.run(cmd_mac_str, shell=True)
    # print(cmd_mac_str)
else:
    print("On Windows")
    # Run on Win
    cmd_win_str = fr"""
pyinstaller --noconfirm --onefile -n {app_name} --windowed --add-data "{home_dir}\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\customtkinter;customtkinter/" --icon="assets\\app.ico" app.py
""" 
    os.system(cmd_win_str)
    # Zip File
    os.chdir("dist") 
    os.system(f"powershell -Command Compress-Archive -Path {app_name}.exe -DestinationPath {app_name}-win.zip")
    #print(cmd_win_str)
    #subprocess.run(cmd_win_str, shell=True) # Not work
