from functions.open_and_use_bulk_script_generator import open_and_use_bulk_script_generator
from functions.access_bulk_scripts_in_file_explorer import access_bulk_scripts_in_file_explorer
from functions.copy_sql_to_git_repo import copy_sql_to_git_repo
from functions.git_switch_to_correct_branch import git_switch_to_correct_branch
from functions.git_pull_newest_from_remote import git_pull_newest_from_remote
from functions.git_commit_new_sql_and_push import git_commit_new_sql_and_push

# Initialize key parameters
branch = 'bulk-script-update-from-PROD'
git_repo_path = r'\\RGHSOFSCTXAPP01\VA-NP-FolderRedir$\Cogito\IMT-A-MSCH0706\Downloads\DAP-SP-Caboodle\Deployments\DEV'
bulk_script_gen_export_destination_parent = r'\\spn4cdw001.sp.local\CustomPackages2\BulkScriptGeneratorOutputDestination' 
caboodle_console_url = 'https://sppcdwa.sp.local/Caboodle_PROD/'


# Run bulk script generator with default values
try:
    bulk_scripts = open_and_use_bulk_script_generator(output_directory=bulk_script_gen_export_destination_parent, 
                                                      console_url = caboodle_console_url,
                                                      # checkboxes_to_check = ['Sources'], # <-- only for testing runs
                                                      headless=False)
except Exception as e:
    print(f"Error in bulk script generator: {e}")
    raise  # Halts script execution

# Find current files
try:
    sql_files_from_bulk_script_gen = access_bulk_scripts_in_file_explorer(output=bulk_scripts)
except Exception as e:
    print(f"Error accessing bulk scripts: {e}")
    raise  

# Fetch newest changes to local Git repo in the correct branch
try:
    git_switch_to_correct_branch(branch=branch, repo_path=git_repo_path)
    git_pull_newest_from_remote(repo_path=git_repo_path)
except Exception as e:
    print(f"Error with Git operations: {e}")
    raise  

# Copy files from Bulk Script Generator export to Git repo
try:
    copy_sql_to_git_repo(input_dict=sql_files_from_bulk_script_gen, destination_path=git_repo_path)
except Exception as e:
    print(f"Error copying SQL files to Git repo: {e}")
    raise  

# Commit all changes and push to remote repo
try:
    git_commit_new_sql_and_push(branch=branch,
                                repo_path=git_repo_path,
                                commit_message='Automated update to sync scripts in Caboodle_DEV with Git')
except Exception as e:
    print(f"Error committing and pushing to Git repo: {e}")
    raise  
