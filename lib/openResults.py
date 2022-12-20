import os
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%m_%d_%Y")

def getDirectory():
    directory = "Output_" + dt_string
    return directory

directory = getDirectory()

# a script that gets goes through all files and subdirectories and opens them

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.startswith("Page"):
            # print(file)
            # print(os.path.join(root, file))
            os.startfile(os.path.join(root, file))

