import os
import fnmatch
from pprint import pprint

def access_bulk_scripts_in_file_explorer(output: dict, 
                                         bulk_scripts_dir = 'DmcsAndPackages'):
    """
    Navigates through directories based on input details and lists the contents of a specific folder.

    Args:
        output (dict): Input details with keys:
            - "status" (str):       Status of the previous operation ("success" expected).
            - "output_dir" (str):   Base output directory to navigate from.
        bulk_scripts_dir (str):     Substring of a directory name to search for. Substring because Caboodle Console prefixes folders with a number which can change dynamically, e.g. "2_DmcsAndPackages".

    Returns:
        dict: A dictionary with the final status and directory contents or error details.
    """

    try:
        if output["status"] != "success": return {"status": "error", "error": "Invalid input status. Expected 'success'."}

        # Extract the output directory
        base_path = output["output_dir"]

        # Navigate to base path
        os.chdir(base_path)
        print(f"Successfully changed to: {os.getcwd()}")

        # Find the folder that contains "EpicScriptGen" in its name
        matching_folders = [d for d in os.listdir(base_path) if fnmatch.fnmatch(d, "*EpicScriptGen*") and os.path.isdir(d)]
        if not matching_folders: return {"status": "error", "error": "No folder found containing 'EpicScriptGen'."}
        # TBA: Error handling for if multiple matching folders containing 'EpicScriptGen' are found!

        # Change to the matching folder
        epic_folder_path = os.path.join(base_path, matching_folders[0])
        os.chdir(epic_folder_path)
        print(f"Successfully changed to EpicScriptGen folder: {os.getcwd()}")

        # Search for folders that contain the bulk_scripts_dir string as a substring (no need to match the exact prefix)
        matching_bulk_scripts_folders = [d for d in os.listdir(epic_folder_path) if bulk_scripts_dir in d and os.path.isdir(os.path.join(epic_folder_path, d))]
        if not matching_bulk_scripts_folders: 
            return {"status": "error", "error": f"Folder containing '{bulk_scripts_dir}' not found."}
        else:
            bulk_scripts_path = os.path.join(epic_folder_path, matching_bulk_scripts_folders[0])
            os.chdir(bulk_scripts_path)
            print(f"Successfully changed to folder containing '{bulk_scripts_dir}': {os.getcwd()}")

            # Get list of all files ending in .sql in the bulk_scripts_path folder
            sql_files = []
            for root, dirs, files in os.walk(bulk_scripts_path):
                for file in files:
                    if file.endswith(".sql"):
                        sql_files.append(os.path.join(root, file))
            
            # Return the list of .sql files with full path
            return {"status": "success", "sql_files": sql_files} 
    
    except FileNotFoundError as e:
        return {"status": "error", "error": f"File not found: {str(e)}"}
    except OSError as e:
        return {"status": "error", "error": f"OS error: {str(e)}"}
    except Exception as e:
        return {"status": "error", "error": f"Unexpected error: {str(e)}"}


if __name__ == '__main__':
    result = access_bulk_scripts_in_file_explorer(output = {"status": "success",
                                                            "output_dir": r"Z:\Cab_Ironman\BulkScriptGenerationDeploymentScriptsTest\2024-11-26_15-48-47"},
                                                bulk_scripts_dir = 'Sources')
    pprint(result)