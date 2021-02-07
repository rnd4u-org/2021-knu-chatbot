import stanza

from SPARQLWrapper import SPARQLWrapper, JSON


nlp = stanza.Pipeline()


sparql = SPARQLWrapper("http://localhost:7200/repositories/q111")
sparql.setReturnFormat(JSON)
sent = []
sent.append("What license does the acl project have?")
sent.append("homepage does the abseil project have")



def lis(param):
    sparql.setQuery('PREFIX project: <http://resources.samsung.com/projects/> PREFIX predicate: <http://purl.org/dc/terms/> SELECT ?license WHERE  {project:' +param+' '   + 'predicate:license ?license .}')

    co = sparql.query().convert()
    print("What license does the <" +  param   +"> project have?"+"\n")
    for i in co["results"]["bindings"]:
        print(i["license"]["value"]+"\n")



def repo(param):
    sparql.setQuery("PREFIX project: <http://resources.samsung.com/projects/> SELECT ?repository WHERE{project:" + param + " " + "<http://resources.samsung.com/git/repository> ?repository .}")

    res = sparql.query().convert()

    print("Which repositories does <" +  param   +"> project have?\n")
    for i in res["results"]["bindings"]:
        print(i["repository"]["value"])
        print("\n")






def le(param):
    sparql.setQuery('PREFIX project: <http://resources.samsung.com/projects/> PREFIX predicate: <http://purl.org/dc/terms/> SELECT ?license ?description WHERE{project:tayga predicate:license ?license .project:'+ param + ' predicate:description ?description .}')
    res = sparql.query().convert()
    print("Which license and description does <" +  param   +"> project have?\n")
    print("License:\n")
    for lic in res["results"]["bindings"]:
        print(lic["license"]["value"])
    print('\n')
    print("Description:\n")
    for des in res["results"]["bindings"]:
        print(des["description"]["value"]+'\n')




def contr(param):
    sparql.setQuery("PREFIX contr: <http://purl.org/dc/terms/> SELECT ?contributor WHERE { <http://resources.samsung.com/repositories/"+ param +"> contr:contributor ?contributor .}")
    res = sparql.query().convert()
    print("Who contributed to <" +  param   +"> repository?\n")
    for cont in res["results"]["bindings"]:
        print(cont["contributor"]["value"]+'\n')



def homepage(param):
    sparql.setQuery("PREFIX project: <http://resources.samsung.com/projects/> PREFIX home:<http://resources.samsung.com/git/> SELECT ?homepage WHERE{project:" + param + " home:homepage ?homepage .}")
    res = sparql.query().convert()
    print("Which homepage does <" +  param   +"> project have?\n")
    for cont in res["results"]["bindings"]:
        print(cont["homepage"]["value"]+"\n")



def con(param):
    sparql.setQuery("PREFIX contr:<http://resources.samsung.com/contributors/> PREFIX proj:<http://purl.org/dc/terms/> SELECT ?project WHERE{contr:" + param + " proj:contributor ?project . }")
    res = sparql.query().convert()
    print("What projects did <" +  param   +"> contribute to?\n")
    for cont in res["results"]["bindings"]:
        print(cont["project"]["value"]+"\n")

#con("102")
#contr('alsa-project/tinycompress')
#repo("7zip")
#le('abseil')
#homepage('abseil')
#repo('abseil')


proj=["7zip",".net","androidplot","android open source project (aosp)","android-youtube-player","alure","almanah diary","allennlp","alicevision","akraino edge stack","aikido","afollestad","advanced linux sound architecture (alsa)","adeb","acl","accord.net","abseil","abicc","abi dumper",]
reps=["alsa-project/alsa-utils","alsa-project/hinawa-rs","alsa-project/alsa-tools","alsa-project/libhinawa-docs","alsa-project/alsa-python","alsa-project/libhinawa","alsa-project/alsa-ucm-conf","alsa-project/alsa-oss","alsa-project/alsa-topology-conf","alsa-project/alsa-tests","alsa-project/alsa-plugins","alsa-project/alsa-gobject-docs","alsa-project/alsa-lib","alsa-project/alsa-gobject-rs","alsa-project/alsa-gobject","alsa-project/alsa-gi","alsa-project/alsa-firmware","alsa-project/tinycompress","alsa-project/snd-firewire-ctl-services","alvaropg/almanah","alicevision/alicevision","pierfrancescosoffritti/android-youtube-player","protobuf.git","gl.git","glfw.git","allenai/allennlp","dotnet/runtime","abi-dumper","lvc/abi-compliance-checker","halfhp/androidplot","abseil/federation-hello","abseil/abseil-cpp","abseil/abseil-hello","abseil/abseil-py","abseil/abseilhub.io","abseil/federation-head","personalrobotics/aikido","joelagnel/adeb/","material-dialogs","accord-net/framework",]
cont=["102","1025kb","0-wiz-0","007","00tiagopolicarpo00","0101011","0b10011","0intro","0lvin","0mkara","0mp","0nko","0x0badc0de","0x0ece","0x20h","0x6e6562","0xf2","0xflotus","0xjac","100pah"]

#w1="What license and description does the adeb project have?"
#w2="Which repositories does the adeb project have?"
#w3="Which homepage does the abseil project have"
#w3="What projects did the abayer contributor contribute to?"
#w3="Who contributed to the alvaropg/almanah repository?"
#w3="What projects did the 0mkara contributor contribute to?"

w3=(input("ввудите вопрос"))


doc = nlp(w3)
for sent in doc.sentences:
    for word in sent.words:
        if word.deprel == 'conj' and word.lemma == 'description':
            lst = w3.split()
            list(set(lst) & set(proj)) != []
            lis(list(set(lst) & set(proj))[0])
            le(list(set(lst) & set(proj))[0])
        elif word.deprel == 'obj' and word.lemma == 'license':
            lst = w3.split()
            list(set(lst) & set(proj))!=[]
            lis(list(set(lst) & set(proj))[0])



        elif word.deprel == 'nsubj' and word.text == 'contributor':
            lst = w3.split()
            list(set(lst) & set(cont)) != []
            con(list(set(lst) & set(cont))[0])




        elif word.deprel == 'root' and word.lemma == 'contribute':
            lst = w3.split()
            print("1")
            list(set(lst) & set(reps)) != []
            contr(list(set(lst) & set(reps))[0])


        elif word.deprel == 'obj' and word.lemma == 'repository':
            lst = w3.split()
            list(set(lst) & set(proj)) != []
            repo(list(set(lst) & set(proj))[0])

        elif word.deprel == 'obj' and word.lemma == 'homepage':
            lst = w3.split()
            list(set(lst) & set(proj)) != []
            homepage(list(set(lst) & set(proj))[0])






