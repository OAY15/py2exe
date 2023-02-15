# build.py - The script that creates the .exe file

import os
import PyInstaller.__main__

# Set the path to your main process and UI programs
main_path = r"D:\bcm\bcm\play\exe\py2exe.py"
ui_path = r"D:\bcm\bcm\play\exe\ui_py2exe.py"

# Set the PyInstaller options
options = [
    '--onefile',  # Create a single executable file
      # Run the executable without a console window
]

# Change the working directory to the directory containing the scripts
os.chdir(os.path.dirname(main_path))

# Call the PyInstaller package to create the executable file
PyInstaller.__main__.run([main_path, ui_path] + options)
