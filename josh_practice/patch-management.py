#!/usr/bin/env python3 

# We are now going to use subprocess 

import subprocess 

# A block of code to upgrade and update the security patches 

def upgrade_system():
    subprocess.run(['apt', 'update'])
    subprocess.run(['apt', 'upgrade','-y'])

# A block of code to automatically remove old plugins 
def auto_remove():
    subprocess.run(['apt', 'autoremove', '-y'])

# A block of code to automatically clean the cache

def auto_clean():
    subprocess.run(['apt','autoclean','-y'])

# Let us now run the blocks of codes 
upgrade_system()
auto_remove()
auto_clean()

# Print a message on the screen 

print("Your system has been upgraded")
