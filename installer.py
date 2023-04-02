import subprocess
import sys
import os

def install_libraries(libraries):
    for library in libraries:
        subprocess.call([sys.executable, '-m', 'pip', 'install', library])

if __name__ == '__main__':
    # Verify Python version
    if sys.version_info < (3, 7) or sys.version_info > (3, 11):
        print("This script requires Python 3.7 to 3.10")
        sys.exit(1)

    # List of libraries to install
    libraries_to_install = ['rembg', 'pillow', 'tk', 'winshell']

    # Install libraries
    install_libraries(libraries_to_install)

    subprocess.call([sys.executable, 'quickedit.py'])

    import winshell
    from win32com.client import Dispatch

    
    script_path = os.path.abspath(__file__)
    directory = os.path.dirname(script_path)
    filename = "quickedit.py"
    icon_filename = "quickedit.ico"  
    
    # Set path to target file
    target_file_path = os.path.join(directory, filename)

    # Set path to shortcut file
    shortcut_file_path = os.path.join(winshell.desktop(), "Quickedit.lnk")

    # Create a shortcut object
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_file_path)

    # Set properties for the shortcut
    shortcut.Targetpath = target_file_path
    shortcut.WorkingDirectory = os.path.dirname(target_file_path)
    shortcut.IconLocation = os.path.join(directory, icon_filename)
    shortcut.Description = "Quickedit"

    # Save the shortcut
    shortcut.save()
