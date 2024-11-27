import os 
import subprocess

def git_switch_to_correct_branch(repo_path = r'\\RGHSOFSCTXAPP01\VA-NP-FolderRedir$\Cogito\IMT-A-MSCH0706\Downloads\DAP-SP-Caboodle\Deployments\DEV', 
                                 branch = 'main'):
    try:
        # Go to repo directory
        os.chdir(repo_path)

        # Ensure correct branch
        subprocess.run(['git', 'checkout', branch], check = True)

    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    git_switch_to_correct_branch(branch = 'SFSTRY0133294-testing')