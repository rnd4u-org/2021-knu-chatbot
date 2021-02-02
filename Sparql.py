from SPARQLWrapper import SPARQLWrapper, JSON


sparql = SPARQLWrapper("http://localhost:7200/repositories/iliarkov")
sparql.setQuery("""PREFIX terms: <http://purl.org/dc/terms/>
SELECT ?license
WHERE {<http://resources.samsung.com/projects/.net> <http://purl.org/dc/terms/license> ?license.
}""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print("LICENSE:")
for result in results["results"]["bindings"]:
    print(result["license"]["value"])

print('')
sparql.setQuery("""PREFIX terms: <http://purl.org/dc/terms/>
SELECT ?repository
WHERE {<http://resources.samsung.com/projects/.net> <http://resources.samsung.com/git/repository> ?repository. 
}""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print("REPOSITORIES:")
for result in results["results"]["bindings"]:
    print(result["repository"]["value"])

print('')
sparql.setQuery("""PREFIX terms: <http://purl.org/dc/terms/>
SELECT ?license ?description
WHERE {<http://resources.samsung.com/projects/.net> <http://purl.org/dc/terms/license> ?license.
       <http://resources.samsung.com/projects/.net> <http://purl.org/dc/terms/description> ?description.
}""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print("LICENSE:")
for result in results["results"]["bindings"]:
    print(result["license"]["value"])
print("DESCRIPTION:")
for result in results["results"]["bindings"]:
    print(result["description"]["value"])

print('')
sparql.setQuery("""PREFIX terms: <http://purl.org/dc/terms/>
SELECT ?contributor
WHERE {<http://resources.samsung.com/repositories/boostorg/boost> <http://purl.org/dc/terms/contributor> ?contributor.
}""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print("CONTRIBUTORS:")
for result in results["results"]["bindings"]:
    print(result["contributor"]["value"])

print('')
sparql.setQuery("""PREFIX terms: <http://purl.org/dc/terms/>
SELECT ?homepage
WHERE {<http://resources.samsung.com/projects/.net> <http://resources.samsung.com/git/homepage> ?homepage.
}""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print("HOMEPAGE:")
for result in results["results"]["bindings"]:
    print(result["homepage"]["value"])

print('')
sparql.setQuery("""PREFIX terms: <http://purl.org/dc/terms/>
SELECT ?project
WHERE {<http://resources.samsung.com/contributors/1wheel> <http://purl.org/dc/terms/contributor> ?project.
}""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print("PROJECTS:")
for result in results["results"]["bindings"]:
    print(result["project"]["value"])
