def mathPow(num,exp):
    return num**exp

def writeMsgs(*args):
    for i in args:
        print("i vale: ",i)

def itemPerItem(arr):
    """
        This function prints all items (item by item) from a list
    """

    for item in arr:
        if not isinstance(item,list):
            print("Item: {}".format(item))
        else:
            itemPerItem(item)
    
