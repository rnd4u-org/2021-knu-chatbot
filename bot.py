import github


def add_coll(h):
    f = 0
    while f == 0:
        print("Must I add any collaborator to this repo? (Yes/No)")
        d = input()
        if d == "No":
            f += 1
        elif d == "Yes":
            print("OK. Enter his username here please.")
            m = input()
            try:
                h.add_to_collaborators(m)
            except github.GithubException:
                print("The attempt is failed. Let's try again.")
        else:
            print("This answer is invalid. Please retry to answer correctly.")


def remove_coll(h):
    f = 0
    while f == 0:
        print("Must I remove any collaborator from this repo? (Yes/No)")
        d = input()
        if d == "No":
            f += 1
        elif d == "Yes":
            print("OK. Enter his username here please.")
            m = input()
            try:
                h.remove_from_collaborators(m)
            except github.GithubException:
                print("The attempt is failed. Let's try again.")
        else:
            print("This answer is invalid. Please retry to answer correctly.")


def add_branch(h):
    f = 0
    while f == 0:
        print("Do you want to create a branch on this repo? (Yes/No)")
        d = input()
        if d == "No":
            f += 1
        elif d == "Yes":
            print("OK. Enter a name of a new branch here.")
            m = input()
            sb = h.get_branch('main')
            h.create_git_ref(ref='refs/heads/' + m, sha=sb.commit.sha)
        else:
            print("This answer is invalid. Please retry to answer correctly.")


def remove_branch(h):
    f = 0
    while f == 0:
        print("Would you like to delete a branch on this repo? (Yes/No)")
        d = input()
        if d == "No":
            f += 1
        elif d == "Yes":
            print("OK. Enter a name of the branch you're going to delete.")
            m = input()
            try:
                src = h.get_git_ref(ref='heads/' + m)
                src.delete()
            except github.GithubException:
                print("The attempt is failed. Let's try again.")
        else:
            print("This answer is invalid. Please retry to answer correctly.")


def printer():
    f = 0
    while f == 0:
        print("Should I close the repo? (Yes/No)")
        d = input()
        if d == "Yes" or d == "No":
            f += 1
            return d
        else:
            print("This answer is invalid. Please retry to answer correctly.")


def rep(h):
    print("Do you want to create a new repository? (Yes/No)")
    x = input()
    if x == "Yes":
        print("Give it a title.")
        m = input()
        r = h.create_repo(name=m)
    elif x != "Yes" and x != "No":
        print("This answer is invalid. Please retry to answer correctly.")
        rep(h)


def delrep(h):
    x = 0
    while x == 0:
        print("Would you like to delete any repo? (Yes/No)")
        q = input()
        if q != "Yes" and q != "No":
            print("This answer is invalid. Please retry to answer correctly.")
        elif q == "Yes":
            print("Should I search for repo by name or by id? (Name/Id)")
            v = input()
            if v != "Name" and v != "Id":
                print("This answer is invalid. Please retry to answer correctly.")
            else:
                print("OK. Enter the data here please.")
                w = input()
                if v == "Name":
                    quo = 0
                    for s in h.get_repos():
                        if w == s.name:
                            s.delete()
                            quo += 1
                    if quo == 0:
                        print("The attempt is failed. Let's try again.")
                else:
                    count = 0
                    for o in h.get_repos():
                        if w == str(o.id):
                            o.delete()
                            count += 1
                    if count == 0:
                        print("The attempt is failed. Let's try again.")
        else:
            x += 1


def opening():
    num = 0
    while num == 0:
        print("Should I open any repo? (Yes/No)")
        a = input()
        if a == "Yes" or a == "No":
            num += 1
            return a
        else:
            print("This answer is invalid. Please retry to answer correctly.")


def settings(h):
    while True:
        add_coll(h)
        remove_coll(h)
        add_branch(h)
        remove_branch(h)
        s = printer()
        if s == "Yes":
            break


def opens(h):
    sign = 0
    while sign == 0:
        print("Should I search for repo by name or by id? (Name/Id)")
        st = input()
        if st != "Name" and st != "Id":
            print("This answer is invalid. Please retry to answer correctly.")
        else:
            print("OK. Enter the data here please.")
            e = input()
            if st == "Name":
                for f in h.get_repos():
                    if e == f.name:
                        sign += 1
                        print('')
                        print(f.id)
                        print(f.full_name)
                        print(f.owner.login)
                        print(f.default_branch)
                        print(f.html_url)
                        print('')
                        settings(f)
                if sign == 0:
                    print("The attempt is failed. Let's try again.")
            else:
                for f in h.get_repos():
                    if e == str(f.id):
                        sign += 1
                        print('')
                        print(f.id)
                        print(f.full_name)
                        print(f.owner.login)
                        print(f.default_branch)
                        print(f.html_url)
                        print('')
                        settings(f)
                if sign == 0:
                    print("The attempt is failed. Let's try again.")


def token(t):
    y = input()
    try:
        cycle(y)
        t += 1
        return t
    except github.GithubException:
        print("Sorry, but these credentials are invalid. Try to log in again.")
        token(0)


def cycle(z):
    g = github.Github(login_or_token=z)
    p = g.get_user()
    repo = p.create_repo(name="my_own_repo")
    repo.delete()
    while True:
        rep(p)
        delrep(p)
        k = opening()
        if k == "No":
            break
        opens(p)


print("Hello! Let's start our work! Do you have a personal access token? (Yes/No)")
s = 0
while s == 0:
    x = input()
    if x == "Yes":
        print("Please write down your token here.")
        s = token(s)
    elif x == "No":
        s += 1
        print("Please create a token and start again.")     # ідентифікація через логін-пароль не працює
    else:
        print("This answer is invalid. Please retry to answer correctly.")
