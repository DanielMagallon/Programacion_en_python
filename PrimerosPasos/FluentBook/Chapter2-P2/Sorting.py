fruits = ['melon','banana','apple','strawberry','watermelon']
print("Fruits before sorted: ",fruits)

fruitsSReverse = sorted(fruits,reverse=True)
fruitsSorted = sorted(fruits)
fruitLenSorted = sorted(fruits,key=len)

print("Fruits after sorted: ",fruitsSorted)
print("Fruits after reverse sorted: ",fruitsSReverse)
print("Fruits after sorted by len: ",fruitLenSorted)

print("Sorting with the same object (fruits.sort())...")
fruits.sort()
print("Object fruits after operation: ",fruits)

print("Order a dict...")
dictionary = { 'name':"Edgar",'age': 21}
print(dictionary)
dict2 = sorted(dictionary)
print(dict2)




