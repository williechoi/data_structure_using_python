year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495

percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))

s = "Hello, world."
print(str(s))
print(repr(s))

import math

print(f'The value of pi is approximately {math.pi:.3f}')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

print('*' * 30)
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

print('*' * 30)
for name, phone in table.items():
    print('{:10} ==> {:10d}'.format(name, phone))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))