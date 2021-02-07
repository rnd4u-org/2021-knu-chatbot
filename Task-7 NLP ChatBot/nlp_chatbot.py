import stanza
from SPARQLWrapper import SPARQLWrapper, JSON

# - What license does the <any> project have?
# - Which repositories does the <any> project have?
# - Which license and description does the <any> project have?
# - Who contributed to the <any> repository?
# - Which homepage does the <any> project have?
# - What projects did the <any> contributor contribute to?
# [Added]
# - How many stars does the <any> repository have?
# - Which title does the <any> project have?
# - Which avatar does the <any> project have?
# - How many subscribers does the <any> repository have?

class NlpChatBot:
    def __init__(self):
        self.__nlp = stanza.Pipeline(lang='en')
        self.__sparql = SPARQLWrapper("http://localhost:7200/repositories/chatbot-samsung")
        self.__question = ''
        self.__links = [
            "http://resources.samsung.com/projects/",
            "http://purl.org/dc/terms/license",
            "http://resources.samsung.com/git/repository",
            "http://purl.org/dc/terms/description",
            "http://resources.samsung.com/repositories/",
            "http://purl.org/dc/terms/contributor",
            "http://resources.samsung.com/git/homepage",
            "http://resources.samsung.com/contributors/",
            "http://resources.samsung.com/git/stars",
            "http://purl.org/dc/terms/title",
            "http://resources.samsung.com/git/avatar",
            "http://resources.samsung.com/git/subscribers"
        ]

    @property
    def query_question(self):
        return self.__question

    @query_question.setter
    def query_question(self, question):
        self.__question = question

    def start_nlp(self):
        self.__doc = self.__nlp(self.__question)

    def display_question_info(self):
        self.list_of_deprels = {}
        for i in self.__doc.sentences:
            for j in i.words:
                self.list_of_deprels[j.deprel] = j.text
        return self.list_of_deprels

    def choose_query_form(self):
        self.l = []
        if self.list_of_deprels['nsubj'] == 'project' and self.list_of_deprels['obj'] == 'license':
            self.selection = "?license"
            self.l.append(self.selection)
            self.query_body = f"<{self.__links[0]}{self.list_of_deprels['compound']}> <{self.__links[1]}> {self.selection} ."
            return self.selection, self.query_body, len(self.l)
        elif self.list_of_deprels['nsubj'] == 'project' and self.list_of_deprels['obj'] == 'repositories':
            self.selection = "?repository"
            self.l.append(self.selection)
            self.query_body = f"<{self.__links[0]}{self.list_of_deprels['compound']}> <{self.__links[2]}> {self.selection} ."
            return self.selection, self.query_body, len(self.l)
        elif self.list_of_deprels['nsubj'] == 'project' and self.list_of_deprels['obj'] == 'license' and self.list_of_deprels['conj'] == 'description':
            self.selection = "?license ?description"
            self.l.append(self.selection.split()[0])
            self.l.append(self.selection.split()[1])
            self.query_body = f"<{self.__links[0]}{self.list_of_deprels['compound']}> <{self.__links[1]}> {self.selection.split()[0]} .\n<{self.__links[0]}{self.list_of_deprels['compound']}> <{self.__links[3]}> {self.selection.split()[1]} ."
            return self.selection, self.query_body, len(self.l)
        elif self.list_of_deprels['root'] == "contributed" and self.list_of_deprels['nsubj'] == "Who":
            self.selection = "?contributor"
            self.l.append(self.selection)
            self.query_body = f"<{self.__links[4]}{self.list_of_deprels['compound']}/{self.list_of_deprels['conj']}> <{self.__links[5]}> {self.selection} ."
            return self.selection, self.query_body, len(self.l)
        elif self.list_of_deprels['nsubj'] == 'project' and self.list_of_deprels['obj'] == 'homepage':
            self.selection = "?homepage"
            self.l.append(self.selection)
            self.query_body = f"<{self.__links[0]}{self.list_of_deprels['compound']}> <{self.__links[6]}> {self.selection} ."
            return self.selection, self.query_body, len(self.l)
        elif self.list_of_deprels['nsubj'] == 'contributor' and self.list_of_deprels['root'] == 'contribute':
            self.selection = "?project"
            self.l.append(self.selection)
            self.query_body = f"<{self.__links[7]}{self.list_of_deprels['compound']}> <{self.__links[5]}> {self.selection} ."
            return self.selection, self.query_body, len(self.l)
        elif self.list_of_deprels['nsubj'] == 'repository' and self.list_of_deprels['obj'] == 'stars':
            self.selection = "?star"
            self.l.append(self.selection)
            self.query_body = f"<{self.__links[4]}{self.list_of_deprels['compound']}/{self.list_of_deprels['conj']}> <{self.__links[8]}> {self.selection} ."
            return self.selection, self.query_body, len(self.l)
        elif self.list_of_deprels['nsubj'] == 'project' and self.list_of_deprels['obj'] == 'title':
            self.selection = "?title"
            self.l.append(self.selection)
            self.query_body = f"<{self.__links[0]}{self.list_of_deprels['compound']}> <{self.__links[9]}> {self.selection} ."
            return self.selection, self.query_body, len(self.l)
        elif self.list_of_deprels['nsubj'] == 'project' and self.list_of_deprels['obj'] == 'avatar':
            self.selection = "?avatar"
            self.l.append(self.selection)
            self.query_body = f"<{self.__links[0]}{self.list_of_deprels['compound']}> <{self.__links[10]}> {self.selection} ."
            return self.selection, self.query_body, len(self.l)
        elif self.list_of_deprels['nsubj'] == 'repository' and self.list_of_deprels['obj'] == 'subscribers':
            self.selection = "?subscriber"
            self.l.append(self.selection)
            self.query_body = f"<{self.__links[4]}{self.list_of_deprels['compound']}/{self.list_of_deprels['conj']}> <{self.__links[11]}> {self.selection} ."
            return self.selection, self.query_body, len(self.l)
        else:
            return "WTf is this query? :/"

    def build_query(self):
        self.__sparql.setQuery(f"""
        SELECT {self.choose_query_form()[0]}
        WHERE {{
        {self.choose_query_form()[1]}
        }}""")
        self.__sparql.setReturnFormat(JSON)
        results = self.__sparql.query().convert()
        for i in results['results']['bindings']:
            if self.choose_query_form()[2] == 1:
                return i[f'{self.selection[1:]}']['value']
        else:
            return i[f'{self.selection[1:8]}']["value"], i[f'{self.selection[-11:]}']["value"]

if __name__ == "__main__":
    ncb = NlpChatBot()
    ncb.query_question = input("Enter your question: ")
    ncb.start_nlp()
    print(ncb.display_question_info())
    print(ncb.build_query())
