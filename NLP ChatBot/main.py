from SPARQLWrapper import SPARQLWrapper, JSON
import stanza


nlp = stanza.Pipeline()

'''
q1 = "What license does androidplot have?"
q2 = "Which repositories does androidplot have?"
q3 = "Which license and description does tayga have?"
q4 = "Who contributed to jupyter/governance?"
q5 = "Which homepage does tayga have?"
q6 = "What projects did jackdanger contribute to?"
'''

query = input("Enter your question: ")
doc = nlp(query)

for sent in doc.sentences:
    for word in sent.words:
        if word.deprel == 'obj' or word.deprel == 'conj':
            object_triple = word.text

        if word.deprel == 'obj':
            object_triple1 = word.text
            predicate_triple1 = word.text
        if word.deprel == 'conj':
            object_triple2 = word.text
            predicate_triple2 = word.text


        if (word.deprel == 'obj' or word.deprel == 'conj') and (word.text != 'contribute'):
            predicate_triple = word.text


        if word.deprel == 'nsubj':
            subject_triple = word.text

        if word.text == 'Who':
            if word.deprel == 'obl':
                pred = "repositories/"+word.text+"/"
            else:
                pred = "repositories/" + sent.words[3].text + sent.words[4].text
            predicate_triple_l = "contributor"
            object_triple_l = "contributor"
            subject_triple = sent.words[5].text

        elif word.text == 'description':
            pred = "projects/"


        elif word.text == 'projects':
            pred = "contributors/"
            d = nlp(object_triple)
            for sent in d.sentences:
                for word in sent.words:
                    object_triple_l = word.lemma
            predicate_triple_l = "contributor"

        elif (word.text == 'license' or word.text == 'repositories' or word.text == 'homepage'):
            pred = "projects/"
            d = nlp(object_triple)
            for sent in d.sentences:
                for word in sent.words:
                    object_triple_l = word.lemma
                    predicate_triple_l = word.lemma


l = query.split(' ')
if 'homepage' in l:
    SPARQLSkeleton = """
    PREFIX subject: <http://resources.samsung.com/%s>
    PREFIX predicate: <http://resources.samsung.com/git/>
    SELECT ?%s
    WHERE{
    subject:%s predicate:%s ?%s .
    }
    """ % (pred, object_triple_l, subject_triple, predicate_triple, object_triple_l)

elif 'repositories' in l:
    SPARQLSkeleton = """
    PREFIX subject: <http://resources.samsung.com/%s>
    PREFIX predicate: <http://resources.samsung.com/git/>
    SELECT ?%s
    WHERE{
    subject:%s predicate:%s ?%s .
    }
    """ % (pred, object_triple_l, subject_triple, predicate_triple_l, object_triple_l)

elif 'description' in l:
    SPARQLSkeleton = """
    PREFIX subject: <http://resources.samsung.com/%s>
    PREFIX predicate: <http://purl.org/dc/terms/>
    SELECT ?%s ?%s
    WHERE{
    subject:%s predicate:%s ?%s .
    subject:%s predicate:%s ?%s .
    }
    """ % (pred, object_triple1, object_triple2, subject_triple, predicate_triple1, object_triple1, subject_triple, predicate_triple2, object_triple2)

else:
    SPARQLSkeleton = """
    PREFIX subject:<http://resources.samsung.com/%s>
    PREFIX predicate:<http://purl.org/dc/terms/>
    SELECT ?%s
    WHERE{
    subject:%s predicate:%s ?%s .
    }
    """ % (pred, object_triple_l, subject_triple, predicate_triple_l, object_triple_l)


sparql = SPARQLWrapper("http://localhost:7200/repositories/228")
sparql.setReturnFormat(JSON)
sparql.setQuery(SPARQLSkeleton)
res = sparql.query().convert()
if 'description' in l:
    for i in res["results"]["bindings"]:
        print(i[object_triple1]["value"])
    for i in res["results"]["bindings"]:
        print(i[object_triple2]["value"])
else:
    for i in res["results"]["bindings"]:
        print(i[object_triple_l]["value"])
