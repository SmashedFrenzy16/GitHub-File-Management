from github import *

token = input("Enter in your GitHub access token: ")

a = Auth.Token(token)

git = Github(auth=a)

repo = input("Enter in your repository path (e.g. User/RepoName): ")

final_repo = git.get_repo(repo)

def create_file():

    file = input("Enter in the file name and extension that you want to create: ")

    message = input("Enter in commit message: ")

    content = input("Enter file cotents: ")

    branch = input("Enter the branch name you want to create this file in: ")

    final_repo.create_file(file, message, content, branch)
