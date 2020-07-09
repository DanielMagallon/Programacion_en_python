import sys

print(sys.path)

l=["eat","a","piece","of","sheat"]

print("Enumeradores")
print(list(enumerate(l,1)))

for ele in enumerate(l):
    print(ele)
print("",end="\n")

# changing index and printing separately
#page 55 i am
for count,ele in enumerate(l,100):
    print(count,ele)
