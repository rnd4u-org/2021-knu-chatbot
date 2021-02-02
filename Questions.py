import stanza


nlp = stanza.Pipeline()
L = []
L.append("Is our repository private?")
L.append("How many branches has our project?")
L.append("How many tags has this project?")
L.append("Who contributed to this project?")
L.append("How many pull requests are there?")
L.append("Which folders are situated on the branch 'master'?")
L.append("Does this branch include empty files?")
L.append("How many commits are there?")
L.append("Is this project used by thousand people?")
L.append("What is the address of website of this project?")
L.append("What is the file 'Read me' about?")
L.append("When was the last uploading file on the branch 'master'?")
L.append("There are some folders including a lot of subfolders, aren't there?")
L.append("What is the link for cloning the repository?")
L.append("How many forks are on this repository?")
L.append("How many stars has this project?")
L.append("How many people are watching this project?")
L.append("When was done the last pull request?")
L.append("Are there any comment to the last commit on the main branch?")
L.append("When was this project created?")
L.append("Who was created it?")
L.append("How many contributors has this project?")
L.append("What is the full name of our project?")
L.append("What is the identifier of our project?")
L.append("What is the name of a default branch?")
L.append("How many commits were created on the default branch last week?")
L.append("Is there a description of the project there?")
L.append("Are there some published packages in this project?")
L.append("Is anybody from my followers contributed to this project?")
L.append("Is it possible to sponsor this project?")
q = 0
for el in L:
    q += 1
    doc = nlp(el)
    print('')
    print(str(q) + ". QUESTION: ")
    print(el)
    print('')
    print("TOKENS: ")
    for sentence in doc.sentences:
        for word in sentence.words:
            print(word.text)
    print('')
    print("POS TAGS: ")
    for sentence in doc.sentences:
        for word in sentence.words:
            print(word.text + ': ' + word.pos)
    print('')
    print("DEPENDENCY TREE: ")
    doc.sentences[0].print_dependencies()
    print('')
    print("NAMED ENTITIES: ")
    for sent in doc.sentences:
        for ent in sent.ents:
            print(ent.text, ent.type)
