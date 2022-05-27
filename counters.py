from collections import Counter

list1 = ['OK', 'PENDING', 'NOTOK', 'OK', 'OK', 'PENDING', 'NOTOK', 'UNKNOWN', 'PENDING', 'PENDING']

count = Counter(list1)
print(count)


dict1 = {
    1: {
        'result': 'OK',
        'id': 1,
        'name': 'Hyungsuk Choi'
    },
    2: {
        'result': 'PENDING',
        'id': 2,
        'name': 'Jungsuk Park'
    }
}

count2 = Counter(dict1)
print(count2)