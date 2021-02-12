import stanza
from SPARQLWrapper import SPARQLWrapper, JSON

# QUESTIONS FOR NLP ChatBot:
# What license does tyaga project have?
# Which repositories does tyaga project have?
# Which license and description does tyaga project have?
# Who contributed to the boostorg/boost repository?
# Which homepage does tyaga project have?
# What projects did ivanov contributor contribute to?

nlp = stanza.Pipeline()
s = SPARQLWrapper('http://localhost:7200/repositories/3141')
qu = nlp(input('Enter your question: '))

wh = 'WHERE{' + '\n'
q = 'SELECT '
l = {'project': 'http://resources.samsung.com/projects/', 'license': 'http://purl.org/dc/terms/license',
         'repository': 'http://resources.samsung.com/git/repository',
         'description': 'http://purl.org/dc/terms/description',
         'repositories': 'http://resources.samsung.com/repositories/',
         'contributors': 'http://resources.samsung.com/contributors/',
         'contributor': 'http://purl.org/dc/terms/contributor', 'homepage': 'http://resources.samsung.com/git/homepage'}
a = {}
for i in qu.sentences:
    for w in i.words:
        print(f'({w.text}, {w.head}, {w.deprel})' + ' , ')
        if w.deprel == "obj":
            a["obj"] = w.text
        elif w.deprel == "nsubj":
            a["nsubj"] = w.text
        elif w.deprel == "conj":
            a["conj"] = w.text
        elif w.deprel == "compound":
            a["compound"] = w.text
        elif w.deprel == "obl":
            a["obl"] = w.text
        elif w.deprel == "root":
            a["root"] == w.text
if 'conj' in a:
    if a['nsubj']=='project'and a['obj']=='license'and a['conj']=='description':
        q += '?license'+'?description'
        wh += '<'+l['project']+a["compound"]+'>'+' '+'<'+l[
            'license']+'>'+' '+'?license .'+'\n'+'<'+l['project']+a["compound"]+'>'+' '+'<' +\
                 l['description']+'>'+' '+'?description .'+'\n'
        e = "license"
        e1 = "description"
        i = 1
    elif a['root']=='contributed'and a['nsubj']=='Who':
        q += '?contributor'
        wh +='<'+l['repositories']+a['compound']+'/'+a['conj']+'>'+' '+'<'+l[
            'contributor']+'>'+' '+'?contributor .' + '\n'
        e = "contributor"
        i = 0
else:
    if a['obj']=='license'and a['nsubj']=='project':
        q += '?license'
        wh += '<'+l['project']+a["compound"]+'>'+' '+'<'+l[
            'license']+'>'+' '+'?license .'+'\n'
        e = "license"
        i = 0

    elif (a['nsubj'] == 'project' and a['obj'] == 'repositories'):
        q += '?repository'
        wh +='<'+l['project']+a["compound"]+'>'+' '+'<'+l[
            'repository']+'>'+' '+'?repository .'+'\n'
        e = "repository"
        i = 0
    elif a['nsubj']=='contributor'and a['root']=='contribute':
        q += '?project'
        wh +='<'+l['contributors']+a['compound'] + '>' + ' ' + '<' + l[
            'contributor']+'>'+' '+'?project .'+'\n'
        e = "project"
        i = 0
    elif a['nsubj']=='project'and a['obj']=='homepage':
        q += '?homepage'
        wh += '<'+l['project']+a['compound']+'>'+' '+'<'+l[
            'homepage']+'>'+' '+'?homepage .'+'\n'
        e = "homepage"
        i = 0

i1 = '\n'+q+wh+'}'+'\n'
print(i1)
s.setQuery(i1)
s.setReturnFormat(JSON)
results = s.query().convert()
for result in results['results']['bindings']:
    print(result[e]['value'])
    if i == 1:
        print(result[e1]['value'])