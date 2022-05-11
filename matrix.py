import numpy as np

arr = np.array([
    ['Mon', 18, 20, 22, 17],
    ['Tue', 11, 18, 21, 18],
    ['Wed', 18, 17, 23, 22],
    ['Thu', 11, 20, 22, 21],
    ['Fri', 18, 17, 23, 22],
    ['Sat', 12, 22, 20, 18],
    ['Sun', 13, 15, 19, 16],
])

mtrx = np.reshape(arr, (7, 5))

# Print data for Wednesday
print(mtrx[2])

# Print data for friday evening
print(mtrx[4][3])

# Add a row
mtrx_row = np.append(mtrx, [['Avg', 12, 15, 13, 11]], 0)
print(mtrx_row)

# Add a column
mtrx_col = np.insert(mtrx, [5], [[1], [2], [3], [4], [5], [6], [7]], 1)
print(mtrx_col)
