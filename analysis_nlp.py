import stanza
nlp = stanza.Pipeline()

q = []

q.append("When was created the javaScript30 project ?")
q.append("Who is the owner of the html project ?")
q.append("What is the full name of the python project ?")
q.append("How many forks have the javaScript30 project ?")
q.append("How many contributors have the html project ?")
q.append("When was the last update of the python project ?")
q.append("How many commits have the python project ?")
q.append("What is the url of the python project ?")
q.append("Does the python project have a commit named Optimise solution ?")
q.append("Does the html project have a file named styles.css ?")
q.append("What is the id of the html project ?")
q.append("Who pulled the last request in the html project ?")
q.append("How many branches have the javaScript30 project ?")
q.append("Which branch has 10 commits in the python project ?")
q.append("How many stargathers have the javaScript30 project ?")
q.append("How many watchers have the html project ?")
q.append("Is the html project expired?")
q.append("What is the name of default branch in the python project ?")
q.append("How many text files are in the html project ?")
q.append("Which branch has file named .travis.yml in python project ?")
q.append("Is the html project private ?")
q.append("Who contributed to the python project ?")
q.append("What size is the javaScript30 project?")
q.append("What is the url of avatar of creator of the python project ?")
  
fname = input('Файл: ')
f = open(fname,'w')

for i in q:
    f.write("\n" + "QUESTION" + "\n" + i + "\n")
    k = nlp(i)
    for j in k.sentences:
        f.write('TOKENS' + '\n')
        for token in j.tokens:
            f.write(f'{token.text}' + ' , ')
        f.write('\n' + "POS TAGS" + "\n")
        for word in j.words:
            f.write(f'{word.text}: {word.upos}' + ' , ')
        f.write('\n' + "DEPENDENCY TREE" + '\n')
        for word in j.words:
            f.write(f'({word.text}, {word.head}, {word.deprel})' + ' , ')
        f.write('\n' + "NAMED ENTITIES" + '\n')
        for ent in j.ents:
            f.write(f'{ent.text}\ttype: {ent.type}' + ' , ')
        
    f.write('\n')
      

f.close()
