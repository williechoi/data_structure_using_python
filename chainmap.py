"""
Chainmap

Chainmap data structure groups multiple dictionaries into a single mapping.
Lookups search the underlying mappings one by one until a key is found.
Insertions, updates, and deletions only affect the first mapping added to the chain.
"""


from collections import ChainMap

dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four": 4}

chain = ChainMap(dict1, dict2)

print(chain)

print(chain["one"])
print(chain["three"])
try:
    print(chain["missing"])
except KeyError as err:
    print(err)
