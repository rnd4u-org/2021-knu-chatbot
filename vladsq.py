from SPARQLWrapper import SPARQLWrapper, JSON

f = open('sqq.txt', 'tw', encoding='utf-8')
f.write('Environment: Python '+"\n"+"vlad bilenko"+"\n")
sparql = SPARQLWrapper("http://localhost:7200/repositories/q111")
sparql.setReturnFormat(JSON)

def lis(param):
    sparql.setQuery('PREFIX project: <http://resources.samsung.com/projects/> PREFIX predicate: <http://purl.org/dc/terms/> SELECT ?license WHERE  {project:' +param+' '   + 'predicate:license ?license .}')

    co = sparql.query().convert()
    f.write("What license does the <" +  param   +"> project have?"+"\n")
    for i in co["results"]["bindings"]:
        f.write(i["license"]["value"]+"\n")



lis('abseil')






def repo(param):
    sparql.setQuery("PREFIX project: <http://resources.samsung.com/projects/> SELECT ?repository WHERE{project:" + param + " " + "<http://resources.samsung.com/git/repository> ?repository .}")

    res = sparql.query().convert()

    f.write("Which repositories does <" +  param   +"> project have?\n")
    for i in res["results"]["bindings"]:
        f.write(i["repository"]["value"])
        f.write("\n")




repo('abseil')


def le(param):
    sparql.setQuery('PREFIX project: <http://resources.samsung.com/projects/> PREFIX predicate: <http://purl.org/dc/terms/> SELECT ?license ?description WHERE{project:tayga predicate:license ?license .project:'+ param + ' predicate:description ?description .}')
    res = sparql.query().convert()
    f.write("Which license and description does <" +  param   +"> project have?\n")
    f.write("License:\n")
    for lic in res["results"]["bindings"]:
        f.write(lic["license"]["value"])
    f.write('\n')
    f.write("Description:\n")
    for des in res["results"]["bindings"]:
        f.write(des["description"]["value"]+'\n')

le('adeb')


def contr(param):
    sparql.setQuery("PREFIX contr: <http://purl.org/dc/terms/> SELECT ?contributor WHERE { <http://resources.samsung.com/repositories/"+ param +"> contr:contributor ?contributor .}")
    res = sparql.query().convert()
    f.write("Who contributed to <" +  param   +"> repository?\n")
    for cont in res["results"]["bindings"]:
        f.write(cont["contributor"]["value"]+'\n')


contr('alsa-project/tinycompress')


def homepage(param):
    sparql.setQuery("PREFIX project: <http://resources.samsung.com/projects/> PREFIX home:<http://resources.samsung.com/git/> SELECT ?homepage WHERE{project:" + param + " home:homepage ?homepage .}")
    res = sparql.query().convert()
    f.write("Which homepage does <" +  param   +"> project have?\n")
    for cont in res["results"]["bindings"]:
        f.write(cont["homepage"]["value"]+"\n")

homepage('abseil')

def con(param):
    sparql.setQuery("PREFIX contr:<http://resources.samsung.com/contributors/> PREFIX proj:<http://purl.org/dc/terms/> SELECT ?project WHERE{contr:" + param + " proj:contributor ?project . }")
    res = sparql.query().convert()
    f.write("What projects did <" +  param   +"> contribute to?\n")
    for cont in res["results"]["bindings"]:
        f.write(cont["project"]["value"]+"\n")

con("takaswie")