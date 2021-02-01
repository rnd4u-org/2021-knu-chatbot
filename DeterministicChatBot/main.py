from github import Github
import sys

class ChatBotGH:
    def __init__(self, username):
        print("Welcome,"+username+", to DetChatBot for Github. ")
        token = input("Enter your access token(please be sure to give it all necesarry permissions): ")
        print("Enter 'Help' to see the list of commands.\n")
        self.username = username
        self.g = Github(token)
        self.user = self.g.get_user()

    def create_repo(self, name):
        self.user.create_repo(name)

    def del_repo(self, full_name):
        repo = self.g.get_repo(full_name)
        repo.delete()

    def get_info(self, full_name_or_id):
        repo = self.g.get_repo(full_name_or_id)
        id = repo.id
        created_at = repo.created_at
        description = repo.description
        owner_name = repo.owner.name
        html_url = repo.html_url
        full_name = repo.full_name
        owner_login = repo.owner.login
        default_branch = repo.default_branch
        watch_count = repo.watchers_count
        list_info = id, html_url, full_name, owner_login, default_branch, str(created_at), description, owner_name, watch_count
        return list(list_info)

    def add_collaborator(self, full_name, collab_name):
        repo = self.g.get_repo(full_name)
        repo.add_to_collaborators(collab_name)

    def del_collaborator(self, full_name, collab_name):
        repo = self.g.get_repo(full_name)
        repo.remove_from_collaborators(collab_name)

    def cr_branch(self, full_name, source_branch_name, new_branch_name):
        repo = self.g.get_repo(full_name)
        sb = repo.get_branch(source_branch_name)
        repo.create_git_ref('refs/heads/' + new_branch_name, sb.commit.sha)

    def del_branch(self, full_name, del_branch_name):
        repo = self.g.get_repo(full_name)
        branch_to_delete = repo.get_git_ref("heads/%s" % del_branch_name)
        branch_to_delete.delete()

    def help(self):
        print('Command list:','Help','Create_repo','Delete_repo','Get_info','Add_collaborator',
              'Delete_collaborator','Create_branch','Delete_branch','Quit', sep='\n')

    def quit(self):
        sys.exit("Ending...")

def work():
    commandlist = ['Help','Create_repo','Delete_repo','Get_info','Add_collaborator','Delete_collaborator','Create_branch','Delete_branch','Quit']
    username = input("Enter your Github username: ")
    CB = ChatBotGH(username)
    query = "Yes"
    while query == "Yes":
        command = input("Enter your command: ")
        try:
            while command not in commandlist:
                print("This command does not exist. Try again.")
                command = input("Enter your command: ")
        except:
            pass

        if command == 'Help':
            CB.help()
        elif command == 'Create_repo':
            try:
                name = input("Enter the name of your new repository: ")
                CB.create_repo(name)
            except Exception as ex:
                print("Info about exception: ", ex)
        elif command == 'Delete_repo':
            try:
                choice = input("You want to find repo by 'Name' or 'Id'? ")
                if choice == 'Name':
                    name = username+"/"+input("Enter the name of repository you want to delete: ")
                    CB.del_repo(name)
                elif choice == 'Id':
                    del_id = int(input("Enter needed id: "))
                    CB.del_repo(del_id)
                else:
                    print("Please enter 'Name' or 'Id'.")
            except Exception as ex:
                print("Info about exception: ", ex)
        elif command == 'Get_info':
            try:
                print("You will get basic info about repo yo seek: ID, HTML_URL, "
                      "full name, owner's login, default branch, creation time, description, owner's name "
                      "and watchers count.")
                choice = input("You want to find repo by 'Name' or 'Id'? ")
                if choice == 'Name':
                    name = username + '/' + input("Enter the name of repository you seek: ")
                    l = CB.get_info(name)
                    for i in l:
                        print(i)
                elif choice == 'Id':
                    id = int(input("Enter needed id: "))
                    l = CB.get_info(id)
                    for i in l:
                        print(i)
                else:
                    print("Please enter 'Name' or 'Id'.")
            except Exception as ex:
                print("Info about exception: ", ex)
        elif command == 'Add_collaborator':
            try:
                rep_name = input("Enter the name of repository where you want to add a collaborator: ")
                col_name = input("Enter the name of collaborator you want to add: ")
                CB.add_collaborator(rep_name, col_name)
            except Exception as ex:
                print("Info about exception: ", ex)
        elif command == 'Delete_collaborator':
            try:
                rep_name = input("Enter the name of repository where you want to remove a collaborator: ")
                col_name = input("Enter the name of collaborator you want to remove: ")
                CB.del_collaborator(rep_name, col_name)
            except Exception as ex:
                print("Info about exception: ", ex)
        elif command == 'Create_branch':
            try:
                rep_name = username+'/'+input("Enter the name of repository you need: ")
                s_branch = input("Enter the name of your source branch: ")
                n_branch = input("Enter the name of your new branch: ")
                CB.cr_branch(rep_name, s_branch, n_branch)
            except Exception as ex:
                print("Info about exception: ", ex)
        elif command == 'Delete_branch':
            try:
                rep_name = username+'/'+input("Enter the name of repository you need: ")
                d_branch = input("Enter the name of your the branch you want to delete: ")
                CB.del_branch(rep_name, d_branch)
            except Exception as ex:
                print("Info about exception: ", ex)
        elif command == 'Quit':
            CB.quit()


        query = input("Do you need something? Type 'Yes' to continue. ")
        if query != "Yes":
            print("Ending...")

work()