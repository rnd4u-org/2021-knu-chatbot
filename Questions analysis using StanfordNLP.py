import stanza

QUESTIONS = [
	'Who created Git?',
	'Why git became the most popular version control system in the world?',
	'Why does it named Git?',
	'How many repositories are there?',
	'What percentage of those are public?',
	'What percentage of those are under MIT license?',
	'What is the difference between GIT and SVN?',
	'What is Git stash?',
	'How many Git functions are there?',
	'How much does Git worth?',
	'Is it neccesary to use Git in development?',
	'What is a distributed VCS?',
	'What is the difference between Git and Github?',
	'What language is used in Git?',
	'Mention the various Git repository hosting functions.',
	'How can you create a repository in Git?',
	'How to resolve a conflict in Git?',
	'How will you find out what all files have been changed in a particular Git commit?',
	'What is the use of git fork? How is forking different from cloning?',
	'What are Hooks in Git?',
	'How will you identify if the branch is already merged into master?',
	'When is the git config command used?',
	' What is the use of git clone command?',
	'What is Git stash apply? How is it different from Git stash pop?',
	'What is the Git Stash drop?',
	'What does a Commit object contain?',
	'What is git cherry-pick? What are the scenarios in which git cherry-pick can be used?',
	'What is ‘git reset’ is used for? What is the default mode of this command?',
	'What is the difference between ‘HEAD’, ‘working tree’ and ‘index’?',
	'What’s the difference between rebase and merge? When should you rebase and when should you merge?',
	'What is the syntax for rebasing?',
	' How will you remove a file from Git without actually removing it from your local filesystem?',
	'What is the common branching pattern in Git?',
	'What are the constituents of the commit object contain?',
	'What is the process for creating a repository in Git?',
	'What is ‘head’ in git and how many heads can be created in a repository?',
	'Why do we need branching in GIT?',
	'What is the regular way for branching in GIT?',
	'State a way to create a new branch in Git?',
	'How do you define a ‘conflict’ in git?',
	'How to resolve a conflict in Git?',
	'How to identify if a certain branch has been merged into master?',
	'What is the use of a Git clone?',
	'What is the function of ‘git config’?',
	'Why is it advisable to create an additional commit rather than amending an existing commit?',
	'What is ‘bare repository’ in GIT?',
	'Name a few Git repository hosting services',
	'What is the use of ‘git log’?',
	'What is the function of ‘git stash apply’?',
	'What is the function of ‘git rm?'
]

nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse,ner')
for q in QUESTIONS:
    doc = nlp(q)
    print('question: {}'.format(q))
    # tokens
    print(*[f'id: {token.id}\ttext: {token.text}' for token in doc.sentences[0].tokens], sep='\n', end='\n')
    # pos tags
    print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n', end='\n')
    # dependency tree
    print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n', end='\n')
    # named entities
    print(*[f'entity: {ent.text}\ttype: {ent.type}' for ent in doc.ents], sep='\n', end='\n\n')