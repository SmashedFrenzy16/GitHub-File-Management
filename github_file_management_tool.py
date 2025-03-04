from github import *

# This script allows you to create, delete, and update files in a GitHub repository using the GitHub API

token = input("Enter in your GitHub access token: ")

a = Auth.Token(token)

git = Github(auth=a)

repo = input("Enter in your repository path (e.g. User/RepoName): ")

final_repo = git.get_repo(repo)

def create_file():

    try:

        file = input("Enter in the file name and extension that you want to create: ")

        message = input("Enter in your commit message: ")

        content = input("Enter in the file contents: ")

        branch = input("Enter in the branch name you want to create this file in: ")

        final_repo.create_file(file, message, content, branch)

        print("File created successfully!")
    
    except Exception as e:

        print(f"The following error occured: {e}")

def delete_file():

    try:


        file_to_delete = input("Enter in the file name and extension of the file you want to delete: ")

        message = input("Enter in your commit message: ")

        branch = input("Enter in the branch name you want to delete this file in: ")

        delete_info = final_repo.get_contents(file_to_delete)

        final_repo.delete_file(delete_info.path, message, delete_info.sha, branch=branch)

        print("File deleted successfully!")

    except Exception as e:

        print(f"The following error occured: {e}")

def update_file():

    try:

        file_to_update = input("Enter in the file name with extension that you want to update: ")

        c = final_repo.get_contents(file_to_update)

        message = input("Enter in the commit message: ")

        branch = input("Enter in the branch name you want to update this file in: ")

        contents = input("Enter in the new contents of the file: ")

        final_repo.update_file(c.path, message, contents, c.sha, branch=branch)

        print("File updated successfully!")

    except Exception as e:
            
            print(f"The following error occured: {e}")

print("Here are the following actions that you can do: \n1. Create a file \n2. Delete a file \n3. Update a file \n4. Exit the program")

while True:


    choice = int(input("Enter in the number of the action you want to do: "))

    if choice == 1:

        create_file()

    elif choice == 2:
        
        delete_file()

    elif choice == 3:
        
        update_file()
    
    elif choice == 4:

        break
