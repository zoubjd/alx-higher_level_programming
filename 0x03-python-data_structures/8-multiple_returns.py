#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        return len(sentence), sentence[0]
    else:
        sentence = None
        len = 0
        return len, sentence
