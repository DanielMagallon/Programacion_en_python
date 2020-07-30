import array

numbers = array.array('h',[-2,-1,0,1,2])
memv = memoryview(numbers)
print("Len memv: ",len(memv))
print("memv[0]: ",memv[0])

memv_oct = memv.cast('B')
print("menv_oct-list: ",memv_oct.tolist())

memv_oct[5]=4

print(numbers)