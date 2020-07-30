import array

symbols='$¢©€øþ'
codes=[ord(symbol) for symbol in symbols]
print(codes)

n1 = [1,4,5,2,10,23,120,34]
n2 = [45,2,22,120,1,5]

interseccion=[i1 for i1 in n1 for i2 in n2 if i1==i2]
print("n1: ",n1)
print("n2: ",n2)
print("n1 inters n2: ",interseccion)

listA=[1,2,7]
listB=[1,3,0]
tupleDif=[(a,b) for a in listA for b in listB if a!=b]
print("Tuples: ",tupleDif)

for tp in tupleDif:
    print(tp[0]," -- ",tp[1])

codesGreater=[ord(x) for x in symbols if ord(x)>200]
print("Codes > 200: ",codesGreater)

codesG2=list(filter(lambda c: c>200,map(ord,symbols)))
print("Codes > 200 with lambda: ",codesG2)

print("Tuple in line: ",tuple(ord(sy) for sy in symbols))
print("Array in line: ",array.array('i',(ord(sy) for sy in symbols)))
print(array.array('u', 'hello \u2641'))

a = array.array('i', [2, 4, 6, 8])

print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)