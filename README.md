```
                ██████████████████████████
                ─██▄▀▄▀█████──██▄▀▄▀█████─
                ──▀██▄█▄██▀────▀██▄█▄██▀──

___________.__                     _________.__           .__  .__   
\__    ___/|  |__  __ __  ____    /   _____/|  |__   ____ |  | |  |  
  |    |   |  |  \|  |  \/ ___\   \_____  \ |  |  \_/ __ \|  | |  |  
  |    |   |   Y  \  |  / /_/  >  /        \|   Y  \  ___/|  |_|  |__
  |____|   |___|  /____/\___  /  /_______  /|___|  /\___  >____/____/
                \/     /_____/           \/      \/     \/           
                (cause thats how we roll homie!)
```

## Install
```
$ pip install docopt
```
I've tried to keep this mainly dependency free

## Commands
New commands go in the commands directory (see existing commands for examples). Basic rundown is

1. the `client_<command name>` method gets executed on the connecting client
2. the `server_<command name>` gets passed the command and the response data from the command and is expected to return a string for display
3. the `server_<command_name>_transform` method if defined is passed the command typed and eis expected to return a new command (see the upload command for an example)
4. the `server_<command_name>_custom` method if defined is the only method called and is generally used to either orchestrate other commands. It must deal with printing its own output etc (see the edit command for an example

## TODO
- Play some gansta ass theme when a connection happens
- Support multi connections?
- SSL?

Who knows I did this for kicks and the code is wonky. Heavilly inspired by https://0x00sec.org/t/how-to-make-a-reverse-tcp-backdoor-in-python-part-1/1038
