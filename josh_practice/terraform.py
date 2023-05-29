#!/usr/bin/env python3 

# Let us use the subprocess and the shutil 

import subprocess
import shutil
import os

# Let check whether git is installed 

# We are going to combine both subprocess and os.system 

#We going to check git binary

def check_whether_git_installed():
    # Return is a just a key name in python that is used to return value in a function
    # In this case, we are going to use return to rteunr some values from check_whether_git_installed()
    # It is much easier to give 
    is_terraform_installed = (os.system(" command -v terraform &>/dev/null")) ==0
    
    if is_terraform_installed:
        print("Terraform is installed")
    else:
        print("Terraform is not installed and need to be installed")
# The if statement is evaluating the value of the variable is_git_installed. 
# If the value of is_terraform_installed is True, indicating that git is installed, the code block inside the if statement will be executed. In this case, it will print the message "terraform is installed."
# If the value of is_terraform_installed is False, meaning Docker is not installed, the code block inside the if statement will be skipped, and no message will be printed.
# The purpose of this if statement is to provide feedback or confirmation to the user that terraform is installed, based on the result of the check performed in the is_terraform_installed() function.

#(Now we are going to get to the subprocess)

def terraform_install_ubuntu():
    os.system("wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg")
    os.system('echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list')
    os.system('sudo apt update -y && sudo apt install terraform -y')

def update_system():
    os.system('apt-get update && apt-get upgrade -y')
    os.system('nproc && lsblk ') 

def final_message():
    print('You should be happy because terraform has been installed and system updated')

# Let us run the functions to perfom the tasks 
terraform_install_ubuntu()
update_system()
final_message()
