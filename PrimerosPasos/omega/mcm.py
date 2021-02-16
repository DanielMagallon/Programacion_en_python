#mcmof = [i for i in range(1,20)]
mcmof = [4,8,15,25]
#mcmof=sorted(mcmof)
acu = mcmof[-1]
max = len(mcmof)
cont=1

#The mcm([1]) is: 1 *2
#The mcm([1, 2]) is: 2 *3
#The mcm([1, 2, 3]) is: 6 *2
#The mcm([1, 2, 3, 4]) is: 12 *5
#The mcm([1, 2, 3, 4, 5]) is: 60 *0
#The mcm([1, 2, 3, 4, 5, 6]) is: 60 *7
#The mcm([1, 2, 3, 4, 5, 6, 7]) is: 420 *2
#The mcm([1, 2, 3, 4, 5, 6, 7, 8]) is: 840 *3
#The mcm([1, 2, 3, 4, 5, 6, 7, 8, 9]) is: 2520 *0
#The mcm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) is: 2520 * 11
#The mcm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) is: 27720

while True:
    for value in mcmof[:-1]:
        if acu % value != 0:
            cont=1
            break
        else: cont+=1

    if cont==max:
        print(f"The mcm({mcmof}) is: {acu}")
        break

    acu+=mcmof[-1]
