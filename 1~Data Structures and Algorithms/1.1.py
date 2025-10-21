"""
Problem:
U have an N-element tuples or sequence that u would like to unpack into a collection of N variables
"""
#example 1
p = (1, 2, 3, 4, 5)
#x, y, z = p, Wrong: too many var to unpack
#x, y, z, a, b, c = p, Wrong: not enough values to unpack
x, y, z, a, b = p #1 2 3 4 5
print(x, y, z, a, b)

x, y, *z = p #1 2 [3, 4, 5]
print(x, y, z)

_, y, z, _, a = p #2 3
print(y, z)

#example 2
name = 'Sam'
x, y, z = name #S a m
print(x, y, z)


