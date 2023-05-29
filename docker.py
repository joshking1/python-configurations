#!/usr/bin/env python3 

# I want to check whether docker is installed and if not, install it

# I will start with the os.system 

import os 

# Check if Docker is installed by running the docker version command

def check_docker_installed():
    # Check if Docker is installed by running the docker version command
    docker_installed = os.system('docker version &>/dev/null') == 0
    
    if docker_installed:
        print("Docker is installed.")
    else:
        print("Docker is not installed.")
    
    print(docker_installed)

def install_docker():
    # Update the package list and install Docker using apt
    os.system('sudo apt update')
    os.system('sudo apt install -y docker.io')

def start_docker_service():
    # Start and enable the Docker service using systemctl
    os.system('sudo systemctl start docker')
    os.system('sudo systemctl enable docker')

# Check if Docker is installed
if not check_docker_installed():
    print("Docker is not installed. Installing Docker...")
    install_docker()
    print("Docker has been installed.")
else:
    print("Docker is already installed.")

# Start and enable the Docker service
print("Starting and enabling the Docker service...")
start_docker_service()
print("Docker service has been started and enabled.")


    
  