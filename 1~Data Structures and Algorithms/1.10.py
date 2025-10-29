"""
Problem:
U want to eliminate the duplicate values in a sequence, but preserve the order of the remaining items.
"""
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 2, 3, 5, 1, 1, 7, 3, 9, 0]
print(list(dedupe(a))) #[1, 2, 3, 5, 7, 9, 0]
