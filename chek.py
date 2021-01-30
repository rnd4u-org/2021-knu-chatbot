from github import Github
import requests

token = 'ad3fa802d6c45d5af915038541d2d19a9730fd9e'
g = Github(token)
u = g.get_user()
n = input('Enter repository`s name:  ')

def subtask1():
    f.write('Login:  '+(u.login)+'\n')
    f.write('ID:  '+str(u.id)+'\n')
    f.write('Avatar url:  '+(u.avatar_url)+'\n')
    f.write('Created at:  '+str(u.created_at)+'\n')
    f.write('Followers:  '+str(u.followers)+'\n'+'\n')


def subtask2():
    r = u.create_repo(n)
    r1 = u.get_repo(n)
    f.write('ID:  '+str(r1.id) +'\n')
    f.write('Full name:  '+r1.full_name +'\n')
    f.write('Owner login:  '+r1.owner.login +'\n')
    f.write('Default branch:  '+r1.default_branch +'\n')
    f.write('HTML url:  '+r1.html_url)
    r1.delete()

f = open('result.txt', 'w')
f.write('Environment: Python(simple scripting)'+'\n')
f.write('Diana Andresiuk'+'\n'+'\n')

f.write('SubTask1:\n'+'\n')
subtask1()

f.write('SubTask2:\n'+'\n')
subtask2()
f.close()