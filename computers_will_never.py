#!/usr/bin/python

from random import random, seed
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def random_line(file):
        seed()
        selected = next(file)
        for n, line in enumerate(file, start=1):
            if random() * n < 1:
                selected = line
        return selected.rstrip()

def computers_will_never():
    verb = ""
    noun = ""
    article = " a "
    
    verb = random_line(open('verbs.txt','r'))
    noun = random_line(open('nouns.txt','r'))

    # Slightly naive vowel handling
    if noun.startswith(("a","e","i","o","u")):
        article = " an "
    elif pos_tag(word_tokenize(noun))[0][1] == 'NNS':
        # TODO: skip startswith() entirely if plural
        article = " "


    print "Computers will never " + verb + article + noun + "."

if __name__=='__main__':
    computers_will_never()
        
