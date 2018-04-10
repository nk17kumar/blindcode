import subprocess
import os

sr = subprocess.call(["sudo", "apt-get", "install", "python-pip"])
sr = subprocess.call(["sudo", "apt-get", "install", "default-jdk"])
sr = subprocess.call(["sudo", "pip", "install", "getch"])
sr = subprocess.call(["sudo", "pip", "install", "gspread"])
sr = subprocess.call(["sudo", "pip", "install", "PyOpenSSL"])
sr = subprocess.call(["sudo", "pip", "install","--upgrade", "oauth2client"])
path = os.path.abspath("..")
os.chdir("/usr/share/applications")
file = open("blindcode.desktop","w")
code = "[Desktop Entry]"+"\n"+"Version=1.0"+ "\n" +"Name=Blind Code"+"\n" +"Type=Application"+"\n" +"Terminal=true"+ "\n"+"Exec= python "+ path + "/src/main.py"+ "\n" + "Icon=" + path + "/resources/icon.jpeg"
file.write(code)
