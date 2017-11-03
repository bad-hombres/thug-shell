import os

def client_lcd(cmd):
    pass

def server_lcd(cmd, data):
    """Changes the local directory

    Usage: lcd /dir
    """
    pass

def server_lcd_custom(cmd):
    d = " ".join(cmd.split(" ")[1:])
    os.chdir(d)



