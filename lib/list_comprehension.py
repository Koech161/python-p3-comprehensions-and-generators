#!/usr/bin/env python3

def return_evens(num_list):
    #pass
    evens =  [num for num in num_list if num % 2 == 0]
    return evens

def make_exclamation(sentence_list):
    #pass
    sentence=[ sen + '!' for sen in sentence_list] 
    print(sentence)
    return sentence
     