import sys
from commands.create_repo import create_repository
from commands.create_branch import create_branch
from commands.push_file import push_file
from commands.pull_changes import pull_changes
from commands.fork_repo import fork_repository

def main():
    print("Welcome to GitPilot! Your personal GitHub assistant.")
    print("Type 'help' to see the list of commands, or 'exit' to quit.\n")

    while True:
        # Take user input
        user_input = input("> ").strip().lower()

        # Command options
        if user_input == "help":
            print("\nAvailable Commands:")
            print("1. create repository - Create a new GitHub repository")
            print("2. create branch - Create a new branch in a repository")
            print("3. push file - Push a file to a repository")
            print("4. pull changes - Pull changes from a branch")
            print("5. fork repository - Fork a repository")
            print("6. exit - Quit the program\n")

        elif user_input == "create repository":
            repo_name = input("Enter repository name: ").strip()
            description = input("Enter repository description: ").strip()
            create_repository(repo_name, description)

        elif user_input == "create branch":
            repo_name = input("Enter repository name: ").strip()
            new_branch = input("Enter new branch name: ").strip()
            base_branch = input("Enter base branch name: ").strip()
            create_branch(repo_name, new_branch, base_branch)

        elif user_input == "push file":
            repo_name = input("Enter repository name: ").strip()
            file_path = input("Enter file path: ").strip()
            commit_message = input("Enter commit message: ").strip()
            push_file(repo_name, file_path, commit_message)

        elif user_input == "pull changes":
            branch_name = input("Enter branch name: ").strip()
            pull_changes(branch_name)

        elif user_input == "fork repository":
            repo_owner = input("Enter repository owner's username: ").strip()
            repo_name = input("Enter repository name: ").strip()
            fork_repository(repo_owner, repo_name)

        elif user_input == "exit":
            print("Thank you for using GitPilot. Goodbye!")
            sys.exit()

        else:
            print("Invalid command. Type 'help' for the list of commands.")

if __name__ == "__main__":
    main()
