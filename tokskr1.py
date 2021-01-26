from github import Github
import requests
f = open('skr12.txt', 'tw', encoding='utf-8')
f.write('Environment: Python (simple scripting)'+"\n"+"vlad bilenko"+"\n")



tok = Github('token')
username = "login"






def skr1(name):
    url = f"https://api.github.com/users/{name}"
    user_data = requests.get(url).json()

    f.write('skr1'+"\n")
    f.write('login '+user_data.get('login')+"\n")
    f.write('id '+str(user_data.get('id'))+"\n")
    f.write('avatar_url ' + user_data.get('avatar_url') + "\n")
    f.write('created_at ' + user_data.get('created_at') + "\n")
    f.write('followers ' + str(user_data.get('followers')) + "\n")

def skr2(token):

    user = token.get_user()
    repo = user.create_repo('zigmunt')
    repo1=user.get_repo('zigmunt')

    f.write('skr2' + "\n")
    f.write('id '+str(repo1.id)+"\n")
    f.write('html_url ' + repo1.html_url + "\n")
    f.write('full_name ' + repo1.full_name + "\n")
    f.write('owner.login ' + repo1.owner.login + "\n")
    f.write('default_branch ' + repo1.default_branch + "\n")


    repo1.delete()
skr1(username)
skr2(tok)