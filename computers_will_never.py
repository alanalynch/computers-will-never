#!/usr/bin/python

from random import randint

def computers_will_never():
    verb = ""
    noun = ""
    
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


    print "Computers will never " + verb + " a " + noun + "."

if __name__=='__main__':
    computers_will_never()
        
