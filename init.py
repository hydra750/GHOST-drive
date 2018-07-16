import os, sys, ctypes
exec(open("config/config.py").read())

# uac elevation
def uac ():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if uac_elevation:
    if not uac():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
