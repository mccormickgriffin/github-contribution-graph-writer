import subprocess
import os

# Get user input for what word they want to write on what years contribution graph
year = input("What year would you like to write on? ")
word = input("What would you like to write? ")

# Create new folder for generated git repo
folder_name = f"{year}-{word}"
create_folder_command = f"mkdir {folder_name}"
process = subprocess.Popen(create_folder_command,
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           text=True)
output, error = process.communicate()

if process.returncode == 0:
    os.chdir(folder_name)
    subprocess.run(["git", "init"])
else:
    print(f"Error creating folder: {error}")
 