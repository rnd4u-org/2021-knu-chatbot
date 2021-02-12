from github import Github


def create_rep(user, rname):
    user.create_repo(rname,auto_init=True)


def delete_rep(user, rname):
    user.get_repo(rname).delete()


def delete_rep_by_id(g, rid):
    g.get_repo(int(rid)).delete()


def sern(user, rname):
    repo1 = user.get_repo(rname)
    print('id '+str(repo1.id))
    print('html_url ' + repo1.html_url)
    print('full_name ' + repo1.full_name)
    print('owner.login ' + repo1.owner.login)
    print('default_branch ' + repo1.default_branch)


def serid(g, rid):
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


def cr_branch(user, repo_name,branch_name):
    repo1 = user.get_repo(repo_name)
    source_branch = 'main'
    sb = repo1.get_branch(source_branch)
    repo1.create_git_ref(ref='refs/heads/' + branch_name, sha=sb.commit.sha)


def del_branch(user, repo_name,branch_name):
    repo1 = user.get_repo(repo_name)
    br = repo1.get_git_ref(ref='heads/' + branch_name)
    br.delete()

#конектимся по токену
token = input("enter your token ")
g = Github(token)
user = g.get_user()
print('Ваш логин - ', user)

while True:
	print('1 - create repository')
	print('2 - remove repository')
	print('3 - find repository by name')
	print('4 - find repository by id')
	print('5 - create branch')
	print('6 - remove branch')
	print('7 - exit')
	i = int(input())
	if i == 1:
		#создание репозитория
		name = input("enter the name of the new repository ")
		create_rep(user, name)
	elif i == 2:
		#удаление репозитория
		name = input("enter the name of the repository to remove ")
		delete_rep(user, name)
		_id = input("enter id of the repository to remove ")
		delete_rep_by_id(g, _id)
	elif i == 3:
		#найти реп по имени
		name = input("enter name ")
		sern(user, name)
	elif i == 4:
		#найти реп по id
		_id = input("enter _id ")
		serid(g, _id)
	elif i == 5:
		#создать ветку
		repo_name = input("enter name of the repository ")
		branch_name = input("enter branch name ")
		cr_branch(user, repo_name,branch_name)
	elif i == 6:
		#удалить ветку
		repo_name=input("enter name of the repository ")
		branch_name = input("enter branch name ")
		del_branch(user, repo_name,branch_name)
	elif i == 7:
		break
	else:
		print('wrong choice')
