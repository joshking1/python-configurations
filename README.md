# python-configurations

# start.py 

In this script, students will be required to:

Understand the purpose and usage of the os module in Python.

Analyze the given code to identify its functionality and expected outcomes.

Explain the role of the create_folder() function and how it creates a new folder named "josh_practice".

Interpret the code that writes the content #!/usr/bin/env python3 to a file named "configuration.py" within the "josh_practice" folder.

Execute the code and verify that the folder and file are created as expected.

Modify the code to include additional files or perform more complex operations on the file system.

By engaging in running this script students will gain hands-on experience with file system manipulation, understanding code execution flow, and utilizing the os module in Python.


# docker.py

In this script, the following steps are performed:

1. The `check_docker_installed()` function checks if Docker is installed by running the `docker version` command. It prints a message indicating whether Docker is installed or not and returns `True` if installed, `False` otherwise.

2. The `install_docker()` function updates the package list and installs Docker using `apt` package manager.

3. The `start_docker_service()` function starts and enables the Docker service using `systemctl`.

4. The script checks if Docker is installed using the `check_docker_installed()` function. If it is not installed, it proceeds to install Docker by calling the `install_docker()` function and prints appropriate messages.

5. Finally, the script starts and enables the Docker service by calling the `start_docker_service()` function.

This script allows you to check for Docker installation, install Docker if needed, and start and enable the Docker service if it is already installed.


