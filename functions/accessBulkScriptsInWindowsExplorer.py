import os
import fnmatch

# Definitions to become function parameters
path = r"Z:\Caboodle_DEV\BulkScriptGenerationDeploymentScriptsTest"
folder_name = '2024-10-17_15-08-32'

# Change to parent directory
try:
    os.chdir(path)
    print(f"Successfully changed to: {os.getcwd()}")
except FileNotFoundError:
    print("The specified path does not exist.")
except OSError as e:
    print(f"Error: {e}")

# Change to folder with execution timestamp
try:
    os.chdir(folder_name)
    print(f"Successfully changed to: {os.getcwd()}")
except FileNotFoundError:
    print("The specified path does not exist.")
except OSError as e:
    print(f"Error: {e}")

# Find the folder that contains "EpicScriptGen" in its name
try:
    current_directory = os.getcwd()
    matching_folders = [d for d in os.listdir(current_directory) if fnmatch.fnmatch(d, "*EpicScriptGen*") and os.path.isdir(d)]
except FileNotFoundError:
    print("No path exists containing substring EpicScriptGen.")
except OSError as e:
    print(f"Error: {e}")

# Access the folder with "EpicScriptGen"
try:
    os.chdir(matching_folders[0])
    print(f"Successfully changed to: {os.getcwd()}")
except FileNotFoundError:
    print("The specified path does not exist.")
except OSError as e:
    print(f"Error: {e}")


# Change to folder with deployment scripts
try:
    os.chdir('3_DmcsAndPackages')
    print(f"Successfully changed to: {os.getcwd()}")
    print(f"Contents in folder: {os.listdir(os.getcwd())}")
except FileNotFoundError:
    print("The specified path does not exist.")
except OSError as e:
    print(f"Error: {e}")