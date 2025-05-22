#!/usr/bin/env python3
#   install these for this to work:
#       sudo apt install kitty cmatrix nyancat libcaca0 
#   and these ones that cant be installed by apt:
#       snap install asciiquarium
#       
#       and for pipes.sh you have to search and install it from github


import gi
import subprocess
import time
import random

gi.require_version('Gio', '2.0')
from gi.repository import Gio

# Idle time threshold (in seconds)
term="kitty"
CHECK_INTERVAL = 2.5
terminal_pid = None

commands = [
    "cmatrix",
    "pipes.sh",
    "asciiquarium",
    "nyancat",
    "cacafire"
]
try:
    print(f"User idle. Launching...")
    cmd_num = random.randint(0, 4)
    cmd = commands[cmd_num]
    print([term, "--start-as=fullscreen","env", "TERM=xterm-256color", cmd])
    proc = subprocess.Popen([term, "--start-as=fullscreen","env", "TERM=xterm-256color", cmd])
    with open('terminal_pid.txt', 'w') as file:
        file.write(str(proc.pid))
except Exception as e:
    print(f"Error: {e}")