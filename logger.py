end_color = '\033[0m'

def red(text):
    return '\033[91m' + text + end_color

def blue(text):
    return '\033[94m' + text + end_color

def green(text):
    return '\033[92m' + text + end_color

def yellow(text):
    return '\033[93m' + text + end_color

def lgrey(text):
    return '\033[2m' + text + end_color

def grey(text):
    return '\033[90m' + text + end_color

def strike(text):
    return '\033[9m' + text + end_color

def underline(text):
    return '\033[4m' + text + end_color

def log(symbol, text):
    print "[%s] %s" % (symbol,text)

def info(text):
    log(green("+"), green(text)) 

def warn(text):
    log(yellow("!"),yellow(str(text)))

def error(text):
    log(red("*"), red(str(text)))

def output(text):
    log(grey("-"), grey(str(text)))
