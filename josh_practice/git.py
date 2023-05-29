#!/usr/bin/env python3 

# We going to use both subprocess and os.system 
import os 
import subprocess

# Let define a function to check whether git is installed 
def is_git_installed():
    git_installed = os.system(" command -v git &>/dev/null")==0

    if git_installed:
        print(" Git is installed and in the most latest version")
    else:
        print("Git installing")

# Moving on from here, we are going to use subprocess module
# Remember this is a list []
def installing_git():
    subprocess.run(['apt','install','git','-y'])

def message_on_screen():
    subprocess.run(['echo','=====END===='])

# Let us now run the functions 
is_git_installed()
installing_git()
message_on_screen()