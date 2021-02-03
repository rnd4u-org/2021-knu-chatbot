from SPARQLWrapper import SPARQLWrapper, JSON


sparql = SPARQLWrapper("http://localhost:7200/repositories/228")
sparql.setReturnFormat(JSON)
f = open('results.txt','w')

def licen():
    sparql.setQuery("""
    PREFIX project: <http://resources.samsung.com/projects/>
    PREFIX predicate: <http://purl.org/dc/terms/>
    SELECT ?license
    WHERE{
    project:7zip predicate:license ?license .
    }
    """)

    res = sparql.query().convert()
    f.write("1.What license does 7zip project have?\n")
    for lic in res["results"]["bindings"]:
        f.write('\t')
        f.write(lic["license"]["value"])
        f.write('\n')


def repo():
    sparql.setQuery("""
    PREFIX project: <http://resources.samsung.com/projects/>
    SELECT ?repository
    WHERE{
    project:androidplot <http://resources.samsung.com/git/repository> ?repository .
    }
    """)
    res = sparql.query().convert()
    f.write("2.Which repositories does androidplot project have?\n")
    for r in res["results"]["bindings"]:
        f.write('\t')
        f.write(r["repository"]["value"])
        f.write('\n')


def lec_and_desc():
    sparql.setQuery("""
    PREFIX project: <http://resources.samsung.com/projects/>
    PREFIX predicate: <http://purl.org/dc/terms/>
    SELECT ?license ?description
    WHERE{
    project:tayga predicate:license ?license .
    project:tayga predicate:description ?description .
    }
    """)
    res = sparql.query().convert()
    f.write("3.Which license and description does tayga project have?\n")
    f.write("\tLicense:\n")
    for lic in res["results"]["bindings"]:
        f.write('\t\t')
        f.write(lic["license"]["value"])
        f.write('\n')
    f.write('\n')
    f.write("\tDescription:\n")
    for des in res["results"]["bindings"]:
        f.write('\t\t')
        f.write(des["description"]["value"])
        f.write('\n')


def contributors():
    sparql.setQuery("""
    PREFIX contr: <http://purl.org/dc/terms/>
    SELECT ?contributor
    WHERE{
    <http://resources.samsung.com/repositories/jupyter/governance> contr:contributor ?contributor .
    }
    """)
    res = sparql.query().convert()
    f.write("4.Who contributed to jupyter/governance repository?\n")
    for cont in res["results"]["bindings"]:
        f.write('\t')
        f.write(cont["contributor"]["value"])
        f.write('\n')


def homepage():
    sparql.setQuery("""
    PREFIX project: <http://resources.samsung.com/projects/>
    PREFIX home:<http://resources.samsung.com/git/>
    SELECT ?homepage
    WHERE{
    project:7zip home:homepage ?homepage .
    }
    """)
    res = sparql.query().convert()
    f.write("5.Which homepage does 7zip project have?\n")
    for cont in res["results"]["bindings"]:
        f.write('\t')
        f.write(cont["homepage"]["value"])
        f.write('\n')


def contributor_action():
    sparql.setQuery("""
    PREFIX contr:<http://resources.samsung.com/contributors/>
    PREFIX proj:<http://purl.org/dc/terms/>
    SELECT ?project
    WHERE{
    contr:jackdanger proj:contributor ?project .
    }
    """)
    res = sparql.query().convert()
    f.write("6.What projects did jackdanger contribute to?\n")
    for cont in res["results"]["bindings"]:
        f.write('\t')
        f.write(cont["project"]["value"])
        f.write('\n')

licen()
f.write('\n')
repo()
f.write('\n')
lec_and_desc()
f.write('\n')
contributors()
f.write('\n')
homepage()
f.write('\n')
contributor_action()
f.write('\n')
f.close()