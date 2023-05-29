#!/usr/bin/env python3

# Let us start with the os.system 

import os 

# A block of code to upgrade and update the security patches 

def upgrade_system():
    os.system("apt-get update")
    os.system("apt-get upgrade -y")

# A block of code to automatically remove old plugins 
def auto_remove():
    os.system("apt-get autoremove -y")

# A block of code to automatically clean the cache

def auto_clean():
    os.system("apt-get autoclean -y")

# Let us now run the blocks of codes 
upgrade_system()
auto_remove()
auto_clean()

# Print a message on the screen 

print("Your system has been upgraded")
