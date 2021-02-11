from SPARQLWrapper import SPARQLWrapper, JSON

s= SPARQLWrapper('http://localhost:7200/repositories/3141')
s.setReturnFormat(JSON)
f = open('results.txt','w')

# QUESTION 1.
s.setQuery("""
PREFIX project: <http://resources.samsung.com/projects/>
PREFIX predicate: <http://purl.org/dc/terms/>
SELECT ?license
WHERE{
project:tayga predicate:license ?license .
}
""")
r = s.query().convert()
f.write('QUESTION 1. What license does tayga project have?\n')
for i in r['results']['bindings']:
    f.write('\tAnswer:  '+str(i['license']['value'])+'\n\n')

# QUESTON 2.
s.setQuery("""
PREFIX project: <http://resources.samsung.com/projects/>
SELECT ?repository
WHERE{
project:tayga <http://resources.samsung.com/git/repository> ?repository .
}
""")
r = s.query().convert()
f.write('QUESTION 2. Which repositories does tayga project have?\n')
for i in r['results']['bindings']:
    f.write('\tAnswer:  '+str(i['repository']['value'])+'\n\n')

# QUESTION 3.
s.setQuery("""
PREFIX project: <http://resources.samsung.com/projects/>
PREFIX predicate: <http://purl.org/dc/terms/>
SELECT ?license ?description
WHERE{
project:tayga predicate:license ?license .
project:tayga predicate:description ?description .
}
""")
r = s.query().convert()
f.write('QUESTION 3. Which license and description does tayga project have?\n')
for i in r['results']['bindings']:
    f.write('\tLicense:  '+str(i['license']['value'])+'\n')
for k in r['results']['bindings']:
    f.write('\tDescription:  '+str(k['description']['value'])+'\n\n')

# QUESTION 4.
s.setQuery("""
PREFIX contr: <http://purl.org/dc/terms/>
SELECT ?contributor
WHERE{
<http://resources.samsung.com/repositories/boostorg/boost> contr:contributor ?contributor .
}
""")
r = s.query().convert()
f.write('QUESTION 4. Who contributed to boostorg/boost repository?\n')
a = 0
for i in r['results']['bindings']:
    a += 1
    f.write('\t'+str(a) +'.  '+ str(i['contributor']['value'])+'\n')
f.write('\n')

# QUESTION 5.
s.setQuery("""
PREFIX project: <http://resources.samsung.com/projects/>
PREFIX home:<http://resources.samsung.com/git/>
SELECT ?homepage
WHERE{
project:tayga home:homepage ?homepage .
}
""")
r = s.query().convert()
f.write('QUESTION 5. Which homepage does tayga project have?\n')
for i in r['results']['bindings']:
    f.write('\tAnswer:  '+str(i['homepage']['value'])+'\n\n')

# QUESTION 6.
s.setQuery("""
PREFIX contr:<http://resources.samsung.com/contributors/>
PREFIX proj:<http://purl.org/dc/terms/>
SELECT ?project
WHERE{
contr:ivanov proj:contributor ?project .
}
""")
r = s.query().convert()
f.write('QUESTION 6. What projects did ivanov contribute to?')
for i in r['results']['bindings']:
    f.write('\n\t'+str(i['project']['value']))
f.close()
