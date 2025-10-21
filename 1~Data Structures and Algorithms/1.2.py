"""
Problem:
U need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a 'too many values
to unpack exception.
"""
#example 1
record = ('Dave', '1@111.com', '123-231-423','892-121-909')
name, email, *phone_nums = record #Dave 1@111.com ['123-231-423', '892-121-909']
print(name, email, phone_nums)

name, *_, last_phone_number = record #Dave 892-121-909
print(name, last_phone_number)

#example 2
"""
The * syntax can be especially useful when iterating over a sequence of tuples of varying length
"""
records = [
    ('foo', 1, 2),
    ('bar', 'hi'),
    ('foo',3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)