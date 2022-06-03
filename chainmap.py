"""
Chainmap

Chainmap data structure groups multiple dictionaries into a single mapping.
Lookups search the underlying mappings one by one until a key is found.
Insertions, updates, and deletions only affect the first mapping added to the chain.
"""


from collections import ChainMap
from collections import defaultdict


dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four": 4}
dict3 = defaultdict(jay='samsung', may='kairos')

chain = ChainMap(dict1, dict2, dict3)

print(chain)

print(chain["one"])
print(chain["three"])
print(chain["may"])
try:
    print(chain["missing"])
except KeyError as err:
    print(err)
