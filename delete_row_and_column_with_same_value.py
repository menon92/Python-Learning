import numpy as np

b = np.array([[10, 10, 10, 10],
            [10, 5, 5, 10],
            [10, 3, 7, 10], 
            [10, 10, 10, 10]])
mask = b == 10
print(mask)
# delete column with same value
c = mask.all(axis = 0)
print(c)
print(b[:,~c])
b = b[:,~c]
# delete row with same value
c = mask.all(axis = 1)
print(c)
print(b[~c,:])

'''
Out:
[[ True  True  True  True]
 [ True False False  True]
 [ True False False  True]
 [ True  True  True  True]]
[ True False False  True]
[[10 10]
 [ 5  5]
 [ 3  7]
 [10 10]]
[ True False False  True]
[[5 5]
 [3 7]]
'''
