from github import Github


def data():
    g = Github(login_or_token="1714d5de8fd7bd64e1d74fdf598e4b29bb1b63cd")
    p = g.get_user()
    print(p.login)
    print(p.id)
    print(p.avatar_url)
    print(p.created_at)
    print(p.followers)


def dataset():
    g = Github(login_or_token="1714d5de8fd7bd64e1d74fdf598e4b29bb1b63cd")
    p = g.get_user()
    repo = p.create_repo(name="my_own_repo")
    print(repo.id)
    print(repo.full_name)
    print(repo.owner.login)
    print(repo.default_branch)
    print(repo.html_url)
    repo.delete()


