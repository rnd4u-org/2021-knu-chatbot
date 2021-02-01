from github import Github
import github
import os
import requests

def rn (rname):
    repo = user.create_repo(rname,auto_init=True)

def rnd(rname):
    repo1 = user.get_repo(rname)
    repo1.delete()

def rni(rid):
    repo1 = g.get_repo(int(rid))
    repo1.delete()

def sern(rname):
    repo1 = user.get_repo(rname)
    print('id '+str(repo1.id))
    print('html_url ' + repo1.html_url)
    print('full_name ' + repo1.full_name)
    print('owner.login ' + repo1.owner.login)
    print('default_branch ' + repo1.default_branch)

def serid(rid):
    repo1 = g.get_repo(int(rid))
    print('id '+str(repo1.id))
    print('html_url ' + repo1.html_url)
    print('full_name ' + repo1.full_name)
    print('owner.login ' + repo1.owner.login)
    print('default_branch ' + repo1.default_branch)



def invite(repo_name,person):
    repo1 = user.get_repo(repo_name)
    repo1.add_to_collaborators(person)


def excommunicado(repo_name,person):
    repo1 = user.get_repo(repo_name)
    repo1.remove_from_collaborators(person)

def pending_list(repo_name):
    repo1 = user.get_repo(repo_name)
    for inv in repo1.get_pending_invitations():
        print(inv)

def pending_remove(repo_name,person_id):
    repo1 = user.get_repo(repo_name)
    repo1.remove_invitation(int(person_id))





def cr_branch(repo_name,branch_name):
    repo1 = user.get_repo(repo_name)
    source_branch = 'main'
    sb = repo1.get_branch(source_branch)
    repo1.create_git_ref(ref='refs/heads/' + branch_name, sha=sb.commit.sha)


def del_branch(repo_name,branch_name):
    repo1 = user.get_repo(repo_name)
    br = repo1.get_git_ref(ref='heads/' + branch_name)
    br.delete()


def startmenu():
    try:
        tok = input("введите токен ")
        token = os.getenv('GITHUB_TOKEN', tok)
        global g
        g = Github(token)
        global user
        user = g.get_user()
        print('приветствую '+user.login)
        menu0()
    except:
        print('неправильный токен ')
        startmenu()









def menu0():
    print("1-Создать / удалить репозиторий 2-Найдите репозиторий  3-Добавить / удалить соавторов 4-Создать / удалить ветку 5 -изменить токен")
    t=input("выберете вариант ")
    if t=='1':
        print('1')
        menu1()
    elif t=='2':
        print('2')
        menu2()
    elif t=='3':
        print('3')
        menu3()
    elif t=='4':
        print('4')
        menu4()
    elif t == '5':
        print('5')
        startmenu()
    else:
        print("выберете правилиный вариант")
        menu0()




def menu1():
    print("1-Создать репозиторий 2-удалить  с именем  3-удалить  с идентификатором 4-в прошлое меню")
    t = input("выберете вариант ")
    if t=='1':
        name=input("введите имя ")
        try:
            rn(name)
            print('репозиторий создан')
        except Exception as e :
            print('репозиторий не создан,измените имя')
        menu1()

    elif t=='2':
        name = input("введите имя ")
        try:
            rnd(name)
            print('репозиторий удален')
        except Exception as e:
            print('репозиторий не найден')
        menu1()

    elif t=='3':

        try:
            id = int(input("введите id "))
            rni(id)
            print('репозиторий удален')
        except Exception as e:
            print('репозиторий не найден либо не правильно введен айди')
        menu1()

    elif t=='4':
        menu0()
    else:
        print("выберете правилиный вариант")
        menu1()







def menu2():
    print("1-найти по имени  2-найти по id   3-в прошлое меню")
    t = input("выберете вариант ")
    if t=='1':
        name=input("введите имя ")
        try:
            sern(name)
            print('репозиторий найден')
        except Exception as e :
            print('репозиторий не найден')
        menu2()
    elif t=='2':
        id = input("введите имя ")
        try:
            serid(id)
            print('репозиторий найден')
        except Exception as e:
            print('репозиторий не найден')
        menu2()
    elif t == '3':
        menu0()
    else:
        print("выберете правилиный вариант")
        menu2()




def menu3():
    print("1-пригласить 2-выгнать  3-список приглашенных(id) 4-убрать из приглашенных(id) 5-прошлое меню")
    t = input("выберете вариант ")
    if t=='1':
        repo_name=input("введите имя репозитория ")
        person = input("введите ник ")
        try:
            invite(repo_name,person)
            print('приглашен')
        except Exception as e :
            print('нет такого репозитория либо человека')
        menu3()
    if t=='2':
        repo_name=input("введите имя репозитория ")
        person = input("введите ник ")
        try:
            excommunicado(repo_name,person)
            print(person+' excommunicado')
        except Exception as e :
            print('нет такого репозитория либо человека')
        menu3()
    if t=='3':
        repo_name=input("введите имя репозитория ")
        try:
            print('список приглашенных')
            pending_list(repo_name)
        except Exception as e :
            print('нет такого репозитория')
        menu3()

    if t=='4':
        repo_name=input("введите имя репозитория ")
        person_id = input("введите id приглашения ")
        try:
            pending_remove(repo_name,person_id)
            print('приглашение отменено')
        except Exception as e :
            print('нет такого репозитория либо приглашения')
        menu3()

    elif t == '5':
        menu0()
    else:
        print("выберете правилиный вариант")
        menu3()



def menu4():
    print("1-создать ветку 2-удалить ветку  3-прошлое меню")
    t = input("выберете вариант ")
    if t=='1':
        repo_name=input("введите имя репозитория ")
        branch_name = input("введите имя ветки ")
        try:
            cr_branch(repo_name,branch_name)
            print('ветка создана')
        except Exception as e :
            print('нет такого репозитория либо нельзя создать ветку')
        menu4()
    elif t=='2':
        repo_name=input("введите имя репозитория ")
        branch_name = input("введите имя ветки ")
        try:
            del_branch(repo_name,branch_name)
            print('ветка удалена')
        except Exception as e :
            print('нет такого репозитория либо ветки')
        menu4()
    elif t == '3':
        menu0()
    else:
        print("выберете правилиный вариант")
        menu4()






startmenu()







