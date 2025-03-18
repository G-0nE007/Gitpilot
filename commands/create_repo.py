from github import Github

def create_repository(repo_name, description):
    try:
        g = Github("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")
        user = g.get_user()
        repo = user.create_repo(repo_name, description=description)
        print(f"Repository '{repo_name}' created successfully!")
    except Exception as e:
        print(f"Error: {e}")
