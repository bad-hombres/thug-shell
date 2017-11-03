import os

def client_exec_script(cmd):
    pass

def server_exec_script(cmd):
    """Upload a local script and execute on the client

    Usage: exec_script <local_script>
    """
    pass

def server_exec_script_custom(full_command):
    file_name = command.split(" ")[1]
    upload_command = "upload " + file_name
    file_name = os.path.basename(file_name)

    send_data(client, transform_cmd("upload", upload_command))
    response = server_upload(upload_command, recv_data(client))

    if "uploaded" in response:
        _, ext = os.path.splitext(file_name)
        cmd = "exec %s " + file_name
        if ext == ".py":
            cmd = cmd % "python"
        elif ext == ".rb":
            cmd = cmd % "ruby"
        elif ext == ".pl":
            cmd = cmd % "perl"
        elif ext == ".sh":
            cmd = cmd % "bash"
        elif ext == ".cmd":
            cmd = cmd % "cmd /c"
        elif ext == ".bat":
            cmd = cmd % "cmd /c"
        elif ext == ".exe":
            cmd = ".\\"
        else:
            cmd = "chmod +x ./" + file_name + " && ./" + file_name

        send_data(client, cmd)
        print(recv_data(client))

    else:
        error("Could not upload %s" % file_name) 
