"""
Problem:
U have two dictionaries and want to find out what they might have in common (same key and value)
"""
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# Find keys in common
a.keys() & b.keys() # {'x', 'y'}

# Find keys in a that are not in b
a.keys() - b.keys() # {'z'}

# Find (key, value) pairs in common
a.items() & b.items() #{('y', 2)}