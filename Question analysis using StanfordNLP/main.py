import stanza

file = open('questions','r')
out_file = open('Results','w')
q_l = file.readlines()
question_list = [s.rstrip() for s in q_l]
nlp = stanza.Pipeline()
question_number = 0
for question in question_list:
    question_number += 1
    doc = nlp(question)
    out_file.write(f'QUESTION {question_number}:\n')
    out_file.write(question+'\n')
    out_file.write("TOKENS:\n")
    for sentence in doc.sentences:
        for word in sentence.words:
            out_file.write(word.text+'\n')
    out_file.write('\n')
    out_file.write("POS TAGS:\n")
    for sentence in doc.sentences:
        for word in sentence.words:
            out_file.write(word.pos+'\n')
    out_file.write('\n')
    out_file.write("DEPENDENCY TREE:\n")
    for sent in doc.sentences:
        for word in sent.words:
            out_file.write(f'ID: {word.id}\tWORD: {word.text}\t\tHEAD ID: {word.head}\t\tHEAD: {sent.words[word.head - 1].text if word.head > 0 else "ROOT"}\t\tDEPREL: {word.deprel}')
            out_file.write('\n')
    out_file.write('\n')
    out_file.write("NAMED ENTITIES:\n")
    for sent in doc.sentences:
        for ent in sent.ents:
            out_file.write(ent.text + ' ' + ent.type)
    out_file.write('\n')
