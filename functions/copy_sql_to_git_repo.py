import os
import shutil

def copy_sql_to_git_repo(input_dict: dict, destination_path = r'\\RGHSOFSCTXAPP01\VA-NP-FolderRedir$\Cogito\IMT-A-MSCH0706\Downloads\DAP-SP-Caboodle\Deployments\DEV'):
    """
    Copies SQL files into corresponding subfolders within a Git repository.

    Args:
        input_dict (dict): Input details with keys:
            - "status" (str):      Status of the operation ("success" expected). If not "success", the function aborts.
            - "sql_files" (list):  List of file paths for SQL scripts to copy.
        destination_path (str):     Root path of the Git repository where files should be copied. 
                                    Each SQL file's folder is named after the file (without the extension).

    Returns:
        dict: A dictionary with the final status:
            - If "status" is not "success", returns {"status": "error", "error": "<error_message>"}.
            - Otherwise, performs the copy operation and prints the results.

    Author: Mathias Schindler (mathias.schindler.01@regionh.dk)
    Creation Date: 27-11-2024
    """
    
    sql_files = input_dict.get('sql_files', [])
    status = input_dict.get('status', 'undefined')

    if status != 'success': return {"status": "error", "error": "Operation status is not success; aborting."} 
    print('Beginning copying files from bulk script generation destination to Git repo location ...')

    for sql_file in sql_files:
        filename = os.path.basename(sql_file)
        source_path = os.path.dirname(sql_file)
        
        filename_no_extension = os.path.splitext(filename)[0]
        target_path = os.path.join(destination_path, filename_no_extension)
        
        # Check if the folder exists 
        if os.path.isdir(target_path):
            target_file_path = os.path.join(target_path, filename)

            # Check if file exists in the subfolder
            if os.path.isfile(target_file_path):
                try:
                    # Copy and replace the file
                    shutil.copy2(sql_file, target_file_path)
                    print(f"Replaced {filename} in {target_path}.")
                except Exception as e:
                    print(f"Failed to replace {filename} in {target_path}. Error: {e}")
            else:
                print(f"Folder found for {filename}, but the file was not found in {target_path}.")
        else:
            print(f"Subfolder for {filename} not found in {destination_path}.")



if __name__ == '__main__':
    from gitSwitchToCorrectBranch import git_switch_to_correct_branch
    from gitPullNewestFromRemote import git_pull_newest_from_remote

    git_switch_to_correct_branch(branch = 'SFSTRY0133294-testing', repo_path = r'\\RGHSOFSCTXAPP01\VA-NP-FolderRedir$\Cogito\IMT-A-MSCH0706\Downloads\DAP-SP-Caboodle\Deployments\DEV')
    git_pull_newest_from_remote(repo_path = r'\\RGHSOFSCTXAPP01\VA-NP-FolderRedir$\Cogito\IMT-A-MSCH0706\Downloads\DAP-SP-Caboodle\Deployments\DEV')

    copy_sql_to_git_repo(input_dict = {'sql_files': ['Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\ActivityDim.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AICllDMFactX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AICllSlicerDicerDataMartX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AIIschemiaAccessLogDataMartX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AIIschemiaDMFactX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AIIschemiaHistoricCAGsDMFactX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AIIschemiaLiveDMFactX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AIIschemiaLiveHistoricScoresDMFactX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AIIschemiaLiveInfoX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AIIschemiaLiveRawDataX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AIModelDimX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AIModelInfoX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AINoShowDataMartX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AINoShowGenericDMFactX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AIPerformanceIndicatorsDataMartX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AIPsyReadmissionDMFactX.sql',
                                                    'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest\\2024-11-27_13-52-24\\EpicScriptGen_20241127_135235_V107.821\\3_DmcsAndPackages\\AllExtractsDataMartX.sql'],
                                        'status': 'success'},
                        destination_path = r'\\RGHSOFSCTXAPP01\VA-NP-FolderRedir$\Cogito\IMT-A-MSCH0706\Downloads\DAP-SP-Caboodle\Deployments\DEV')
                        