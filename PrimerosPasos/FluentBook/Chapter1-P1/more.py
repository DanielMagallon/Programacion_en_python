class MyList():

    def __init__(self,arr):
        self.array=arr

    def addItem(self,item):
        self.array.append(item)

    def __iter__(self):
        for i in self.array:
            yield "Val: "+i

    def __bool__(self):
        return len(self.array)>=3

ml = MyList(["Edgar","Daniel","Magallon"])

for m in ml:
    print(m)

print("The size of the array is {}".format(">=3" if bool(ml) else "<3"))

if ml:
    print("Is >= 3")

print("My name is {0[name]} & my age is {0[age]}. I need a {1[0]}".format(dict(name='Fred',age="21"),
                                                ["guitar","bass"]))
print("My name is {0:8}".format('Fred','21'))

matriz=[["Edgar","Daniel","Magallon"],["Jose","Poo"],[1,2,3,4,5,6]]

for i in matriz:
    for j in i:
        print(str(j).format('%l'),end="  ")
    print()

