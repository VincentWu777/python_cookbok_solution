"""
Problem:
U want to make a dictionary that maps keys to more than one value
"""
#example 1
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
} #using a list to preserve the insertion order

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
} #using a set to eliminate duplicates

#example 2
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)