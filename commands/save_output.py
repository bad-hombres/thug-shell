
def client_save_output(cmd):
    pass

def server_save_output(cmd, data):
    """Saves the ouput of the previous command to a file

    Usage: save_output <filename>
    """
    pass

def server_save_output_custom(cmd):
    file_name = cmd.split(" ")[1]
    f = open(file_name, "w")
    f.write(get_prev_data())
    f.close()


