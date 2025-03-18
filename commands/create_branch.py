from github import Github

def create_branch(repo_name, new_branch, base_branch):
    try:
        g = Github("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")
        repo = g.get_user().get_repo(repo_name)

        base_branch_ref = repo.get_git_ref(f"heads/{base_branch}")
        base_branch_sha = base_branch_ref.object.sha
        
        repo.create_git_ref(ref=f"refs/heads/{new_branch}", sha=base_branch_sha)
        print(f"Branch '{new_branch}' created successfully from '{base_branch}'!")
    except Exception as e:
        print(f"Error: {e}")
