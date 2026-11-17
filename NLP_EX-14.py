import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP_SG VP_SG
S -> NP_PL VP_PL
NP_SG -> 'he' | 'she'
NP_PL -> 'they'
VP_SG -> 'runs' | 'plays'
VP_PL -> 'run' | 'play'
""")

parser = ChartParser(grammar)

sentences = [
    "he runs",
    "they run",
    "he run",
    "they runs"
]

for sentence in sentences:
    tokens = sentence.split()
    trees = list(parser.parse(tokens))

    if trees:
        print(sentence, "- Agreement Correct")
    else:
        print(sentence, "- Agreement Incorrect")