def functionElipsis(first,*args):
    print("First argument: ",first)
    print("Other arguments: ")
    for arg in args:
        print(arg)


f = functionElipsis("Hello","there","everyone","everybody")
ar = ["good bye","bye bye"]

functionElipsis("Bye",ar)
functionElipsis("Bye",*ar)
functionElipsis("Bye",*("bai","arribiderchi"))

def functionKeyWord(first="Primero",*args,**kwargs):
    print("First argument: ",first)
    print("Array arguments: ")
    for a in args:
        print(a)

    print("Keyword args: ")
    for key,val in kwargs.items():
        print("Key: {} = {}".format(key,val))


functionKeyWord(*["Hello","Hi","Bye","Good bye"],**dict(one=1,two=2,three=3))
