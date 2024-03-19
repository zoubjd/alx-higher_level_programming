#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        lenght = len(sentence)
    else:
        lenght = 0
    return (lenght, sentence if not sentence else sentence[:1])
