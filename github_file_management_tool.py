from github import *

token = input("Enter in your GitHub access token: ")

a = Auth.Token(token)

git = Github(auth=a)

repo = input("Enter in your repository path (e.g. User/RepoName): ")

final_repo = git.get_repo(repo)

def create_file():

    try:

        file = input("Enter in the file name and extension that you want to create: ")

        message = input("Enter in commit message: ")

        content = input("Enter file cotents: ")

        branch = input("Enter the branch name you want to create this file in: ")

        final_repo.create_file(file, message, content, branch)
    
    except Exception as e:

        print(f"The following error occured: {e}")

def delete_file():

    try:


        file_to_delete = input("Enter in the file name and extension of the file you want to delete: ")

        message = input("Enter in commit message: ")

        branch = input("Enter the branch name you want to delete this file in: ")

        delete_info = final_repo.get_contents(file_to_delete, ref="test")

        final_repo.delete_file(delete_info.path, message, delete_info.sha, branch=branch)

    except Exception as e:

        print(f"The following error occured: {e}")

def update_file():

    try:

        file_to_update = input("Enter in the file name with extension that you want to update: ")

        c = final_repo.get_contents(file_to_update, ref="test")

        message = input("Enter in commit message: ")

        branch = input("Enter the branch name you want to update this file in: ")

        final_repo.update_file(c.path, message, "test", c.sha, branch=branch)

    except Exception as e:
            
            print(f"The following error occured: {e}")
