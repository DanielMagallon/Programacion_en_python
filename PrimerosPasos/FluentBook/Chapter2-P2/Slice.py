s='bicycle'

print("Bicycle sliced each third position from 0")
print(s[::3])
print("Bicycle sliced each third position from 1")
print(s[1::3])
print("bicycle in reverse: ",s[::-1])
print("bicycle in reverse by two: ",s[::-2])

x=[1,2,3,4,5,6,7,8,9,10,2,4,5,6,3,6,3,6,4]
print(x[1:17:5])


invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                  $17.50      3   $52.50
1489  6mm Tactile Switch x20             $4.95       2   $9.90
1510  Panavise Jr. - PV-201              $28.00      1   $28.00
1601  PiTFT Mini Kit 320x240             $34.95      1   $34.95
"""

SKU = slice(0,6)
DESCRIPTION = slice(6,40)
UNIT_PRICE = slice(40,52)
QUANTITY = slice(52,55)
ITEM_TOTAL = slice(55,None)
lineItems=invoice.split('\n')[2:]

for item in lineItems:
    print(item[UNIT_PRICE],item[DESCRIPTION])

l = list(range(10))
print("l: ",*l)
l[2:5] = [20,30]
print("l: ",*l)

l = [1,2,3]*5
print("l[1,2,3] * 5 = ",l)
print("EDG"*3)
l = [[1,2],[3]]*2
print("[[1,2],[3]]*2 = ",l)
