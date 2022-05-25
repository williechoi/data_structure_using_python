
arr = bytearray((0, 1, 2, 3))
print(arr[1])

print(arr)

# bytearrays are mutable
arr[1] = 255
print(arr)
print(arr[1])

del arr[1]
print(arr)

arr.append(42)
print(arr)
print(arr[3])

# Bytearrays can only hold `bytes`
# integers in the range 0 <= x <= 255
try:
    arr[1] = 'hello'
except TypeError as err:
    print(err)

try:
    arr[1] = 300
except ValueError as err:
    print(err)

"""
A bytearray can be converted back into immutable bytes object, 
but this involves copying the stored data in full, a slow operation taking O(n) time
"""

print(bytes(arr))