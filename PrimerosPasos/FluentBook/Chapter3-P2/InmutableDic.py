from types import MappingProxyType

d = {1:'A'}

dproxy = MappingProxyType(d)
print(dproxy)

print(dproxy[1])
#Error dproxy[2]='x'
d[2] = 'B'
print(dproxy)

st = {"1","2","1"}
print(st)

st2inm = frozenset({'2','puto','puta','2'})
print(st2inm)

no_repeatset = set('a la pradera')
no_repeatfset = frozenset('a la verga')

print(no_repeatset)
print(no_repeatfset)

