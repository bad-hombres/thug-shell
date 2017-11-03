import os

def client_edit(command):
    pass

def server_edit(command):
    """Edit a file from the client

    Usage: edit <filename>
    Note: this downloads the file and edits it locally then 
          re uploads it
    """
    pass

def server_edit_custom(command):
    file_name = command.split(" ")[1]
    dowload_command = "download %s %s" % (file_name,"/tmp/tmpfile")
    upload_command = "upload /tmp/tmpfile %s" % file_name
    
    send_data(client, transform_cmd("download", dowload_command))
    response = server_download(dowload_command, recv_data(client))

    print response
    if "downloaded" in response:
        os.system("nano /tmp/tmpfile")
        send_data(client, transform_cmd("upload", upload_command))
        response = server_upload(upload_command, recv_data(client))
        if "uploaded" in response:
            info("Edited %s" % file_name)
        else:
            error("Could not upload %s after editing" % file_name)
    else:
        error("Could not download %s for editing" % file_name)
