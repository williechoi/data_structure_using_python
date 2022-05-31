from array import *


def print_array(arr):
    for x in arr:
        print(x, end=' ')
    print('\n')
    print_separating_line()


def print_separating_line():
    print('----------------------------')


array1 = array('i', [10, 20, 30, 40, 50])
print_array(array1)

print(array1[0])
print(array1[1])
print_separating_line()

array1.insert(1, 60)
print_array(array1)

array1.remove(40)
print_array(array1)

array1.index(30)
print_separating_line()

try:
    array1.index(40)
except ValueError:
    print('element not found')
print_separating_line()

array1[2] = 999
print_array(array1)

array2 = array('H', [4000, 10, 700, 22222])
print(sum(array2))
print(array2[1:3])