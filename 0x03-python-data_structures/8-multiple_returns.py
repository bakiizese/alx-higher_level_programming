#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    if sentence:
        return (ln, sentence[0])
    else:
        return (ln, "None")
