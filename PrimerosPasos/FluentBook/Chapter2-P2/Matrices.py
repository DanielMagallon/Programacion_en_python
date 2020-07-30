tic_tac_toe = [['_'] * 3 for i in range(3) ]

print("List independient: ")

def printBoard(board,position=None,val=None):
    if not (position is None and val is None):
        x, y = position
        board[x][y] = val

    for tt in board:
        for t in tt:
            print("{:^5}".format(t),end=' ')
        print()
    print("************")

printBoard(board=tic_tac_toe)
printBoard(val='x',position=(0,1),board=tic_tac_toe)

print("List position dependient: ")

ttt = [['_']*3]*3
printBoard(board=ttt,val='O',position=(0,0))

l2 = (1,2,3)
print("id(l2) -> ",id(l2))
print('l2 = ',l2)
l2*=3
print("l2 = (1,2,3)*3 = ",l2)
print("id(l2) -> ",id(l2))

l2 = [1,2,3]
print("\nid(l2) -> ",id(l2))
print('l2 = ',l2)
l2*=3
print("l2 = [1,2,3]*3 = ",l2)
print("id(l2) -> ",id(l2))

t = (1,2,[50,40])
try:
    t[2] += [60,70]
except TypeError as te:
    print("Error: ",te)
print(t)