# # Demyd Teslenko
from github import Github
from pprint import pprint
import requests

class Task:
    def __init__(self, username):
        self.__username = username
        self.__g = Github("66fba14fb37fe2f60ef940dfda8e305e1537c113")
        self.__url = f"https://api.github.com/users/{username}"
        self.__user = self.__g.get_user()

    def SubTask_1(self):
        def get_login(self):
            return f'User Login: {requests.get(self.__url).json()["login"]}'

        def get_id(self):
            return f'User ID: {requests.get(self.__url).json()["id"]}'

        def get_avatar_url(self):
            return f'User avatar URL: {requests.get(self.__url).json()["avatar_url"]}'

        def get_created_at(self):
            return f'User creation date: {requests.get(self.__url).json()["created_at"]}'

        def get_followers(self):
            return f'User followers: {requests.get(self.__url).json()["followers"]}'

        self.l = get_login(self), get_id(self), get_avatar_url(self), get_created_at(self), get_followers(self)
        return list(self.l)

    def SubTask_2(self):
        def create_repo(self, repo_name):
            self.__new_repo = self.__user.create_repo(f"{repo_name}")
            self.__repo = self.__g.get_repo(f"{self.__username}/{repo_name}")
            return self.__repo

        def get_id(self):
            self.__id = self.__repo.id
            return f'Repo id: {self.__id}'

        def get_html_url(self):
            self.__html_url = self.__repo.html_url
            return f'HTML URL of Repo: {self.__html_url}'

        def get_full_name(self):
            self.__full_name = self.__repo.full_name
            return f'Full name of Repo: {self.__full_name}'

        def get_owner_login(self):
            self.__owner_login = self.__repo.owner.login
            return f'Repo Owner\'s Login: {self.__owner_login}'

        def get_default_branch(self):
            self.__default_branch = self.__repo.default_branch
            return f'Repo Default Branch: {self.__default_branch}'

        def del_repo(self):
            self.__repo.delete()

        create_repo(self, "aaa")
        self.l = get_id(self), get_html_url(self), get_full_name(self), get_owner_login(self), get_default_branch(self)
        del_repo(self)
        return list(self.l)

t = Task("demidtes")
s1 = t.SubTask_1()
s2 = t.SubTask_2()
s3 = s1+s2

f = open("import_data.txt", "a")

count=0
for i in range(len(s3)):
    if count == 0:
        f.write("SubTask 1. Write a simple script that can get basic information about your GitHub profile" + '\n')
    elif count == len(s1):
        f.write('SubTask 2. Write a simple script that can create a new repository, get basic information about this repository and delete this repository' + '\n')
    f.write(s3[i] + '\n')
    count+=1

f.close()
