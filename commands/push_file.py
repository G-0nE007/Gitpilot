from github import Github
import base64

def push_file(repo_name, file_path, commit_message, branch="main"):
    try:
        g = Github("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")
        repo = g.get_user().get_repo(repo_name)

        with open(file_path, "rb") as file:
            content = file.read()

        file_name_in_repo = file_path.split("/")[-1]

        try:
            existing_file = repo.get_contents(file_name_in_repo, ref=branch)
            repo.update_file(existing_file.path, commit_message, content.decode("utf-8"), existing_file.sha, branch=branch)
            print(f"File '{file_name_in_repo}' updated successfully!")
        except:
            repo.create_file(file_name_in_repo, commit_message, content.decode("utf-8"), branch=branch)
            print(f"File '{file_name_in_repo}' created successfully!")
    except Exception as e:
        print(f"Error: {e}")
