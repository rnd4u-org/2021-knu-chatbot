import stanza

f = open('nlp.txt', 'tw', encoding='utf-8')
f.write('Environment: Python '+"\n"+"vlad bilenko"+"\n")

nlp = stanza.Pipeline()



sent = []
sent.append("Is our repository private?")
sent.append("How many branches has Django project?")
sent.append("How many tags has Django project?")
sent.append("Does this branch include empty files?")
sent.append("How many commits are in Django project?")
sent.append("Is this project used by thousand people?")
sent.append("What is the address of website of this project?")
sent.append("Who contributed to Django project?")
sent.append("How many pull requests are there?")
sent.append("Which folders are situated on the branch 'master'?")
sent.append("What is the file 'Read me' about?")
sent.append("When was the last uploading file on the branch 'master'?")
sent.append("Are there any comment to the last commit on the main branch?")
sent.append("How many commits were created on the default branch last week?")
sent.append("Is there a description of the project there?")
sent.append("Are there some published packages in this project?")
sent.append("When was Django project created?")
sent.append("Who was created Django project?")
sent.append("How many contributors has this project?")
sent.append("What is the full name of our project?")
sent.append("What is the identifier of our project?")
sent.append("What is the name of a default branch?")
sent.append("Is anybody from my followers contributed to this project?")
sent.append("Is it possible to sponsor this project?")
sent.append("There are some folders including a lot of subfolders, aren't there?")
sent.append("What is the link for cloning the repository?")
sent.append("How many forks are on this repository?")
sent.append("How many stars has this project?")
sent.append("How many people are watching this project?")
sent.append("When was done the last pull request?")

i = 0
for w in sent:
    i += 1
    doc = nlp(w)
    f.write(str(i) + ". QUESTION: "+'\n'+w+'\n')
    f.write("TOKENS - POS TAGS: "+'\n')
    for sentence in doc.sentences:
        for word in sentence.words:
            f.write(word.text + ' - ' + word.pos+'\n')


    f.write("DEPENDENCY TREE: "+"\n")
    for sent in doc.sentences :
        for word in sent.words:
            f.write(str(word.text)+" "+str(word.head)+" "+str(word.deprel)+"\n")


    f.write("NAMED ENTITIES: "+"\n")
    for sent in doc.sentences:
        for ent in sent.ents:
            f.write(ent.text+' ')
            f.write(ent.type+"\n")
