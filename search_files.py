import os
import paramiko
import sys
import utility

def print_dir_contents(path):
    """
    function that will list all the directories/files/subdirectories 
    in a given directory
    """
    for i in os.listdir(path):
        childpath = os.path.join(path, i)
        if os.path.isdir(childpath):
            print_dir_contents(childpath)
        else:
            print(childpath)

def ssh_call(server, remote_user, test, password, command="find /tmp -name '*'"):
    """Run a command under SSH."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=remote_user, password=password)
    if test:
        (stdin, stdout, stderr) = ssh.exec_command(command)
        return stdout.readlines()
    else:
        (stdin, stdout, stderr) = ssh.exec_command(command)
    return stdout.readlines()


def list_files():
    options = [{"argument_name": "server", "require": True, "help_string": "give the server IP e.g 192.168.x.x", "custom_name": "server_name","action": "store", "data_type": str},
               {"argument_name": "remote_user", "require": True, "help_string": "give the user e.g inniopark", "custom_name": "remote_user","action": "store", "data_type": str},
               {"argument_name": "password", "require": True, "help_string": "Path of remote server", "custom_name": "password","action": "store", "data_type": str, "default_value": "*"},
               {"argument_name": "test", "require": True, "help_string": "possible values 0 or 1 it will only show the output", "custom_name": "test","action": "store", "data_type": int, "default_value": 1},
               {"argument_name": "extension", "require": True, "help_string": "five a file extension like '*.sql'", "custom_name": "file_extension","action": "store", "data_type": str, "default_value": "*.sql"},
               {"argument_name": "command", "require": False, "help_string": "command to be executed on remote server", "custom_name": "command","action": "store", "data_type": str}]
    PROG = sys.argv[0]
    DESCRIPTION = """
            Program to execute command on a remote server
            ---------------------------------------------
            """
    program_info = {"program_name": PROG, "description": DESCRIPTION}


    obj = utility.CreateArguments(options, program_info)
    ops = obj.create_cli_arguments()

    if ops.command is None:
        l = ssh_call(ops.server_name, ops.remote_user, ops.test, ops.password)
    else:
        l = ssh_call(ops.server_name, ops.remote_user, ops.test, ops.password, ops.command)
    return l

l = ["192.168.116.24"]
master_password = ""
command = "find /tmp -name '*'"
for i in l:
    output = ssh_call(i, "sukhdev", 0, "Mouse@123", command)
    print(i+"@sukhdev")
    for line in output:
        print(line)

