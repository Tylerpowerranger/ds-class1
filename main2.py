import numpy as np
array1=np.array([1,2,3,4,5])
array2=np.array([6,7,8,9,10])
for x in array1:
    print(x)
array3=np.concatenate((array1,array2))
print(array3)
print(np.sort(array3))