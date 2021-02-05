import stanza
from SPARQLWrapper import SPARQLWrapper, JSON


nlp = stanza.Pipeline()
senten = input()
Q = senten[:-1].split(' ')
der1 = {}
for n in range(len(Q[1:])):
    if Q[1:][n].isalpha():
        if not Q[1:][n].islower():
            der1['ilia'] = Q[1:][n]
            Q.pop(n + 1)
            Q[n + 1:n + 1] = ['ilia']
    else:
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
       ('contributed', 'repository'): ['http://purl.org/dc/terms/contributor', 'http://resources.samsung.com/repositories/']}
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
if Q[0] != "Who":
    for el in L:
        if '"deprel":"obj"' in el or '"deprel":"conj"' in el:
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
    for word in query:
        select += ' ?'
        select += word
    data += select
    data += '\n'
    for n in range(len(query)):
        if n == 0:
            data += 'WHERE {'
        else:
            data += '       '
        for el in L:
            if '"deprel":"nsubj"' in el:
                S = el.split(',\n')
                for p in S:
                    if '"text":' in p:
                        p = p.replace('"text":', '')
                        p = p[1:-1]
                        q = 0
                        if (query[n], p) in der.keys():
                            q += 1
                        if q != 0:
                            rep = '<' + der[(query[n], p)][0] + '> '
                            data1 = '<' + der[(query[n], p)][1] + der1['ilia'] + '> '
                            data += data1
                            data += rep
        write = '?' + query[n] + '.' + '\n'
        data += write
    data += '}\n'
else:
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
    for word in query:
        select += ' ?'
        select += word
    data += select
    data += '\n'
    for n in range(len(query)):
        if n == 0:
            data += 'WHERE {'
        else:
            data += '       '
        for el in L:
            if '"deprel":"obl"' in el:
                S = el.split(',\n')
                for p in S:
                    if '"text":' in p:
                        p = p.replace('"text":', '')
                        p = p[1:-1]
                        q = 0
                        if (query[n], p) in der.keys():
                            q += 1
                        if q != 0:
                            rep = '<' + der[(query[n], p)][0] + '> '
                            data1 = '<' + der[(query[n], p)][1] + der1['ilia'] + '> '
                            data += data1
                            data += rep
        write = '?' + query[n] + '.' + '\n'
        data += write
    data += '}'
for el in query:
    sparql = SPARQLWrapper("http://localhost:7200/repositories/iliarkov")
    sparql.setQuery(data)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print(result[el]["value"])
