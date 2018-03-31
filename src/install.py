import subprocess
import os
from main import project_path

path = os.path.abspath("..")
# project_path.set_path(path+"/src")
sr = subprocess.call(["sudo", "apt-get", "install", "python-pip"])
sr = subprocess.call(["sudo", "apt-get", "install", "default-jdk"])
sr = subprocess.call(["sudo", "pip", "install", "getch"])
sr = subprocess.call(["sudo", "pip", "install", "gspread"])
sr = subprocess.call(["sudo", "pip", "install", "PyOpenSSL"])
sr = subprocess.call(["sudo", "pip", "install","--upgrade" "oauth2client"])
code = "\"[Desktop Entry]"+"\n"+"Version=1.0"+ "\n" +"Name=Blind Code"+"\n" +"Type=Application"+"\n" +"Terminal=true"+ "\n"+"Exec= gksu python "+ path + "/src/main.py"+ "\n" + "Icon=" + path + "/resources/icon.jpeg\""
os.chdir("/usr/share/applications")
sr = subprocess.call(["sudo", "touch", "blindcode.desktop"])
sr = subprocess.call(["sudo", "echo", code , ">>" , "blindcode.desktop"])