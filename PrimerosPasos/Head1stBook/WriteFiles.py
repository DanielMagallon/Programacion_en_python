import os

#out = open("file2Write.txt","w+")
#a+ appends
with open("file2Write.txt","a+") as out:
    print("This line was send by the python print method ",file=out)
    for _ in range(1,41):
        out.write(str(_)+"\n")

print("Var read1 exists" if 'read1' in locals() else "Var read1 doesn't exist")



string = '  xoxo love xoxo   '

# Leading and trailing whitespaces are removed
print(string)
print(string.strip())

# All <whitespace>,x,o,e characters in the left
# and right of string are removed
print(string.strip(' xoe'))

# Argument doesn't contain space
# No characters are removed.
print(string.strip('stx'))

string = 'android is awesome'
print(string.strip('an'))