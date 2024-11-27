import os 
import subprocess

def git_commit_new_sql_and_push(repo_path = r'\\RGHSOFSCTXAPP01\VA-NP-FolderRedir$\Cogito\IMT-A-MSCH0706\Downloads\DAP-SP-Caboodle\Deployments\DEV', 
                            branch = 'main',
                            commit_message = 'Automated update to sync scripts in Caboodle_DEV with Git'):

    print('Beginning commiting new files and pushing to remote ...')
    try:
        # Go to repo directory
        os.chdir(repo_path)

        # Ensure correct branch
        subprocess.run(['git', 'checkout', branch], check = True)

        # Stage all changes
        subprocess.run(['git', 'add', '.'], check = True)

        # Add a commit message
        subprocess.run(['git', 'commit', '-m', commit_message], check = True)

        # Push changes to remote
        subprocess.run(['git', 'push', 'origin', branch], check = True)

        print("Changes successfully committed and pushed to remote.")

    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    git_commit_new_sql_and_push(branch = 'SFSTRY0133294-testing')