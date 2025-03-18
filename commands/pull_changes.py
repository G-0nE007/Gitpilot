import subprocess

def pull_changes(branch_name):
    try:
        subprocess.run(["git", "pull", "origin", branch_name], check=True)
        print(f"Changes pulled successfully for branch '{branch_name}'!")
    except subprocess.CalledProcessError as e:
        print(f"Error pulling changes: {e}")
