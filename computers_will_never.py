#!/usr/bin/python

from random import randint
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def computers_will_never():
    verb = ""
    noun = ""
    article = " a "
    
    with open('verbs.txt','r') as verbs:
        # TODO: don't read lists into memory

        data = verbs.readlines()

        index = randint(0,len(data)-1)
        verb = data[index].rstrip()

    with open('nouns.txt','r') as nouns:
        # TODO: don't read this into memory either

        data = nouns.readlines()

        index = randint(0,len(data)-1)
        noun = data[index].rstrip()

        # Slightly naive vowel handling
        if noun.startswith(("a","e","i","o","u")):
            article = " an "
        elif pos_tag(word_tokenize(noun))[0][1] == 'NNS':
            # TODO: skip startswith() entirely if plural
            article = " "


    print "Computers will never " + verb + article + noun + "."

if __name__=='__main__':
    computers_will_never()
        
