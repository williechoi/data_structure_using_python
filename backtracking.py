"""
Backtracking

Backtracking is a form of recursion. But it involves choosing only option out of any possibilities.
We begin by choosing an option and backtrack from it, if we reach a state where we conclude that this specific option
does not give the required solution. We repeat these steps by going across each available option until we get
the desired solution.
"""


def permute(lst, s):
    if lst == 1:
        return s
    else:
        return [y + x for y in permute(1, s) for x in permute(lst-1, s)]


print(permute(1, ["a", "b", "c"]))
print(permute(2, ["a", "b", "c"]))
print(permute(3, ["a", "b", "c"]))
