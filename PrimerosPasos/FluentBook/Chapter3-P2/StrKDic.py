class StrKeyDict(dict):

    def __missing__(self, key):
        print("It's missing key: ",key)
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

print("Testing StrKeyDict...")
print("Test using d[]: ")
d = StrKeyDict([('2','two'),('4','four')])
print("d['2']: ",d['2'])
print("d['4']: ",d['4'])
try:
    print("d['1']: ",d['1'])
except KeyError:
    pass

print("\nTest using d.get(key): ")

print("d.get('2'): ",d.get('2'))
print("d.get(4): ",d.get(4))
print("d.get(1,N/A): ",d.get(1,'N/A'))

print("\nTest using in: ")
print("2 in d: ",2 in d)
print("'2' in d: ",'2' in d)
print("1 in d: ",1 in d)