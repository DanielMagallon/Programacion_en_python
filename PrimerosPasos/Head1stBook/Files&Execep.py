import os

# pathFile = os.path.dirname(__file__) -> This is the path where is located the python file that is executed
#For example, if the python file is in "/home/user/file.py" the specified method will return: /home/user/
#24.4 66.4
# os.getcwd() -> Will return the current directory where the python file was executed, for example
# if it's made a script in /usr/local/bin that executes the python file, something like this:
# python3 /home/user/file.py
#the "getcwd" method will return the path of the script: /usr/local/bin
#os.chdir() -> Will change to the folder where the python file is located but when is executed with bash
#the current path is from the path

os.chdir("../../PrimerosPasos")
print("Current directory: "+os.getcwd(),end='\n\n')
file="readable"

if not os.path.exists(file):
    print(f"The file {file} doesn't exist")
    exit(1)

my_file = open(file)


print("First line: "+my_file.readline(),end='')
print("Second line: "+my_file.readline(),end='')
print("Thirth line: "+my_file.readline())
print("Fourth line: "+my_file.readline())

print("From beginning again...")
my_file.seek(0)
print("First line: "+my_file.readline(),end='\n')

print("From beginning at char index 5 again...")
my_file.seek(5)
print("First line: "+my_file.readline(),end='')

print("From beginning with limit")
my_file.seek(0)
print("First line: "+my_file.readline(8),end='\n\n')

print("Reading all lines: ")
my_file.seek(0)

for line in my_file:
    (part,partSaid) = line.split("=")
    print(part,end=':')
    print(partSaid,end='')

print("\nDouble split")
text="I'm :nothing: using :nothing: double split"

#(first,second,third) = text.split(":")
#print(first+"-"+second+"-"+third)
var = text.split(":")
print("Index of ':' = "+str(text.find(":")))
print(var)

print("Looking for help")
#help(text.split())

my_file.close()

print("\n------------Exceptions----------------------\n")

while True:
    try:
        print("Give a number madafaka: ")
        num1 = int(input())
        print("Give another number madafaka: ")
        num2 = int(input())
        print(f"The int value of {num1} / {num2} = {(num1/num2)}")
        print(f"The decimal value of {num1} / {num2} = {int(num1 / num2)}")
        break
    except:
        ZeroDivisionError
        print("Try again, division by Zero is not valid, stupid")

