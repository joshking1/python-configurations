#!/usr/bin/env python3 

# We are going to use os system 

import os 

def create_folder():
    folder_name = "josh_practice"
    os.mkdir(folder_name)

# Let us call the function

create_folder()
print("Folder create")

# Let add the following file to the josh_practice folder 
folder_name = "josh_practice"
file_name = "configuration.py"
create_file = os.path.join(folder_name,file_name)

file = open(create_file,"w") 
content = "\n #!/usr/bin/env python3"
file.write(content)
file.close()