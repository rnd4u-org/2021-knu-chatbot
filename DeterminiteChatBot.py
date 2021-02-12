
from github import Github
import os


def get_token():
    token = input("Привет,введи свой токен: ")
    token = os.getenv('GITHUB_TOKEN', str(token))
    g = Github(token)
    return g


def actions():
    print("""
        1 - создать\удалить репозиторий
        2 - найти репозиторий и вернуть базовую информацию
        3 - добавить\удалить участников репозитория
        4 - создать\удалить ветку
        5 - выход""")
    chosen_action = input(": ")
    return chosen_action


def action_1():
    print("""Выберите действие:
        1 - создать репозиторий с именем
        2 - удалить репозиторий с именем
        3 - выход""")
    first_block_cho_act = input(": ")
    return first_block_cho_act


def action_exit(i):
    print("""Хотите сделать что-то еще?
            1 - да
            2 - нет""")
    choice_y_no = input(": ")
    if choice_y_no == "2":
        i += 1
    else:
        pass
    return i


def create_repo():
    name_repo = input("Введите имя репозитория для создания: ")
    try:
        repo = user.create_repo(name_repo)
        print("""Успешно создан""")
    except Exception:
        print("Этот репозиторий уже существует")


def delete_repo():
    print("Введите имя репозиторя для удаления")
    name_repo = input(": ")
    try:
        repo = g.get_repo("{}/{}".format(user.login, name_repo))
        repo.delete()
        print("Успешно удален")
    except Exception:
        print("Этого репозитория не существует")




def action_2():
    print("""Выберите действие:
        1 - найти репозиторий и вернуть базовую информацию
        2 - выход""")
    sec_block_cho_act = input(": ")
    return sec_block_cho_act


def find_repo():
    print("Введите имя репозитория который нужно найти")
    name_repo = input(": ")
    try:
        repo = g.get_repo("{}/{}".format(user.login, name_repo))
        print("""Базовая информация репозитория:
        id of repository: {}
        html_url of repository: {}
        full_name of repository: {}
        owner.login: {}
        default_branch: {}""".format(repo.id, repo.html_url, repo.full_name, repo.owner.login, repo.default_branch))
    except Exception:
        print("Этот репозиторий не существует")




def action_3():
    print("""Выберите действие:
         1 - добавить участника в репозиторий
         2 - удалить участника из репозитория
         3 - выход""")
    third_block_cho_act = input(": ")
    return third_block_cho_act


def add_repo():
    print("Введите имя репозитория.")
    name_repo = input(": ")
    try:
        repo = g.get_repo("{}/{}".format(user.login, name_repo))
        print("Введите имя участника для добавления")
        collab_name = input(": ")
        try:
            repo.add_to_collaborators(collab_name)
            print("Добавлен")
        except Exception:
            print("Не может быть добавлен")
    except Exception:
        print("Этот репозиторий не существует")


def remove_repo():
    print("Введите имя репозитория")
    name_repo = input(": ")
    try:
        repo = g.get_repo("{}/{}".format(user.login, name_repo))
        print("Введите имя участника для удаления")
        collab_name = input(": ")
        try:
            repo.remove_from_collaborators(collab_name)
            print("Удален")
        except Exception:
            print("Участник не найден")
    except Exception:
        print("Этот репозиторий не найден")


def action_4():
    print("""Выберите действие:
        1 - создать ветку 
        2 - удалить ветку
        3 - выход""")
    four_block_cho_act = input(": ")
    return four_block_cho_act


def create_branch():
    print("Введите имя репозитория")
    name_repo = input(": ")
    try:
        repo = g.get_repo("{}/{}".format(user.login, name_repo))
        print("Введите имя ветки для создания")
        branch = input(": ")
        sb = repo.get_branch("main")
        repo.create_git_ref(ref='refs/heads/' + branch, sha=sb.commit.sha)
        print("Создана")
    except Exception:
        print("Этот репозиторий не найден")


def delete_branch():
    print("Введите имя репозитория")
    name_repo = input(": ")
    try:
        repo = g.get_repo("{}/{}".format(user.login, name_repo))
        print("Введите имя ветки для удаления")
        branch = input(": ")
        try:
            sb = repo.get_git_ref(ref='heads/' + branch)
            sb.delete()
            print("Удалена")
        except Exception:
            print("Эта ветка не найдена")
    except Exception:
        print("Этот репозиторий не найден")


g = get_token()
user = g.get_user()
try:
    user.login
except Exception:
    print("Токен не верный. Попробуйте ещё раз")
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
            print("Вы ввели не верное число попробуйте еще раз")
    if chosen_action == "2":
        s = action_2()
        if s == "1":
            find_repo()
            i = action_exit(i)
        if s == "2":
            i += 1
        if s not in ["1", "2"]:
            print("Вы ввели не верное число попробуйте еще раз")
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
            print("Вы ввели не верное число попробуйте еще раз")
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
            print("Вы ввели не верное число попробуйте еще раз")
    if chosen_action == "5":
        i += 1
    if chosen_action not in ["1", "2", "3", "4", "5"]:
        print("Вы ввели не верное число попробуйте еще раз")
print("Process is finished.")