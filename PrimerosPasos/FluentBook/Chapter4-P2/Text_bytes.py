import array

v1 = 'café'
v2 = 'cafe'


print(f"{v1}.len = {len(v1)}")
print(f"{v2}.len = {len(v2)}")

v1_encode = v1.encode('utf-8')
v2_encode = v2.encode('utf-8')

print(f"v1.encode(utf-8) = {v1_encode} and len = {len(v1_encode)}")
print(f"v2.encode(utf-8) = {v2_encode} and len = {len(v2_encode)}")


cafebytes = bytes('café',encoding='utf-8')
print(f"Café from bytes(): {cafebytes}")

for index,cafebyte in enumerate(cafebytes):
    print(f"cafe[{index}]: {cafebyte} wich is equal to: {chr(cafebyte)}")

print(cafebytes[-1:])
print(cafebytes[-1])
print(cafebytes[:-1])

cafe_arrayb = bytearray(cafebytes)
print(cafe_arrayb)

for index,cafebyte in enumerate(cafe_arrayb):
    print(f"cafe[{index}]: {cafebyte} wich is equal to: {chr(cafebyte)}")

for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

arr = [True, 5, 0, 1, False]
boolean = bool(" ")
print(boolean)
print("bytes of array: ",bytes(arr))

