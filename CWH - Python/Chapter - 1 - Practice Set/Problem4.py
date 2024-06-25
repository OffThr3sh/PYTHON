# import os module

import os

# Path of a directory that we want 

dir = "D:\EDUCATION"

# Use os.listdir() to get the list of files and directories

contents = os.listdir(dir)

# Print the contents

for item in contents:
    print(item)