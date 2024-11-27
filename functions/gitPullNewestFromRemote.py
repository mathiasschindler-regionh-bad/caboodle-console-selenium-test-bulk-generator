import os 
import subprocess

def git_pull_newest_from_remote(repo_path = r'\\RGHSOFSCTXAPP01\VA-NP-FolderRedir$\Cogito\IMT-A-MSCH0706\Downloads\DAP-SP-Caboodle\Deployments\DEV'):
    try:
        # Go to repo directory
        os.chdir(repo_path)

        # Pull newest changes from remote
        subprocess.run(['git', 'pull'], check = True)

    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    git_pull_newest_from_remote()