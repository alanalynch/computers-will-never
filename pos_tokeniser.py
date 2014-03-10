#!/usr/bin/python

from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

def pos_tokeniser():
    pruned = []
    
    with open('31K verbs.txt','r') as to_tokenise:

        verbs = to_tokenise.readlines()
        
        for v in verbs:
            token = pos_tag(word_tokenize(v.rstrip())) # because newlines confuse nltk

            # We're looking for verbs in the present tense. nltk sees them standing alone
            # and assumes they're either nouns, proper nouns, nouns ending in 'es', or a gerund.
            # Fortunately the ones we want are consistently nouns or proper nouns here
            if token[0][1] in ('NN','NNP'):
                pruned.append(token[0][0] + "\n") # pos_tag() returns a list of tuples
    
    with open('verbs.txt','w') as final_list:
        
        for w in pruned:
            final_list.write(str(w))
