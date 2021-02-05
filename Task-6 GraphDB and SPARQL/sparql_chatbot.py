from SPARQLWrapper import SPARQLWrapper, JSON

class SparqlQueries:
    def __init__(self):
        self.__sparql = SPARQLWrapper("http://localhost:7200/repositories/chatbot-samsung")
        self.__project = ''
        self.__repo = ''
        self.__username = ''

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, project_name):
        self.__project = project_name

    @property
    def repo(self):
        return self.__repo

    @repo.setter
    def repo(self, repo_name):
        self.__repo = repo_name

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    def query_license(self):
        self.__sparql.setQuery("""
        PREFIX purlterms: <http://purl.org/dc/terms/>
        SELECT ?license
        WHERE {{
        <http://resources.samsung.com/projects/{}> purlterms:license ?license .
        }}
        """.format(self.__project) )
        self.__sparql.setReturnFormat(JSON)
        results = self.__sparql.query().convert()
        for i in results['results']['bindings']:
            return f"1. What license does the {self.__project} project have?", i['license']['value']

    def query_repositories(self):
        self.__sparql.setQuery("""
        SELECT ?repository
        WHERE {{
        <http://resources.samsung.com/projects/{}> <http://resources.samsung.com/git/repository> ?repository .
        }}
        """.format(self.__project) )
        self.__sparql.setReturnFormat(JSON)
        results = self.__sparql.query().convert()
        for i in results['results']['bindings']:
            return f"2. Which repositories does the {self.__project} project have?", i['repository']['value']

    def query_lic_and_desc(self):
        self.__sparql.setQuery("""
        PREFIX purlterms: <http://purl.org/dc/terms/>
        SELECT ?license ?description
        WHERE {{
        <http://resources.samsung.com/projects/{}> purlterms:license ?license .
        <http://resources.samsung.com/projects/{}> purlterms:description ?description .
        }}
        """.format(self.__project, self.__project) )
        self.__sparql.setReturnFormat(JSON)
        results = self.__sparql.query().convert()
        for i in results["results"]["bindings"]:
            return f"3. Which license and description does the {self.__project} project have?", i["license"]["value"], i["description"]["value"]

    def query_contributors(self):
        self.__sparql.setQuery("""
        PREFIX purlterms: <http://purl.org/dc/terms/>
        SELECT ?contributor
        WHERE {{
        <http://resources.samsung.com/repositories/{}> purlterms:contributor ?contributor .
        }}""".format(self.__repo) )
        self.__sparql.setReturnFormat(JSON)
        results = self.__sparql.query().convert()
        for i in results["results"]["bindings"]:
            return f"4. Who contributed to the {self.__repo} repository?", i["contributor"]["value"]

    def query_homepage(self):
        self.__sparql.setQuery("""
        SELECT ?homepage
        WHERE {{
        <http://resources.samsung.com/projects/{}> <http://resources.samsung.com/git/homepage> ?homepage .
        }}""".format(self.__project))
        self.__sparql.setReturnFormat(JSON)
        results = self.__sparql.query().convert()
        for i in results["results"]["bindings"]:
            return f"5. Which homepage does the {self.__project} project have?", i["homepage"]["value"]

    def query_contribute_to(self):
        self.__sparql.setQuery("""
        PREFIX purlterms: <http://purl.org/dc/terms/>
        SELECT ?project
        WHERE {{
        <http://resources.samsung.com/contributors/{}> purlterms:contributor ?project .
        }}""".format(self.__username))
        self.__sparql.setReturnFormat(JSON)
        results = self.__sparql.query().convert()
        for i in results["results"]["bindings"]:
            return f"6. What projects did the {self.__username} contributor contribute to?", i["project"]["value"]

sq = SparqlQueries()

with open("sparql_res.txt", 'w', encoding="utf-8") as f:
    sq.project = input("Enter project name: ")
    for i in sq.query_license():
        f.write(f"{i}\n")
    for i in sq.query_repositories():
        f.write(f"{i}\n")
    for i in sq.query_lic_and_desc():
        f.write(f"{i}\n")
    sq.repo = input("Enter repo path (including parent dirs)-> http://resources.samsung.com/repositories/")
    for i in sq.query_contributors():
        f.write(f"{i}\n")
    for i in sq.query_homepage():
        f.write(f"{i}\n")
    sq.username = input("Enter contributor username: ")
    for i in sq.query_contribute_to():
        f.write(f"{i}\n")
