def client_hello(cmd):
    return "Hello " + " ".join(cmd.split(" ")[1:])

def server_hello(cmd, response):
    """Test command
    """
    return response

