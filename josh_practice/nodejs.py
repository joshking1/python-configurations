#!/usr/bin/env python3 

# We are going to use both subprocess and os.system 

import os 
import subprocess

# Let us create a function that will check whether the nodejs binary exists
def does_nodejs_exists():
    # Let us create a variable we will use to check the true statement 
    node_js_installed = os.system(' command -v node &>/dev/null') == 0

    if node_js_installed == True:

        print("Nodejs installed and in its latest version")

    else: 

        print (" Nodejs is not installed and will be installing shortly...........")

# Now we move to the usage of subprocess module that is more flexible
# We started by updating the system
def update_the_system():
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'upgrade','-y'])

# Let us now install nodejs

def install_nodejs():
    subprocess.run(['sudo', 'apt','install','nodejs','-y'])
    subprocess.run(['node','-v'])

def final_message():
    subprocess.run(['echo','===============END================'])

#Call all the functions 
final_message()
install_nodejs()
update_the_system()
does_nodejs_exists()

