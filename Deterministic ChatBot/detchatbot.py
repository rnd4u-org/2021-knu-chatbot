from github import Github
import sys

class chatbotgh:
    def __init__(self, username):
        print("Welcome,"+username+", to Deterministic ChatBot for Github. ")
        token = input("Enter your (access!!!!!!) token: ")
        print("Enter 'Help' to see the list of commands.\n")
        self.username = username
        self.g = Github(token)
        self.user = self.g.get_user()

    def get_info(self, full_name_or_id):
        repo = self.g.get_repo(full_name_or_id)
        id = repo.id
        description = repo.description
        created_at = repo.created_at
        html_url = repo.html_url
        owner_name = repo.owner.name
        owner_login = repo.owner.login
        full_name = repo.full_name
        watch_count = repo.watchers_count
        default_branch = repo.default_branch
        list_info = id, description, str(created_at), html_url, owner_name, owner_login, full_name, watch_count, default_branch,
        return list(list_info)

    def create_repo(self, name):
        self.user.create_repo(name)

    def del_repo(self, full_name):
        repo = self.g.get_repo(full_name)
        repo.delete()

    def add_collaborator(self, full_name, collab_name):
        repo = self.g.get_repo(full_name)
        repo.add_to_collaborators(collab_name)

    def cr_branch(self, full_name, source_branch_name, new_branch_name):
        repo = self.g.get_repo(full_name)
        sb = repo.get_branch(source_branch_name)
        repo.create_git_ref('refs/heads/' + new_branch_name, sb.commit.sha)

    def del_collaborator(self, full_name, collab_name):
        repo = self.g.get_repo(full_name)
        repo.remove_from_collaborators(collab_name)

    def del_branch(self, full_name, del_branch_name):
        repo = self.g.get_repo(full_name)
        branch_to_delete = repo.get_git_ref("heads/%s" % del_branch_name)
        branch_to_delete.delete()

    def end(self):
        sys.exit("Ending...")

    def help(self):
        print('Command list:','Get_info', 'Create_repo', 'Delete_repo',  'Add_collaborator', 'Create_branch',
              'Delete_collaborator', 'Delete_branch', 'Help', 'End', sep='\n')

def work():
    commandlist = ['Create_repo', 'Delete_repo', 'Get_info', 'Add_collaborator', 'Create_branch','Delete_collaborator', 'Delete_branch', 'Help', 'End',]
    username = input("Enter your Github username: ")
    cb = chatbotgh(username)
    interrogation = "Yes"
    while interrogation == "Yes":
        command = input("Enter your command: ")
        try:
            while command not in commandlist:
                print("This command does not exist. Try again.")
                command = input("Enter your command: ")
        except:
            pass

        if command == 'Help':
            cb.help()
        elif command == 'Create_repo':
            try:
                name = input("Enter the name of your new repository: ")
                cb.create_repo(name)
            except Exception as exc:
                print("Info about exception: ", exc)
        elif command == 'Delete_repo':
            try:
                choice = input("You want to find repo by 'Name' or 'Id'? ")
                if choice == 'Name':
                    name = username+"/"+input("Enter the name of repository you want to delete: ")
                    cb.del_repo(name)
                elif choice == 'Id':
                    del_id = int(input("Enter needed id: "))
                    cb.del_repo(del_id)
                else:
                    print("Please enter 'Name' or 'Id'.")
            except Exception as exc:
                print("Info about exception: ", exc)
        elif command == 'Get_info':
            try:
                print("You will get basic info about repo yo seek: ID, HTML_URL, "
                      "full name, owner's login, default branch, creation time, description, owner's name "
                      "and watchers count.")
                choice = input("You want to find repo by 'Name' or 'Id'? ")
                if choice == 'Name':
                    name = username + '/' + input("Enter the name of repository you seek: ")
                    o = cb.get_info(name)
                    for i in o:
                        print(i)
                elif choice == 'Id':
                    id = int(input("Enter needed id: "))
                    o = cb.get_info(id)
                    for i in o:
                        print(i)
                else:
                    print("Enter 'Name' or 'Id'.")
            except Exception as exc:
                print("Info about exception: ", exc)
        elif command == 'Add_collaborator':
            try:
                rep_name = input("Enter the name of repository where you want to add a collaborator: ")
                col_name = input("Enter the name of collaborator you want to add: ")
                cb.add_collaborator(rep_name, col_name)
            except Exception as exc:
                print("Info about exception: ", exc)
        elif command == 'Delete_collaborator':
            try:
                rep_name = input("Enter the name of repository where you want to remove a collaborator: ")
                col_name = input("Enter the name of collaborator you want to remove: ")
                cb.del_collaborator(rep_name, col_name)
            except Exception as exc:
                print("Info about exception: ", exc)
        elif command == 'Create_branch':
            try:
                rep_name = username+'/'+input("Enter the name of repository what you need: ")
                s_branch = input("Enter the name of your source branch: ")
                n_branch = input("Enter the name of your new branch: ")
                cb.cr_branch(rep_name, s_branch, n_branch)
            except Exception as exc:
                print("Info about exception: ", exc)
        elif command == 'Delete_branch':
            try:
                rep_name = username+'/'+input("Enter the name of repository what you need: ")
                d_branch = input("Enter the name of your branch what you want to delete: ")
                cb.del_branch(rep_name, d_branch)
            except Exception as exc:
                print("Info about exception: ", exc)
        elif command == 'End':
            cb.end()


        interrogation = input("Do you need something? Type 'Yes' to continue. ")
        if interrogation != "Yes":
            print("Chat Over...")
work()





