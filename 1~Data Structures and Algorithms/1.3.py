"""
Problem:
U want to keep a limited history of the last few items seen during iteration or during some other kind of processing.
"""
#Keeping a limited history is a perfect use for a collections.deque (double-ended queue)

#example 1:
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line  in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)