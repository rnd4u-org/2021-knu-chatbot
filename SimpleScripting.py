from github import Github
f=open('text.txt','w')

def Task1():
    g = Github(login_or_token="035aa5e19aa349c8aae73016861bc4a83c0dc003")
    p = g.get_user()
    f.write('Task1 \n')
    f.write(p.login)
    f.write(str(p.id)+'\n')
    f.write(str(p.avatar_url)+'\n')
    f.write(str(p.created_at)+'\n')
    f.write(str(p.followers)+'\n')


def Task2():
    g = Github(login_or_token="035aa5e19aa349c8aae73016861bc4a83c0dc003")
    p = g.get_user()
    repo = p.create_repo(name="1233124")
    f.write('Task2 \n')
    f.write(str(repo.id)+'\n')
    f.write(str(repo.full_name)+'\n')
    f.write(str(repo.owner.login)+'\n')
    f.write(str(repo.default_branch)+'\n')
    f.write(str(repo.html_url)+'\n')
    repo.delete()
Task1()
Task2()
