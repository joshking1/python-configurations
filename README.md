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

# git.py 


In this updated script, the following steps are performed:

1. The `is_git_installed()` function checks if Git is installed by running the command `command -v git &>/dev/null`. It prints a message indicating whether Git is installed or not.

2. The `installing_git()` function installs Git using the `apt` package manager by running the command `apt install git -y`.

3. The `message_on_screen()` function simply prints the message "=====END=====".

4. The script calls the `is_git_installed()` function to check if Git is installed. If it is not installed, it proceeds to install Git by calling the `installing_git()` function. The appropriate messages are printed during the process.

5. Finally, the script calls the `message_on_screen()` function to display the "=====END=====" message.

This script allows you to check for Git installation, install Git if needed, and display a concluding message at the end.

# Nodejs.py

This script checks whether Node.js is installed, installs it if needed, and displays a final message.


In this updated script, the following steps are performed:

1. The `does_nodejs_exist()` function checks if Node.js is installed by running the command `command -v node &>/dev/null`. It prints a message indicating whether Node.js is installed or not.

2. The `update_the_system()` function updates the system by running `apt update` and `apt upgrade -y` commands.

3. The `install_nodejs()` function installs Node.js using the `apt` package manager by running `apt install nodejs -y` command. It also displays the version of Node.js installed by running `node -v` command.

4. The `final_message()` function simply prints the message "===============END================".

5. The script calls the `final_message()` function to display the final message, then proceeds to install Node.js if it is not already installed by calling the `install_nodejs()` function. The system is updated first by calling the `update_the_system()` function. Appropriate messages are printed during the process.

This script allows you to check for Node.js installation, install Node.js if needed, update the system, and display a concluding message at the end.



