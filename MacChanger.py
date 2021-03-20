#!

# Imports Subprocess module to allow running bash commands
import subprocess

subprocess.call("ifconfig eth0 down", Shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:55", shell=True)

