import subprocess
import os
from datetime import datetime, timedelta

class FolderManager:
    _instance = None

    def __new__(self):
        # Singleton Pattern
        if not self._instance:
            self._instance = super(FolderManager, self).__new__(self)
        return self._instance
    
    def create_and_open_folder(self, folder_name):
        # Create new folder for generated git repo
        create_folder_command = f"mkdir {folder_name}"
        process = subprocess.Popen(create_folder_command,
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        _, error = process.communicate()

        if process.returncode == 0:
            os.chdir(folder_name)
        else:
            raise RuntimeError(f"Error creating folder: {error}")
