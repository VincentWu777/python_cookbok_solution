"""
Problem:
U have a sequence of items, and u'd like to determine the most frequently occurring items in the sequence.
"""
words = [
    "apple", "banana", "orange", "grape", "apple",
    "pear", "peach", "cherry", "banana", "melon",
    "kiwi", "plum", "apple", "grape", "mango",
    "lemon", "banana", "peach", "lime", "grape",
    "strawberry", "orange", "apple", "pear", "blueberry",
    "banana", "plum", "apple", "grape", "melon"
]

from collections import Counter
words_counts = Counter(words)
top_three = words_counts.most_common(3)
print(top_three) #[('apple', 5), ('banana', 4), ('grape', 4)]

print(words_counts['apple']) #5