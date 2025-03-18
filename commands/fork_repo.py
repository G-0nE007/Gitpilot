from github import Github

def fork_repository(repo_owner, repo_name):
    try:
        g = Github("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")
        user = g.get_user()
        forked_repo = user.create_fork(f"{repo_owner}/{repo_name}")
        print(f"Repository '{repo_name}' forked successfully!")
    except Exception as e:
        print(f"Error: {e}")
