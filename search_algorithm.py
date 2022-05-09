def linear_search(values, search_for):
    search_at = 0
    search_res = False

    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at = search_at + 1

    return search_res


def intpolsearch(values, x):
    idx0 = 0
    idxn = len(values) - 1

    while idx0 <= idxn and x >= values[idx0] and x <= values[idxn]:
        mid = idx0 + int(((float(idxn - idx0) / (values[idxn] - values[idx0])) * (x - values[idx0])))
        if values[mid] == x:
            return "Found " + str(x) + " at index " + str(mid)
        if values[mid] < x:
            idx0 = mid + 1

    return "Searched element not in the list"


l = [64, 34, 25, 12, 22, 11, 90]
l2 = [2, 6, 11, 19, 27, 31, 45, 121]

print(linear_search(l, 12))
print(linear_search(l, 91))

print(intpolsearch(l2, 9))
