import stanza

nlp = stanza.Pipeline()

f1 = open('Questions.txt', 'r')
f2 = open('ResultNLP.txt', 'w')
i = 0
for line in f1:
    i += 1
    doc = nlp(line)
    f2.write('\n'+'\n'+'QUESTION '+str(i)+'. '+line)
    f2.write("Tokens: ")
    for s in doc.sentences:
        for w in s.words:
            f2.write(w.text+'\n')
    f2.write('\n'+'Pos tags: ')
    for s in doc.sentences:
        for w in s.words:
            f2.write(w.text + ': ' + w.pos+'\n')
    f2.write('\n'+'Dependency tree: ')
    for s in doc.sentences:
        for w in s.words:
            f2.write('\n'+'ID: '+str(w.id)+', Word: '+w.text+', Head ID: '+str(w.head)+', Head: '+(s.words[w.head-1].text if w.head>0 else 'Root')+', Deprel: '+w.deprel)
    f2.write('\n'+'\n'+'Named entities: ')
    for s in doc.sentences:
        for a in s.ents:
            f2.write(a.text, a.type)
