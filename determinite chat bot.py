from github import Github
import os


def get_token():
    token = input("Hello!Input your personal token: ")
    token = os.getenv('GITHUB_TOKEN', str(token))
    g = Github(token)
    return g


def actions():
    print("""
        1 - create/delete repository with name
        2 - find repository with name/id and return basic information
        3 - add/remove collaborators to/from repository
        4 - create branch/delete branch
        5 - exit""")
    chosen_action = input(": ")
    return chosen_action


def action_1():
    print("""Choose the action:
        1 - create repository with name
        2 - delete repository with name
        3 - exit""")
    first_block_cho_act = input(": ")
    return first_block_cho_act


def action_exit(i):
    print("""Whould you like to do something else ?
            1 - yes
            2 - no""")
    choice_y_no = input(": ")
    if choice_y_no == "2":
        i += 1
    else:
        pass
    return i


def create_repo():
    name_repo = input("Please, input name of repository for creating: ")
    try:
        repo = user.create_repo(name_repo)
        print("""Successfully created!""")
    except Exception:
        print("This repository already exists!")


def delete_repo():
    print("Please, input name of repository for deleting.")
    name_repo = input(": ")
    try:
        repo = g.get_repo("{}/{}".format(user.login, name_repo))
        repo.delete()
        print("Successfully deleted!")
    except Exception:
        print("This repository doesn't exists!")




def action_2():
    print("""Choose the action:
        1 - find repo with name 
        2 - exit""")
    sec_block_cho_act = input(": ")
    return sec_block_cho_act


def find_repo():
    print("Please, input name of repository for finding.")
    name_repo = input(": ")
    try:
        repo = g.get_repo("{}/{}".format(user.login, name_repo))
        print("""Basic information about repository:
        id of repository: {}
        html_url of repository: {}
        full_name of repository: {}
        owner.login: {}
        default_branch: {}""".format(repo.id, repo.html_url, repo.full_name, repo.owner.login, repo.default_branch))
    except Exception:
        print("This repository doesn't exists!")




def action_3():
    print("""Choose the action:
         1 - add collaborators to repository
         2 - remove collaborators  from repository
         3 - exit""")
    third_block_cho_act = input(": ")
    return third_block_cho_act


def add_repo():
    print("Please, input name of repository.")
    name_repo = input(": ")
    try:
        repo = g.get_repo("{}/{}".format(user.login, name_repo))
        print("Please, input name of collaborators for adding.")
        collab_name = input(": ")
        try:
            repo.add_to_collaborators(collab_name)
            print("Added!")
        except Exception:
            print("Can't be added to collaborators!")
    except Exception:
        print("This repository doesn't exists!")


def remove_repo():
    print("Please, input name of repository.")
    name_repo = input(": ")
    try:
        repo = g.get_repo("{}/{}".format(user.login, name_repo))
        print("Please, input name of collaborators for removing.")
        collab_name = input(": ")
        try:
            repo.remove_from_collaborators(collab_name)
            print("Done!")
        except Exception:
            print("This collaborator doesn't found!")
    except Exception:
        print("This repository doesn't exists!")


def action_4():
    print("""Choose the action:
        1 - create branch
        2 - delete branch
        3 - exit""")
    four_block_cho_act = input(": ")
    return four_block_cho_act


def create_branch():
    print("Please, input name of repository.")
    name_repo = input(": ")
    try:
        repo = g.get_repo("{}/{}".format(user.login, name_repo))
        print("Please, input name of branch for creating")
        branch = input(": ")
        sb = repo.get_branch("main")
        repo.create_git_ref(ref='refs/heads/' + branch, sha=sb.commit.sha)
        print("Created!")
    except Exception:
        print("This repository doesn't exists!")


def delete_branch():
    print("Please, input name of repository.")
    name_repo = input(": ")
    try:
        repo = g.get_repo("{}/{}".format(user.login, name_repo))
        print("Please, input name of branch for deleting")
        branch = input(": ")
        try:
            sb = repo.get_git_ref(ref='heads/' + branch)
            sb.delete()
            print("Deleted!")
        except Exception:
            print("This branch doesn't exists!")
    except Exception:
        print("This repository doesn't exists!")


g = get_token()
user = g.get_user()
try:
    user.login
except Exception:
    print("Token is incorrect!Try again.")
    g = get_token()
i = 0
while i == 0:
    chosen_action = actions()
    if chosen_action == "1":
        f = action_1()
        if f == "1":
            create_repo()
            i = action_exit(i)
        if f == "2":
            delete_repo()
            i = action_exit(i)
        if f == "3":
            i += 1
        if f not in ["1", "2", "3", "4"]:
            print("Your input is not correct! Try again.")
    if chosen_action == "2":
        s = action_2()
        if s == "1":
            find_repo()
            i = action_exit(i)
        if s == "2":
            i += 1
        if s not in ["1", "2"]:
            print("Your input is not correct! Try again.")
    if chosen_action == "3":
        t = action_3()
        if t == "1":
            add_repo()
            i = action_exit(i)
        if t == "2":
            remove_repo()
            i = action_exit(i)
        if t == "3":
            i += 1
        if t not in ["1", "2", "3"]:
            print("Your input is not correct! Try again.")
    if chosen_action == "4":
        four = action_4()
        if four == "1":
            create_branch()
            i = action_exit(i)
        if four == "2":
            delete_branch()
            i = action_exit(i)
        if four == "3":
            i += 1
        if four not in ["1", "2", "3"]:
            print("Your input is not correct! Try again.")
    if chosen_action == "5":
        i += 1
    if chosen_action not in ["1", "2", "3", "4", "5"]:
        print("Your input is not correct! Try again.")
print("Process is finished.")