from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:7200/repositories/1234")
query1 = """
    SELECT ?license
    WHERE{
    <http://resources.samsung.com/projects/abseil> <http://purl.org/dc/terms/license> ?license .
    }
"""
sparql.setQuery(query1)
print("RESULTING ANSWER TO SPARQL QUERY 1")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print(result["license"]["value"])

query2 = """
    SELECT ?repository
    WHERE{
    <http://resources.samsung.com/projects/abseil> <http://resources.samsung.com/git/repository>?repository.
    }
"""
sparql.setQuery(query2)
print("RESULTING ANSWER TO SPARQL QUERY 2")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print(result["repository"]["value"])
query3 = """
    SELECT DISTINCT ?license ?description
    WHERE{
    <http://resources.samsung.com/projects/abseil> <http://purl.org/dc/terms/license> ?license.
    <http://resources.samsung.com/projects/abseil> <http://purl.org/dc/terms/description> ?description.
}
"""
sparql.setQuery(query3)
print("RESULTING ANSWER TO SPARQL QUERY 3")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print(result["license"]["value"])
    print(result["description"]["value"])
query4 = """
    SELECT ?contributor
    WHERE{
    <http://resources.samsung.com/repositories/ceph/boost> <http://purl.org/dc/terms/contributor> ?contributor.
}
"""
sparql.setQuery(query4)
print("RESULTING ANSWER TO SPARQL QUERY 4")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print(result["contributor"]["value"])
query5 = """
    SELECT ?homepage
    WHERE{
    	<http://resources.samsung.com/projects/abseil> <http://resources.samsung.com/git/homepage> ?homepage.
}
"""
sparql.setQuery(query5)
print("RESULTING ANSWER TO SPARQL QUERY 5")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print(result["homepage"]["value"])
query6 = """
    SELECT ?project
    WHERE{
    	<http://resources.samsung.com/contributors/1wheel> <http://purl.org/dc/terms/contributor> ?project.
}
"""
sparql.setQuery(query6)
print("RESULTING ANSWER TO SPARQL QUERY 6")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print(result["project"]["value"])
