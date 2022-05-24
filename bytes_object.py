"""
Bytes: Immutable Arrays of Single Bytes

bytes objects are immutable sequence of single bytes, or integers in the range 0 <= x <= 255.
Conceptually, bytes objects are similar to str objects, and you can also think of them as
immutable arrays of bytes.

Like strings, bytes have their own literal syntax for creating objects and are space efficient.
bytes objects are immutable, but unlike strings, there's a dedicated mutable byte array data
type called bytearray that they can be unpacked into:
"""

arr = bytes((0, 1, 2, 3))

print(arr[1])


print(arr)

try:
    print(bytes((0, 300)))
except ValueError:
    print('Invalid byte range')

try:
    arr[1] = 23
except TypeError as err:
    print(f'An error occurred while trying to assign a new value: {err}')


try:
    del arr[1]
except TypeError as err:
    print(f'An error occurred while trying to delete bytes object: {err}')

# ASCII A-Z: 65-90
# ASCII a-z: 97-122

arr2 = bytes((65+32, 66+32, 67+32, 68+32))

print(arr2)

# bytes (b'\xeb\x8c\x80\xed\x95\x9c\xeb\xaf\xbc\xea\xb5\xad') <=> utf8 (대한민국)
hangul_utf_arr = bytes((0xEB, 0x8c, 0x80, 0xed, 0x95, 0x9c, 0xeb, 0xaf, 0xbc, 0xea, 0xb5, 0xad))
print(hangul_utf_arr)
print(hangul_utf_arr.decode('utf8'))

eng_utf_arr = bytes((0x41, 0x70, 0x70, 0x6C, 0x65))
print(eng_utf_arr)  # b'\x41\x70\x70\x6c\x65'
print(eng_utf_arr.decode('utf8'))
