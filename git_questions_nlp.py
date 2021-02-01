import stanza
import csv

nlp = stanza.Pipeline()
list_of_questions = []

with open('git_questions_nlp.csv', 'r', encoding = 'utf-8') as f:
    reader = csv.reader(f, delimiter='\n')
    for row in reader:
        list_of_questions.append(row[0])

with open('git_questions_nlp_analysis.txt', 'w', encoding='utf-8') as f:
    counter = 0
    for question in list_of_questions:
        counter += 1
        doc = nlp(question)
        f.write(f"QUESTION {counter}: {question} \n")
        f.write("\n***TOKENS*** \n")
        for i, sentence in enumerate(doc.sentences):
            for token in sentence.tokens:
                f.write(f"\tid: {token.id}\t text: {token.text}\n")

        f.write("\n***POS TAGS*** \n")
        for sentence in doc.sentences:
            for word in sentence.words:
                f.write(f"\t{word.text} -- {word.pos}\n")

        f.write("\n***DEPENDENCY TREE*** \n")
        for sentence in doc.sentences :
            for word in sentence.words:
                f.write(f"\t{str(word.text)} {str(word.head)} {str(word.deprel)}\n")

        f.write("\n***NAMED ENTITIES*** \n")
        for sentence in doc.sentences:
            for entity in sentence.ents:
                f.write(f"\t{entity.text} {entity.type}\n")
        f.write("\n")
