import collections
import builtins

dict1 = {'a':1,'b':2}
dict2 = {'b':3,'c':4}
dict3 = {'f': 5}

chain = collections.ChainMap(dict1,dict2)

print("All the ChainMap contents are: ")
print(chain.maps)
print("All keys of ChainMap are: ")
print(chain.keys())
print("All keys (list,no repeat) are: ")
print(list(chain.keys()))
print("All values of ChainMap are: ")
print(chain.values())
print("All values (list) of ChainMap are: ")
print(list(chain.values()))
chain=chain.new_child(dict3)
print("Chain.newchild(dict3): ",chain)
print("chain['b']: ",chain['b'])


print("\n----Counter:-----")
ct = collections.Counter('Abracadabra')
print("Abracadabra counter letters: ",ct)
ct.update('aaaaazzz')
print("Ct.update(aaaaazzz): ",ct)
print("ct.mostCommon(2): ",ct.most_common(2))