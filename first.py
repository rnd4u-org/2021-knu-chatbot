from github import Github

token = '13dd7ed083d0bef36f8bf8f9b770748167026a9c'
t = Github(token)
us = t.get_user()
inp = input('Enter repository`s name:  ')

def subtask1():
    f.write('Login:  '+(us.login)+'\n')
    f.write('ID:  '+str(us.id)+'\n')
    f.write('Avatar url:  '+(us.avatar_url)+'\n')
    f.write('Created at:  '+str(us.created_at)+'\n')
    f.write('Followers:  '+str(us.followers)+'\n'+'\n')

def subtask2():
    us.create_repo(inp)
    g = us.get_repo(inp)
    f.write('ID:  '+str(g.id) +'\n')
    f.write('Full name:  '+g.full_name +'\n')
    f.write('Owner login:  '+g.owner.login +'\n')
    f.write('Default branch:  '+g.default_branch +'\n')
    f.write('HTML url:  '+g.html_url)
    g.delete()

f = open('lol.txt', 'w')
f.write('Environment: Python(simple scripting)'+'\n')
f.write('Yaroslav Pishchanskyi'+'\n'+'\n')

f.write('SubTask1:\n'+'\n')
subtask1()

f.write('SubTask2:\n'+'\n')
subtask2()

f.close()





































