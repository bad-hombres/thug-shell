def client_help(cmd):
    pass

def server_help(cmd, data):
    """Provides this help screen

    Usage: help
    """
    pass

def server_help_custom(cmd):
    global commands
    parts = cmd.split(" ")
    if len(parts) == 2:
        print commands[parts[1]]["function"].__doc__
    else:
        for cmd in commands.keys():
            print cmd + ": " + commands[cmd]["function"].__doc__.split("\n")[0]

        print "exit: exit the shell"
