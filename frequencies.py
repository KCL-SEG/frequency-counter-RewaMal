"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    strings = [str(x) for x in items]
    for i in strings:

        if i in frequencies :
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    return frequencies
