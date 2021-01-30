import github
from pprint import pprint
import requests
import sys

class ChatBot:
    def __init__(self, token, username):
        self.__username = username
        self.__g = github.Github(token)
        self.__user = self.__g.get_user()

    def create_repo(self):
        try:
            self.repo_name = input("Enter repo name to create: ")
            self.__new_repo = self.__user.create_repo(f"{self.repo_name}")
            print("Repo created!")
        except github.GithubException:
            print("Something went wrong, please try again.")

    def delete_repo(self):
        try:
            while True:
                name_or_id = input("Do you want to delete repo by:\n 1- Name,\n 2- ID,\n 3- Back to previous point\n-> ")
                if name_or_id == '1':
                    self.repo_name = self.__username+"/"+input("Enter repo name to delete: ")
                    break
                elif name_or_id == '2':
                    self.repo_name = int(input("Enter repo id to delete: "))
                    break
                elif name_or_id == '3':
                    break
                else:
                    print("Wrong answer. Try again.")
            # self.__repo = self.__g.get_repo(f"{self.__username}/{repo_name}")
            self.__repo = self.__g.get_repo(self.repo_name)
            self.__repo.delete()
            print("Repo deleted!")
        except github.GithubException:
            print("Something went wrong, please try again.")

    def get_repo_info(self):
        try:
            while True:
                name_or_id = input("Do you want to find a repo by:\n 1- Name,\n 2- ID,\n 3- Back to previous point\n-> ")
                if name_or_id == '1':
                    self.repo_name = self.__username+"/"+input("Enter repo name to show info: ")
                    break
                elif name_or_id == '2':
                    self.repo_name = int(input("Enter repo id to show info: "))
                    break
                elif name_or_id == '3':
                    break
                else:
                    print("Wrong answer. Try again.")
            # self.__repo = self.__g.get_repo(f"{self.__username}/{repo_name}")
            self.__repo = self.__g.get_repo(self.repo_name)
            self.__id = self.__repo.id
            self.__description = self.__repo.description
            self.__html_url = self.__repo.html_url
            self.__full_name = self.__repo.full_name
            self.__owner_login = self.__repo.owner.login
            self.__default_branch = self.__repo.default_branch
            self.l = self.__id, self.__description, self.__html_url, self.__full_name, self.__owner_login, self.__default_branch
            pprint(self.l)
        except github.GithubException:
            print("Something went wrong, please try again.")

    def add_collaborator(self):
        try:
            self.repo_name = input("Enter repo name to add collaborator in: ")
            self.coll_name = input("Enter collaborator name you want to add: ")
            self.__repo = self.__g.get_repo(f"{self.__username}/{self.repo_name}")
            self.__repo.add_to_collaborators(self.coll_name)
            print("Collaborator added!")
        except github.GithubException:
            print("Something went wrong, please try again.")

    def remove_collaborator(self):
        try:
            self.repo_name = input("Enter repo name to remove collaborator from: ")
            self.coll_name = input("Enter collaborator name you want to remove: ")
            self.__repo = self.__g.get_repo(f"{self.__username}/{self.repo_name}")
            self.__repo.remove_from_collaborators(self.coll_name)
            print("Collaborator removed!")
        except github.GithubException:
            print("Something went wrong, please try again.")

    def create_branch(self):
        try:
            self.repo_name = input("Enter repo name to create branch on: ")
            self.main_branch_name = input("Enter your main branch name: ")
            self.new_branch_name = input("Enter branch name you want to create: ")
            self.__repo = self.__g.get_repo(f"{self.__username}/{self.repo_name}")
            self.branch = self.__repo.get_branch(self.main_branch_name)
            self.__repo.create_git_ref(ref='refs/heads/' + self.new_branch_name, sha=self.branch.commit.sha)
            print("Branch created!")
        except github.GithubException:
            print("Something went wrong, please try again.")

    def delete_branch(self):
        try:
            self.repo_name = input("Enter repo name to delete branch from: ")
            self.delete_branch_name = input("Enter branch name you want to delete: ")
            self.__repo = self.__g.get_repo(f"{self.__username}/{self.repo_name}")
            self.branch = self.__repo.get_git_ref("heads/%s" % self.delete_branch_name)
            self.branch.delete()
            print("Branch deleted!")
        except github.GithubException:
            print("Something went wrong, please try again.")

    def end_work(self):
        return

    def do_nothing(self):
        print("There is no such option!")

    def stop_bot(self):
        return sys.exit("ChatBot [OFF]")

    def func_constructor(self, option):
        l_1 = ["Choose option:\n 1- Create repo,\n 2- Delete repo,\n 3- Back to main menu:\n-> ", self.create_repo, self.delete_repo, self.end_work]
        l_2 = ["Choose option:\n 1- Show info,\n 2- Back to main menu:\n-> ", self.get_repo_info, self.end_work, self.do_nothing]
        l_3 = ["Choose option:\n 1- Add collaborator,\n 2- Remove collaborator,\n 3- Back to main menu:\n-> ", self.add_collaborator, self.remove_collaborator, self.end_work]
        l_4 = ["Choose option:\n 1- Create branch,\n 2- Delete branch,\n 3- Back to main menu:\n-> ", self.create_branch, self.delete_branch, self.end_work]
        l_0 = [self.stop_bot]
        if option == '1':
            return l_1
        elif option == '2':
            return l_2
        elif option == '3':
            return l_3
        elif option == '4':
            return l_4
        elif option == '0':
            return l_0

    def start_option(self, option):
        if int(option) < 5:
            if type(self.func_constructor(option)[0]) == str:
                sub_option = input(self.func_constructor(option)[0])
                if sub_option == '1':
                    self.func_constructor(option)[1]()
                elif sub_option == '2':
                    self.func_constructor(option)[2]()
                elif sub_option == '3':
                    self.func_constructor(option)[3]()
                else:
                    self.do_nothing()
            elif type(self.func_constructor(option)[0]) != str:
                self.func_constructor(option)[0]()
        else:
            print("There is no such option")

    def start_bot(self):
        while True:
            option = input("Choose option:\n 1- Create/Delete Repo,\n 2- Find repo and get info,\n 3- Add/Remove Collaborator,\n 4- Create/Delete Branch,\n 0- Quit:\n-> ")
            self.start_option(option)

if __name__ == "__main__":
    print("ChatBot [ON]")
    get_token = input("Enter personal token: ")
    get_username = input("Enter username: ")
    cb = ChatBot(get_token, get_username)
    cb.start_bot()
