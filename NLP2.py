import stanza
from SPARQLWrapper import SPARQLWrapper, JSON


nlp = stanza.Pipeline()
senten = input()
Q = senten[:-1].split(' ')
der1 = {}
G = []
qc = 0
for n in range(len(Q[1:])):
    if Q[1:][n].isalpha():
        if not Q[1:][n].islower():
            qc += 1
            der1['ilia'] = Q[1:][n]
            Q.pop(n + 1)
            Q[n + 1:n + 1] = ['ilia']
    else:
        qc += 1
        der1['ilia'] = Q[1:][n]
        Q.pop(n + 1)
        Q[n + 1:n + 1] = ['ilia']
sent = ' '.join(Q)
data = 'PREFIX terms: <http://purl.org/dc/terms/>\n'
der = {('license', 'project'): ['http://purl.org/dc/terms/license', 'http://resources.samsung.com/projects/'],
       ('repositories', 'project'): ['http://resources.samsung.com/git/repository', 'http://resources.samsung.com/projects/'],
       ('description', 'project'): ['http://purl.org/dc/terms/description', 'http://resources.samsung.com/projects/'],
       ('homepage', 'project'): ['http://resources.samsung.com/git/homepage', 'http://resources.samsung.com/projects/'],
       ('projects', 'contributor'): ['http://purl.org/dc/terms/contributor', 'http://resources.samsung.com/contributors/'],
       ('contributed', 'repository'): ['http://purl.org/dc/terms/contributor', 'http://resources.samsung.com/repositories/'],
       ('title', 'project'): ['http://purl.org/dc/terms/title', 'http://resources.samsung.com/projects/'],
       ('avatar', 'project'): ['http://resources.samsung.com/git/avatar', 'http://resources.samsung.com/projects/'],
       ('identifier', 'repository'): ['http://purl.org/dc/terms/identifier', 'http://resources.samsung.com/repositories/'],
       ('subscribers', 'repository'): ['http://resources.samsung.com/git/subscribers', 'http://resources.samsung.com/repositories/'],
       ('stars', 'repository'): ['http://resources.samsung.com/git/stars', 'http://resources.samsung.com/repositories/'],
       ('time', 'repository'): ['http://purl.org/dc/terms/created', 'http://resources.samsung.com/repositories/'],
       ('languages', 'repository'): ['http://purl.org/dc/terms/language', 'http://resources.samsung.com/repositories/'],
       ('groups', 'contributor'): ['http://resources.samsung.com/git/contributorGroup', 'http://resources.samsung.com/contributors/']}
doc = nlp(sent)
s = str(doc.sentences)
l = s.splitlines()
l = l[1:-1]
a = ''
for s in l:
    if s != ' ':
        while True:
            if s[0] == ' ':
                s = s.replace(' ', '')
            else:
                break
    s += '\n'
    a += s
L = a.split('},\n{')
L[0] = L[0][1:]
L[-1] = L[-1][:-2]
for n in range(len(L)):
    L[n] = L[n][1:]
    L[n] = L[n][:-1]
M = []
print(L)
if Q[0] != "Who":
    kc = ''
    for c in L:
        if '"deprel":"compound"' in c or '"deprel":"amod"' in c or '"deprel":"nmod"' in c or '"deprel":"conj"' in c:
            S = c.split(',\n')
            for kce in S:
                if '"text":' in kce:
                    kc = kce.replace('"text":', '')
                    kc = kc[1:-1]
    for el in L:
        if '"deprel":"obj"' in el or '"deprel":"conj"' in el or '"deprel":"nmod"' in el or '"deprel":"nsubj"' in el or '"deprel":"root"' in el:
            M.append(el)
    query = []
    for it in M:
        S = it.split(',\n')
        for p in S:
            if '"text":' in p:
                p = p.replace('"text":', '')
                p = p[1:-1]
                query.append(p)
    select = 'SELECT'
    rewrite = 'WHERE {'
    write = ''
    for n in range(len(query)):
        for el in L:
            if '"deprel":"obl"' in el or '"deprel":"nsubj"' in el or '"deprel":"conj"' in el or '"deprel":"root"' in el:
                S = el.split(',\n')
                for p in S:
                    if '"text":' in p:
                        p = p.replace('"text":', '')
                        p = p[1:-1]
                        if (query[n], p) in der.keys():
                            select += ' ?'
                            select += query[n]
                            write += '       '
                            rep = '<' + der[(query[n], p)][0] + '> '
                            if qc != 0:
                                data1 = '<' + der[(query[n], p)][1] + der1['ilia'] + '> '
                            else:
                                data1 = '<' + der[(query[n], p)][1] + kc + '> '
                            write += data1
                            write += rep
                            write += '?' + query[n] + '.' + '\n'
                            G.append(query[n])
    data += select
    data += '\n'
    data += rewrite
    write = write[7:]
    data += write
    data += '}\n'
else:
    kc = ''
    for c in L:
        if '"deprel":"compound"' in c or '"deprel":"amod"' in c:
            S = c.split(',\n')
            for kce in S:
                if '"text":' in kce:
                    kc = kce.replace('"text":', '')
                    kc = kc[1:-1]
    for el in L:
        if '"deprel":"root"' in el:
            M.append(el)
    query = []
    for it in M:
        S = it.split(',\n')
        for p in S:
            if '"text":' in p:
                p = p.replace('"text":', '')
                p = p[1:-1]
                query.append(p)
    select = 'SELECT'
    rewrite = 'WHERE {'
    write = ''
    for n in range(len(query)):
        for el in L:
            if '"deprel":"obl"' in el or '"deprel":"nsubj"' in el or '"deprel":"conj"' in el:
                S = el.split(',\n')
                for p in S:
                    if '"text":' in p:
                        p = p.replace('"text":', '')
                        p = p[1:-1]
                        if (query[n], p) in der.keys():
                            select += ' ?'
                            select += query[n]
                            write += '       '
                            rep = '<' + der[(query[n], p)][0] + '> '
                            if qc != 0:
                                data1 = '<' + der[(query[n], p)][1] + der1['ilia'] + '> '
                            else:
                                data1 = '<' + der[(query[n], p)][1] + kc + '> '
                            write += data1
                            write += rep
                            write += '?' + query[n] + '.' + '\n'
                            G.append(query[n])
    data += select
    data += '\n'
    data += rewrite
    write = write[7:]
    data += write
    data += '}\n'
print(data)
for el in G:
    sparql = SPARQLWrapper("http://localhost:7200/repositories/iliarkov")
    sparql.setQuery(data)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print(result[el]["value"])
