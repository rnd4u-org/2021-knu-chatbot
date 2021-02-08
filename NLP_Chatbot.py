import stanza
from SPARQLWrapper import SPARQLWrapper, JSON

nlp = stanza.Pipeline()
sparql = SPARQLWrapper("http://localhost:7200/repositories/1234")

q = nlp(input("Input question: ")) #question 1 What license does the abseil project have?
#question 2 Which repositories does the abseil project have?
#question 3 Which license and description does the abseil project have?
#question 4 Who contributed to the ceph/boost repository?
#question 5 homepage does the abseil project have?
#question 6 What projects did the abayer contributor contribute to?

m = {}

for j in q.sentences:
    for word in j.words:
        print(f'({word.text}, {word.head}, {word.deprel})' + ' , ')
        if word.deprel == "obj":
            m["obj"] = word.text
        if word.deprel == "root":
            m["root"] = word.text
        if word.deprel == "nsubj":
            m["nsubj"] = word.text
        if word.deprel == "compound":
            m["compound"] = word.text
        if word.deprel == "conj":
            m["conj"] = word.text
        if word.deprel == "obl":
            m["obl"] = word.text
        if word.deprel == "root":
            m["root"] == word.text

where = "WHERE{" + "\n"
query = "SELECT" + " "
links = {'project' : 'http://resources.samsung.com/projects/' , 'license' : 'http://purl.org/dc/terms/license' ,'repository' : 'http://resources.samsung.com/git/repository' , 'description' : 'http://purl.org/dc/terms/description' ,'repositories' : 'http://resources.samsung.com/repositories/' , 'contributors' : 'http://resources.samsung.com/contributors/' , 'contributor' : 'http://purl.org/dc/terms/contributor' ,'homepage' : 'http://resources.samsung.com/git/homepage'}

if 'conj' in m:
    if m['nsubj'] == 'project' and m['obj'] == 'license' and m['conj'] == 'description' :
        query += '?license' + '?description'
        where += '<' + links['project'] + m["compound"] + '>' + ' ' + '<' + links['license'] + '>' + ' ' + '?license .' + '\n' + '<' + links['project'] + m["compound"] + '>' + ' ' + '<' + links['description'] + '>' + ' ' + '?description .' + '\n'
        var = "license"
        var1= "description"
        p=1
    if m['root'] == "contributed" and m['nsubj'] == "Who":
        query += '?contributor'
        where += '<' + links['repositories'] + m['compound'] +'/' + m['conj'] + '>' + ' ' + '<' + links['contributor'] + '>' + ' ' + '?contributor .' + '\n' 
        var = "contributor"
        p=0
else:
    if m['nsubj'] == 'project' and m['obj'] == 'license' :
        query += '?license'
        where += '<' + links['project'] + m["compound"] + '>' + ' ' + '<' + links['license'] + '>' + ' ' + '?license .' + '\n'
        var = "license"
        p=0

    if (m['nsubj'] == 'project' and m['obj'] == 'repositories') :
        query += '?repository'
        where += '<' + links['project'] + m["compound"] + '>' + ' ' + '<' + links['repository'] + '>' + ' ' + '?repository .' + '\n'
        var = "repository"
        p=0
    
    if m['nsubj'] == 'contributor' and m['root'] == 'contribute' :
        query += '?project'
        where += '<' + links['contributors'] + m['compound'] + '>' + ' ' + '<' + links['contributor'] + '>' + ' ' + '?project .' + '\n' 
        var = "project"
        p=0
    if  m['nsubj'] == 'project' and m['obj'] == 'homepage' :
        query += '?homepage'
        where += '<' + links['project'] + m['compound'] + '>' + ' ' + '<' + links['homepage'] + '>' + ' ' + '?homepage .' + '\n' 
        var = "homepage"
        p=0
        
k = "\n" + query + "\n" + where + '}' + "\n"
print(k)
sparql.setQuery(k)
print("RESULTING ANSWER TO SPARQL QUERY")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print(result[var]["value"])
    if p == 1:
        print(result[var1]["value"])
