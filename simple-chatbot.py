import github
from pprint import pprint
import requests
import sys

class ChatBot:
    def __init__(self, token, username):
        self.__username = username
        self.__g = github.Github(token)
        self.__user = self.__g.get_user()

    def create_repo(self, repo_name):
        try:
            self.__new_repo = self.__user.create_repo(f"{repo_name}")
            print("Repo created!")
        except github.GithubException:
            print("Something went wrong, please try again.")

    def delete_repo(self, repo_name):
        try:
            # self.__repo = self.__g.get_repo(f"{self.__username}/{repo_name}")
            self.__repo = self.__g.get_repo(repo_name)
            self.__repo.delete()
            print("Repo deleted!")
        except github.GithubException:
            print("Something went wrong, please try again.")

    def get_repo_info(self, repo_name):
        try:
            # self.__repo = self.__g.get_repo(f"{self.__username}/{repo_name}")
            self.__repo = self.__g.get_repo(repo_name)
            self.__id = self.__repo.id
            self.__description = self.__repo.description
            self.__html_url = self.__repo.html_url
            self.__full_name = self.__repo.full_name
            self.__owner_login = self.__repo.owner.login
            self.__default_branch = self.__repo.default_branch
            self.l = self.__id, self.__description, self.__html_url, self.__full_name, self.__owner_login, self.__default_branch
            return self.l
        except github.GithubException:
            print("Something went wrong, please try again.")

    def add_collaborator(self, repo_name, collaborator_name):
        try:
            self.__repo = self.__g.get_repo(f"{self.__username}/{repo_name}")
            self.__repo.add_to_collaborators(collaborator_name)
            print("Collaborator added!")
        except github.GithubException:
            print("Something went wrong, please try again.")

    def remove_collaborator(self, repo_name, collaborator_name):
        try:
            self.__repo = self.__g.get_repo(f"{self.__username}/{repo_name}")
            self.__repo.remove_from_collaborators(collaborator_name)
            print("Collaborator removed!")
        except github.GithubException:
            print("Something went wrong, please try again.")

    def create_branch(self, repo_name, main_branch_name, new_branch_name):
        try:
            self.__repo = self.__g.get_repo(f"{self.__username}/{repo_name}")
            self.branch = self.__repo.get_branch(main_branch_name)
            self.__repo.create_git_ref(ref='refs/heads/' + new_branch_name, sha=self.branch.commit.sha)
            print("Branch created!")
        except github.GithubException:
            print("Something went wrong, please try again.")

    def delete_branch(self, repo_name, delete_branch_name):
        try:
            self.__repo = self.__g.get_repo(f"{self.__username}/{repo_name}")
            self.branch = self.__repo.get_git_ref("heads/%s" % delete_branch_name)
            self.branch.delete()
            print("Branch deleted!")
        except github.GithubException:
            print("Something went wrong, please try again.")

    def end_work(self):
        return sys.exit("ChatBot [OFF]")

    def func_option_1(self):
        while True:
            option_1 = input("Choose option:\n 1- Create repo,\n 2- Delete repo,\n 3- Back to main menu:\n-> ")
            if option_1 == '1':
                self.create_repo(input("Enter repo name to create: "))
            elif option_1 == '2':
                while True:
                    name_or_id = input("Do you want to delete repo by:\n 1- Name,\n 2- ID,\n 3- Back to previous point\n-> ")
                    if name_or_id == '1':
                        self.delete_repo(self.__username+"/"+input("Enter repo name to delete: "))
                        break
                    elif name_or_id == '2':
                        self.delete_repo(int(input("Enter repo id to delete: ")))
                        break
                    elif name_or_id == '3':
                        break
                    else:
                        print("Wrong answer. Try again.")
            elif option_1 == '3':
                break
            else:
                print("There is no such option!")

    def func_option_2(self):
        while True:
            name_or_id = input("Do you want to find a repo by:\n 1- Name,\n 2- ID,\n 3- Back to previous point\n-> ")
            if name_or_id == '1':
                pprint(self.get_repo_info(self.__username+"/"+input("Enter repo name to show info: ")))
                # pprint(self.get_repo_info(self.repo_name))
                break
            elif name_or_id == '2':
                pprint(self.get_repo_info(int(input("Enter repo id to show info: "))))
                break
            elif name_or_id == '3':
                break
            else:
                print("Wrong answer. Try again.")


    def func_option_3(self):
        while True:
            option_3 = input("Choose option:\n 1- Add Collaborator,\n 2- Remove Collaborator,\n 3- Back to main menu:\n-> ")
            if option_3 == '1':
                self.repo_name = input("Enter repo name to add collaborator in: ")
                self.coll_name = input("Enter collaborator name you want to add: ")
                self.add_collaborator(self.repo_name, self.coll_name)
            elif option_3 == '2':
                self.repo_name = input("Enter repo name to remove collaborator from: ")
                self.coll_name = input("Enter collaborator name you want to remove: ")
                self.remove_collaborator(self.repo_name, self.coll_name)
            elif option_3 == '3':
                break
            else:
                print("There is no such option!")

    def func_option_4(self):
        while True:
            option_4 = input("Choose option:\n 1- Create Branch,\n 2- Delete Branch,\n 3- Back to main menu:\n-> ")
            if option_4 == '1':
                self.repo_name = input("Enter repo name to create branch on: ")
                self.main_branch_name = input("Enter your main branch name: ")
                self.branch_name = input("Enter branch name you want to create: ")
                self.create_branch(self.repo_name, self.main_branch_name, self.branch_name)
            elif option_4 == '2':
                self.repo_name = input("Enter repo name to delete branch from: ")
                self.branch_name = input("Enter branch name you want to delete: ")
                self.delete_branch(self.repo_name, self.branch_name)
            elif option_4 == '3':
                break
            else:
                print("There is no such option!")

    def choose_option(self, option):
        if option == '1':
            self.func_option_1()
        elif option == '2':
            self.func_option_2()
        elif option == '3':
            self.func_option_3()
        elif option == '4':
            self.func_option_4()
        elif option == '0':
            self.end_work()
        else:
            print("There is no such option!")
            return

    def start_bot(self):
        while True:
            option = input("Choose option:\n 1- Create/Delete Repo,\n 2- Find repo and get info,\n 3- Add/Remove Collaborator,\n 4- Create/Delete Branch,\n 0- Quit:\n-> ")
            self.choose_option(option)

if __name__ == "__main__":
    print("ChatBot [ON]")
    get_token = input("Enter personal token: ")
    get_username = input("Enter username: ")
    cb = ChatBot(get_token, get_username)
    cb.start_bot()
