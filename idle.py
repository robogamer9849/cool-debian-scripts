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
IDLE_THRESHOLD = 300
CHECK_INTERVAL = 10
terminal_pid = None

commands = [
    "cmatrix",
    "pipes.sh",
    "asciiquarium",
    "nyancat",
    "cacafire"
]

def get_idle_time():
    bus = Gio.bus_get_sync(Gio.BusType.SESSION, None)
    proxy = Gio.DBusProxy.new_sync(
        bus,
        Gio.DBusProxyFlags.NONE,
        None,
        "org.gnome.Mutter.IdleMonitor",
        "/org/gnome/Mutter/IdleMonitor/Core",
        "org.gnome.Mutter.IdleMonitor",
        None,
    )
    idle_time_ms = proxy.call_sync("GetIdletime", None, Gio.DBusCallFlags.NONE, -1, None)
    return idle_time_ms.unpack()[0] // 1000  # convert to seconds

while True:
    try:
        idle_time = get_idle_time()
        # print(idle_time)
        if idle_time >= IDLE_THRESHOLD:
            if terminal_pid is None:
                print(f"User idle for {idle_time}s. Launching cmatrix...")
                cmd_num = random.randint(0, 4)
                cmd = commands[cmd_num]
                proc = subprocess.Popen([term, "--start-as=fullscreen","env", "TERM=xterm-256color", cmd])
                terminal_pid = proc.pid
                # print(terminal_pid)
        else:
            if terminal_pid is not None:
                print(f"User active again. Closing cmatrix...")
                subprocess.call(["pkill", term])
                terminal_pid = None
                cmd = None
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(CHECK_INTERVAL)
