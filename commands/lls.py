
import os, subprocess as sp

def client_lls(cmd):
    pass

def server_lls(cmd, data):
    """Run ls command on the server

    Usage: lls -al
    Note: passes all args to the ls command
    """
    pass

def server_lls_custom(cmd):
    cmd = cmd[1:]
    sh = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE, shell=True)
    out, err = sh.communicate()
    print out + err




