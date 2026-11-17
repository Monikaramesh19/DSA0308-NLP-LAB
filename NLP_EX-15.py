import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.8] | N [0.2]
VP -> V NP [0.7] | V [0.3]
Det -> 'the' [1.0]
N -> 'cat' [0.5] | 'mouse' [0.5]
V -> 'chased' [1.0]
""")

parser = ViterbiParser(grammar)

sentence = "the cat chased the mouse".split()

for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.prob())