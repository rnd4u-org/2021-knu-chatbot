from github import Github
import os

token = os.getenv('GITHUB_TOKEN', 'a9500c053ffadc3eb9e69e5fcfd349602a2da6e3')
g = Github(token)

def subtask1(g):
    user = g.get_user()
    results1 = []
    results1.append(user.login)
    results1.append(user.id)
    results1.append(user.avatar_url)
    results1.append(user.created_at)
    results1.append(user.followers)
    return results1

def subtask2(g):
    user = g.get_user()
    results2 = []
    repo = user.create_repo("liviiaaaa")
    results2.append(repo.id)
    results2.append(repo.html_url)
    results2.append(repo.full_name)
    results2.append(repo.owner.login)
    results2.append(repo.default_branch)  
    repo = g.get_repo("liviiaaaa/liviiaaaa")
    repo.delete()
    return results2

results1 = subtask1(g)
results2 = subtask2(g)

fname = input('Файл: ')
f = open(fname,'w')
f.write("- Enviroment: Python(Simple Scripting)" + "\n")
f.write("- Liviia Firishchak" + "\n")
f.write("- login , id , avatar_url , created_at , followers :" + "\n")
for i in results1:
    if results1.index(i) < (len(results1) - 1):
        f.write(str(i) + " , ")
    elif results1.index(i) == (len(results1) - 1):
        f.write(str(i) + " .")
    else:
        break
f.write("\n")
f.write("- id , html_url , full_name , owner_login , default_branch :" + "\n")
for j in results2:
    if results2.index(j) < (len(results2) - 1):
        f.write(str(j) + " , ")
    elif results2.index(j) == (len(results2) - 1):
        f.write(str(j) + " .")
    else:
        break
f.close()
