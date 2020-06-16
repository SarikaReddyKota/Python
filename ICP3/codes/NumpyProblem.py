import numpy as np
a = np.random.uniform(low=1, high=20, size=20)
print(a)
b = a.reshape((4,5))
print(b)
b[np.where(b==np.amax(b,axis=1,keepdims=True))] = 0
print('Replaced array: \n{}'.format(b))

