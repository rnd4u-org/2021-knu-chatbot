import stanza
stanza.download('en')
english_text = ''' I want a person available 7 days and with prompt response all most every time. Only Indian freelancer need I need PHP developer who have strong experience in Laravel and Codeigniter framework for daily 4 hours. I need this work by Monday 27th Jan. should be free from plagiarism . 
Need SAP FICO consultant for support project needs to be work on 6 months on FI AREAWe.  Want a same site to be created as the same as this https://www.facebook.com/?ref=logo, please check the site before contacting to me and i want this site to be ready in 10 days. They will be ready at noon tomorrow .'''
processor_dict = {
    'tokenize': 'gsd',
    'pos': 'hdt',
    'ner': 'conll03',
    'lemma': 'default'
}

stanza.download('de', processors=processor_dict, package=None)
def stanza_nlp(text):
  nlp = stanza.Pipeline(lang='en', processors='tokenize, mwt, pos, lemma,depparse,ner')
  doc = nlp(text)
  print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')
  print(*[f'entity: {ent.text}\ttype: {ent.type}' for ent in doc.ents], sep='\n')

stanza_nlp(english_text)

