import os

def client_cd(cmd):
    os.chdir(cmd.split(" ")[1])
    return os.getcwd()

def server_cd(command, data):
    """Changes directory in the client process

    Usage: cd /dir
    """
    set_server_path(data)
    return "Ok"

