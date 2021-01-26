import requests
from github import Github
from pprint import pprint

token = '3c97d1fee60fccf63b9a374dea2db3ae881e21e8'

def SubTask1():
    g = Github(token)
    user = g.get_user()
    f.write("Environment: Python (simple scripting)\n")
    f.write("Igor\n")
    f.write("SubTask 1\n")
    f.write(user.login+"\n")
    f.write(user.name+"\n")
    f.write(str(user.id)+"\n")
    f.write(user.avatar_url+"\n")
    f.write(str(user.created_at)+"\n")
    f.write(str(user.followers)+"\n")

def createrepo():
    g = Github(token)
    user = g.get_user()
    full_name = input("Enter the name of your new repo: ")
    repocr = user.create_repo(full_name)
    return repocr.full_name


def delrepo():
    g = Github(token)
    user = g.get_user()
    full_name = input("Enter (your Github Username)/(name of your repo you want to delete): ")
    repo = g.get_repo(full_name)
    repo.delete()

def Subtask2(full_name):
    g = Github(token)
    user = g.get_user()
    #full_name = input("Enter (your Github Username)/(name of your repo you need): ")
    repo = g.get_repo(full_name)
    f.write("Subtask 2\n")
    f.write(str(repo.id)+"\n")
    f.write(repo.html_url+"\n")
    f.write(repo.full_name+"\n")
    f.write(repo.owner.login+"\n")
    f.write(repo.default_branch)


f = open('text.txt', 'w')
SubTask1()
Subtask2(createrepo())
delrepo()
f.close()