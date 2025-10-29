"""
Your program has become an unreadable mess of hardcoded slice indices and u want to clean it up.
"""
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[a]) #[2, 3]

items[a] = [10, 11]
print(items) #[0, 1, 10, 11, 4, 5, 6]

del items[a]
print(items) #[0, 1, 4, 5, 6]

a = slice(10, 50, 2)
a.start #10
a.stop #50
a.step #2