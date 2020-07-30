import numpy as np

lista=[1,2,3]
array = np.array(lista)

print("Numpy array: ",array)

print(np.arange(0,40))
print(np.arange(5,100,5))
print(np.zeros(shape=(8,8)))

random = np.random.randint(0,100,50)
print("Random values: ",random)
print("Max: ",random.max())
print("Min: ",random.min())
random = random.reshape(10,5)
print(random)