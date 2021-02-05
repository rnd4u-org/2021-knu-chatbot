from github import Github
import PySimpleGUI as sg
# CHAT BOT WITH GUI AND EXCEPTION OPERATOR

# CREATE REPO FUNCTION
def repo():
    layout = [
        [sg.Text('Do you want to create repo?'),
         ],
        [sg.Button('YES'), sg.Button('NO')]
    ]
    window = sg.Window('Create repo', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in ('NO'):
            window.close()
            menu()
        elif event == 'YES':
            window.close()
            layout = [
                [sg.Text('Enter the name of repo:'),
                 ],
                [sg.InputText(key='-IN-')],
                [sg.Button('OK')]
            ]
            window = sg.Window('Create repo', layout)
            while True:
                event, values = window.read()
                if event in (None, 'Exit'):
                    break
                elif event == 'OK':
                    window.close()
                    n = values['-IN-']
                    try:
                        r = u.create_repo(n)
                        window.close()
                        layout = [
                            [sg.Text('CONGRATULATIONS! You created the repo ' + n)],
                            [sg.Button('OK')]
                        ]
                        window = sg.Window('Create repo', layout)
                        while True:
                            event, values = window.read()
                            if event in (None, 'Exit'):
                                break
                            elif event == 'OK':
                                window.close()
                                menu()
                                break
                    except Exception:
                        layout = [
                            [sg.Text(un + ', you wrote the wrong repo`s name or this repo is already created. Try again')],
                            [sg.Button('OK')]
                        ]
                        window = sg.Window('ERROR!', layout)
                        while True:
                            event, values = window.read()
                            if event in (None, 'Exit'):
                                break
                            elif event in ('OK'):
                                window.close()
                                repo()

# DELETE REPO FUNCTION
def drepo():
    layout = [
        [sg.Text('Do you want to delete repo?'),
         ],
        [sg.Button('YES'), sg.Button('NO')]
    ]
    window = sg.Window('Delete repo', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in ('NO'):
            window.close()
            menu()
        elif event == 'YES':
            window.close()
            layout = [
                [sg.Text('Do you want to find repo by name or id?'),
                 ],
                [sg.Button('Name'), sg.Button('ID')]
            ]
            window = sg.Window('Delete repo', layout)
            while True:
                event, values = window.read()
                if event in (None, 'Exit'):
                    break
                elif event == 'Name':
                    window.close()
                    layout = [
                        [sg.Text('Enter the repo`s name:'),
                         ],
                        [sg.InputText(key='-IN-')],
                        [sg.Button('OK')]
                    ]
                    window = sg.Window('Delete repo', layout)
                    while True:
                        event, values = window.read()
                        if event in (None, 'Exit'):
                            break
                        elif event in ('OK'):
                            window.close()
                            n = values['-IN-']
                            try:
                                r = u.get_repo(n)
                                r.delete()
                                window.close()
                                layout = [
                                    [sg.Text('CONGRATULATIONS! You deleted the repo ' + n)],
                                    [sg.Button('OK')]
                                ]
                                window = sg.Window('Delete repo', layout)
                                while True:
                                    event, values = window.read()
                                    if event in (None, 'Exit'):
                                        break
                                    elif event == 'OK':
                                        window.close()
                                        menu()
                                        break
                            except Exception:
                                layout = [
                                    [sg.Text(un + ', you wrote the wrong repo`s name. Try again.')],
                                    [sg.Button('OK')]
                                ]
                                window = sg.Window('ERROR!', layout)
                                while True:
                                    event, values = window.read()
                                    if event in (None, 'Exit'):
                                        break
                                    elif event in ('OK'):
                                        window.close()
                                        drepo()
                elif event == 'ID':
                    window.close()
                    layout = [
                        [sg.Text('Enter the repo`s ID:'),
                         ],
                        [sg.InputText(key='-IN-')],
                        [sg.Button('OK')]
                    ]
                    window = sg.Window('Delete repo', layout)
                    while True:
                        event, values = window.read()
                        if event in (None, 'Exit'):
                            break
                        elif event in ('OK'):
                            window.close()
                            i = values['-IN-']
                            try:
                                for r1 in u.get_repos():
                                    if int(i) == r1.id:
                                        print(r1.full_name)
                                        r1.delete()
                                        window.close()
                                        layout = [
                                            [sg.Text('CONGRATULATIONS! You deleted the repo'), sg.Text(r1.name)],
                                            [sg.Button('OK')]
                                        ]
                                        window = sg.Window('Delete repo', layout)
                                        while True:
                                            event, values = window.read()
                                            if event in (None, 'Exit'):
                                                break
                                            elif event == 'OK':
                                                window.close()
                                                menu()
                                                break
                            except Exception:
                                layout = [
                                    [sg.Text(un + ', you wrote the wrong repo`s ID. Try again.')],
                                    [sg.Button('OK')]
                                ]
                                window = sg.Window('ERROR!', layout)
                                while True:
                                    event, values = window.read()
                                    if event in (None, 'Exit'):
                                        break
                                    elif event in ('OK'):
                                        window.close()
                                        drepo()

# GET REPO FUNCTION
def grepo():
    layout = [
        [sg.Text('Do you want to get repo`s information?'),
         ],
        [sg.Button('YES'), sg.Button('NO')]
    ]
    window = sg.Window('Get repo', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in ('NO'):
            window.close()
            menu()
        elif event == 'YES':
            window.close()
            layout = [
                [sg.Text('Do you want to find repo by name or ID?')],
                [sg.Button('Name'), sg.Button('ID')]
            ]
            window = sg.Window('Get repo', layout)
            while True:
                event, values = window.read()
                if event in (None, 'Exat'):
                    break
                elif event == ('Name'):
                    window.close()
                    layout = [
                        [sg.Text('Enter the name of repo:'),
                         ],
                        [sg.InputText(key='-IN-')],
                        [sg.Button('OK')]
                    ]
                    window = sg.Window('Get repo', layout)
                    while True:
                        event, values = window.read()
                        if event in (None, 'Exit'):
                            break
                        elif event == 'OK':
                            window.close()
                            n = values['-IN-']
                            try:
                                r = u.get_repo(n)
                                layout = [
                                    [sg.Text('ID:  '), sg.Text(r.id)],
                                    [sg.Text('Full name:  '), sg.Text(r.full_name)],
                                    [sg.Text('Owner login:  '), sg.Text(r.owner.login)],
                                    [sg.Text('Default branch:  '), sg.Text(r.default_branch)],
                                    [sg.Text('HTML url:  '), sg.Text(r.html_url)],
                                    [sg.Button('OK')]
                                ]
                                window = sg.Window('Get repo', layout)
                                while True:
                                    event, values = window.read()
                                    if event in (None, 'Exit'):
                                        break
                                    elif event == ('OK'):
                                        window.close()
                                        menu()
                            except Exception:
                                layout = [
                                    [sg.Text(un + ', you wrote the wrong repo`s name. Try again')],
                                    [sg.Button('OK')]
                                ]
                                window = sg.Window('ERROR!', layout)
                                while True:
                                    event, values = window.read()
                                    if event in (None, 'Exit'):
                                        break
                                    elif event in ('OK'):
                                        window.close()
                                        grepo()
                elif event == ('ID'):
                    window.close()
                    layout = [
                        [sg.Text('Enter the ID of repo:'),
                         ],
                        [sg.InputText(key='-IN-')],
                        [sg.Button('OK')]
                    ]
                    window = sg.Window('Get repo', layout)
                    while True:
                        event, values = window.read()
                        if event in (None, 'Exit'):
                            break
                        elif event == 'OK':
                            window.close()
                            i = values['-IN-']
                            try:
                                for r1 in u.get_repos():
                                    if int(i) == r1.id:
                                        layout = [
                                            [sg.Text('ID:  '), sg.Text(r1.id)],
                                            [sg.Text('Full name:  '), sg.Text(r1.full_name)],
                                            [sg.Text('Owner login:  '), sg.Text(r1.owner.login)],
                                            [sg.Text('Default branch:  '), sg.Text(r1.default_branch)],
                                            [sg.Text('HTML url:  '), sg.Text(r1.html_url)],
                                            [sg.Button('OK')]
                                        ]
                                        window = sg.Window('Get repo', layout)
                                        while True:
                                            event, values = window.read()
                                            if event in (None, 'Exit'):
                                                break
                                            elif event == ('OK'):
                                                window.close()
                                                menu()
                                    else:
                                        window.close()
                                        layout = [
                                            [sg.Text(un + ', you wrote the wrong repo`s name. Try again')],
                                            [sg.Button('OK')]
                                        ]
                                        window = sg.Window('ERROR!', layout)
                                        while True:
                                            event, values = window.read()
                                            if event in (None, 'Exit'):
                                                break
                                            elif event in ('OK'):
                                                window.close()
                                                grepo()

                            except Exception:
                                layout = [
                                    [sg.Text(un + ', you wrote the wrong repo`s name. Try again')],
                                    [sg.Button('OK')]
                                ]
                                window = sg.Window('ERROR!', layout)
                                while True:
                                    event, values = window.read()
                                    if event in (None, 'Exit'):
                                        break
                                    elif event in ('OK'):
                                        window.close()
                                        grepo()

# ADD COLLABORATOR FUNCTION
def add_c():
    layout = [
        [sg.Text('Do you want to add collaborator into your repo?')],
        [sg.Button('YES'), sg.Button('NO')]
    ]
    window = sg.Window('Add col', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in ('NO'):
            window.close()
            menu()
        elif event == 'YES':
            window.close()
            layout = [
                [sg.Text('Enter the name of repo in which you want to add collaborator:')],
                [sg.InputText(key='-IN-')],
                [sg.Button('OK')]
            ]
            window = sg.Window('Add col', layout)
            while True:
                event, values = window.read()
                if event in (None, 'Exit'):
                    break
                elif event == 'OK':
                    window.close()
                    n = values['-IN-']
                    try:
                        r = u.get_repo(n)
                        window.close()
                        layout = [
                            [sg.Text('Enter the login of the new collaborator:')],
                            [sg.InputText(key='-IN1-')],
                            [sg.Button('OK')]
                        ]
                        window = sg.Window('Add col', layout)
                        while True:
                            event, values = window.read()
                            if event in (None, 'Exit'):
                                break
                            elif event == 'OK':
                                window.close()
                                l = values['-IN1-']
                                try:
                                    r.add_to_collaborators(l)
                                    window.close()
                                    layout = [
                                        [sg.Text('CONGRATULATIONS! You added collaborator ' + l + 'to the repo ' + n)],
                                        [sg.Button('OK')]
                                    ]
                                    window = sg.Window('Add col', layout)
                                    while True:
                                        event, values = window.read()
                                        if event in (None, 'Exit'):
                                            break
                                        elif event == 'OK':
                                            window.close()
                                            menu()
                                            break
                                except Exception:
                                    layout = [
                                        [sg.Text(un + ', you wrote the wrong col`s name or this col is already added. Try again')],
                                        [sg.Button('OK')]
                                    ]
                                    window = sg.Window('ERROR!', layout)
                                    while True:
                                        event, values = window.read()
                                        if event in (None, 'Exit'):
                                            break
                                        elif event in ('OK'):
                                            window.close()
                                            add_c()
                    except Exception:
                        layout = [
                            [sg.Text(un + ', you wrote the wrong repo`s name. Try again')],
                            [sg.Button('OK')]
                        ]
                        window = sg.Window('ERROR!', layout)
                        while True:
                            event, values = window.read()
                            if event in (None, 'Exit'):
                                break
                            elif event in ('OK'):
                                window.close()
                                add_c()

# REMOVE COLLABORATOR FUNCTION
def rem_c():
    layout = [
        [sg.Text('Do you want to remove collaborator from your repo?')],
        [sg.Button('YES'), sg.Button('NO')]
    ]
    window = sg.Window('Remove col', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in ('NO'):
            window.close()
            menu()
        elif event == 'YES':
            window.close()
            layout = [
                [sg.Text('Enter the name of repo from which you want to delete collaborator:')],
                [sg.InputText(key='-IN-')],
                [sg.Button('OK')]
            ]
            window = sg.Window('Remove col', layout)
            while True:
                event, values = window.read()
                if event in (None, 'Exit'):
                    break
                elif event == 'OK':
                    window.close()
                    n = values['-IN-']
                    try:
                        r = u.get_repo(n)
                        window.close()
                        layout = [
                            [sg.Text('Enter the login of the collaborator you want to remove:')],
                            [sg.InputText(key='-IN1-')],
                            [sg.Button('OK')]
                        ]
                        window = sg.Window('Remove col', layout)
                        while True:
                            event, values = window.read()
                            if event in (None, 'Exit'):
                                break
                            elif event == 'OK':
                                window.close()
                                l = values['-IN1-']
                                try:
                                    r.remove_from_collaborators(l)
                                    window.close()
                                    layout = [
                                        [sg.Text('CONGRATULATIONS! You removed collaborator ' + l + 'from the repo ' + n)],
                                        [sg.Button('OK')]
                                    ]
                                    window = sg.Window('Remove col', layout)
                                    while True:
                                        event, values = window.read()
                                        if event in (None, 'Exit'):
                                            break
                                        elif event == 'OK':
                                            window.close()
                                            menu()
                                            break
                                except Exception:
                                    layout = [
                                        [sg.Text(un + ', you wrote the wrong col`s name or this col is alrady deleted. Try again')],
                                        [sg.Button('OK')]
                                    ]
                                    window = sg.Window('ERROR!', layout)
                                    while True:
                                        event, values = window.read()
                                        if event in (None, 'Exit'):
                                            break
                                        elif event in ('OK'):
                                            window.close()
                                            rem_c()
                    except Exception:
                        layout = [
                            [sg.Text(un + ', you wrote the wrong repo`s name. Try again')],
                            [sg.Button('OK')]
                        ]
                        window = sg.Window('ERROR!', layout)
                        while True:
                            event, values = window.read()
                            if event in (None, 'Exit'):
                                break
                            elif event in ('OK'):
                                window.close()
                                rem_c()

# CREATE BRUNCH FUNCTION
def c_branch():
    layout = [
        [sg.Text('Do you want to create branch in your repo?')],
        [sg.Button('YES'), sg.Button('NO')]
    ]
    window = sg.Window('Create branch', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in ('NO'):
            window.close()
            menu()
        elif event == 'YES':
            window.close()
            layout = [
                [sg.Text('Enter the name of repo in which you want to create branch:')],
                [sg.InputText(key='-IN-')],
                [sg.Button('OK')]
            ]
            window = sg.Window('Create branch', layout)
            while True:
                event, values = window.read()
                if event in (None, 'Exit'):
                    break
                elif event == 'OK':
                    window.close()
                    n = values['-IN-']
                    try:
                        r = u.get_repo(n)
                        window.close()
                        layout = [
                            [sg.Text('Enter the name of the new branch:')],
                            [sg.InputText(key='-IN1-')],
                            [sg.Button('OK')]
                        ]
                        window = sg.Window('Create branch', layout)
                        while True:
                            event, values = window.read()
                            if event in (None, 'Exit'):
                                break
                            elif event == 'OK':
                                window.close()
                                l = values['-IN1-']
                                try:
                                    x = r.get_branch('main')
                                    r.create_git_ref(ref='refs/heads/' + l, sha=x.commit.sha)
                                    window.close()
                                    layout = [
                                        [sg.Text('CONGRATULATIONS! You created new branch ' + l + 'in the repo ' + n)],
                                        [sg.Button('OK')]
                                    ]
                                    window = sg.Window('Create branch', layout)
                                    while True:
                                        event, values = window.read()
                                        if event in (None, 'Exit'):
                                            break
                                        elif event == 'OK':
                                            window.close()
                                            menu()
                                            break
                                except Exception:
                                    layout = [
                                        [sg.Text(
                                            un + ', you wrote the wrong branch`s name or this branch is already added. Try again')],
                                        [sg.Button('OK')]
                                    ]
                                    window = sg.Window('ERROR!', layout)
                                    while True:
                                        event, values = window.read()
                                        if event in (None, 'Exit'):
                                            break
                                        elif event in ('OK'):
                                            window.close()
                                            c_branch()
                    except Exception:
                        layout = [
                            [sg.Text(un + ', you wrote the wrong repo`s name. Try again')],
                            [sg.Button('OK')]
                        ]
                        window = sg.Window('ERROR!', layout)
                        while True:
                            event, values = window.read()
                            if event in (None, 'Exit'):
                                break
                            elif event in ('OK'):
                                window.close()
                                c_branch()

# DELETE BRUNCH FUNCTION
def d_branch():
    layout = [
        [sg.Text('Do you want to delete branch from your repo?')],
        [sg.Button('YES'), sg.Button('NO')]
    ]
    window = sg.Window('Delete branch', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in ('NO'):
            window.close()
            menu()
        elif event == 'YES':
            window.close()
            layout = [
                [sg.Text('Enter the name of repo from which you want to delete branch:')],
                [sg.InputText(key='-IN-')],
                [sg.Button('OK')]
            ]
            window = sg.Window('Delete branch', layout)
            while True:
                event, values = window.read()
                if event in (None, 'Exit'):
                    break
                elif event == 'OK':
                    window.close()
                    n = values['-IN-']
                    try:
                        r = u.get_repo(n)
                        window.close()
                        layout = [
                            [sg.Text('Enter the name of the branch:')],
                            [sg.InputText(key='-IN1-')],
                            [sg.Button('OK')]
                        ]
                        window = sg.Window('Delete branch', layout)
                        while True:
                            event, values = window.read()
                            if event in (None, 'Exit'):
                                break
                            elif event == 'OK':
                                window.close()
                                l = values['-IN1-']
                                try:
                                    x = r.get_git_ref(ref='heads/' + l)
                                    x.delete()
                                    window.close()
                                    layout = [
                                        [sg.Text('CONGRATULATIONS! You deleted the branch ' + l + 'from the repo ' + n)],
                                        [sg.Button('OK')]
                                    ]
                                    window = sg.Window('Delete branch', layout)
                                    while True:
                                        event, values = window.read()
                                        if event in (None, 'Exit'):
                                            break
                                        elif event == 'OK':
                                            window.close()
                                            menu()
                                            break
                                except Exception:
                                    layout = [
                                        [sg.Text(
                                            un + ', you wrote the wrong branch`s name or this branch. Try again')],
                                        [sg.Button('OK')]
                                    ]
                                    window = sg.Window('ERROR!', layout)
                                    while True:
                                        event, values = window.read()
                                        if event in (None, 'Exit'):
                                            break
                                        elif event in ('OK'):
                                            window.close()
                                            d_branch()
                    except Exception:
                        layout = [
                            [sg.Text(un + ', you wrote the wrong repo`s name. Try again')],
                            [sg.Button('OK')]
                        ]
                        window = sg.Window('ERROR!', layout)
                        while True:
                            event, values = window.read()
                            if event in (None, 'Exit'):
                                break
                            elif event in ('OK'):
                                window.close()
                                d_branch()

# NAME
def name():
    layout = [
        [sg.Text('Enter your name:'),
        ],
        [sg.InputText(key='-IN-')],
        [sg.Button('OK')]
    ]
    window = sg.Window('Name', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event =='OK':
            global un
            un = values['-IN-']
            window.close()
            token()
            break
    window.close()

# HI
def hi():
    layout = [
        [sg.Text('HI! It`s Diannell chat bot.\nThis chat bot could help you with actions with repos.\nClick OK to continue.')],
        [sg.Button('OK')]
    ]
    window = sg.Window('Name', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event == 'OK':
            window.close()
            name()

# TOKEN
def token():
    a=0
    layout = [
        [sg.Text(un+ ', are you have a token?'),
         ],
        [sg.Button('YES'), sg.Button('NO')]
    ]
    window = sg.Window('Token', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in ('NO'):
            window.close()
            layout = [
                [sg.Text('Please create token to continue'),
                 ]
            ]
            window = sg.Window('Token', layout)
            while True:
                event, values = window.read()
                if event in (None, 'Exit'):
                    break
            token()
        elif event == 'YES':
            window.close()
            layout = [
                [sg.Text('Enter your token:'),
                 ],
                [sg.InputText(key='-IN-')],
                [sg.Button('OK')]
            ]
            window = sg.Window('Token', layout)
            while True:
                event, values = window.read()
                if event in (None, 'Exit'):
                    break
                elif event == 'OK':
                    global tok
                    tok = values['-IN-']
                    global g
                    g = Github(tok)
                    global u
                    u = g.get_user()
                    window.close()
                    try:
                        window.close()
                        menu()
                    except Exception:
                        window.close()
                        layout = [
                            [sg.Text(un+', you wrote the wrong token. Try again')],
                            [sg.Button('OK')]
                        ]
                        window = sg.Window('ERROR!', layout)
                        while True:
                            event, values = window.read()
                            if event in (None, 'Exit'):
                                break
                            elif event in ('OK'):
                                window.close()
                                token()
                    break

# CHAT BOT MENU
def menu():
    layout = [
        [sg.Text(un+ ', what would you want to do?'),
         ],
        [sg.Button('1. Create repo'), sg.Button('2. Delete repo'), sg.Button('3. Get repo`s information')],
        [sg.Button('4. Add collaborators to repo'), sg.Button('5. Remove collaborators from repo')],
        [sg.Button('6. Create branch'), sg.Button('7. Delete branch')]
    ]
    window = sg.Window('Menu', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in ('NO'):
            break
        elif event == '1. Create repo':
            window.close()
            repo()
        elif event == '2. Delete repo':
            window.close()
            drepo()
        elif event == '3. Get repo`s information':
            window.close()
            grepo()
        elif event == '4. Add collaborators to repo':
            window.close()
            add_c()
        elif event == '5. Remove collaborators from repo':
            window.close()
            rem_c()
        elif event == '6. Create branch':
            window.close()
            c_branch()
        elif event == '7. Delete branch':
            window.close()
            d_branch()
    window.close()

hi()