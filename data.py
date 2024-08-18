import numpy as np
#it is a module of pandas taht is used to work with array because list is very fast and it takes a lotof memory an dis also slow
a = np.zeros([2,2],int)#fill with zeros
print(a)
b = np.ones([2,2],int)
print(b)
# for i in range we have
c = np.arange(2,101,2)
print(c)
x = np.array[[1,2,3],[2,3,4]],np.i
# for custom input
y = np.full((2,2),7)
# for converting array in differnet shapes
z = np.arange(2,101,2).reshape(2,5)
print(z)