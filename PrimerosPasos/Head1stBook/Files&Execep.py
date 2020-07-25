import os

# pathFile = os.path.dirname(__file__) -> This is the path where is located the python file that is executed
#For example, if the python file is in "/home/user/file.py" the specified method will return: /home/user/
#24.4 66.4
# os.getcwd() -> Will return the current directory where the python file was executed, for example
# if it's made a script in /usr/local/bin that executes the python file, something like this:
# python3 /home/user/file.py
#the "getcwd" method will return the path of the script: /usr/local/bin
#os.chdir() -> Will change to the folder where the python file is located

os.chdir("")
print("Current directory: "+os.getcwd(),end='\n\n')

my_file = open("readable")

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
print("First line: "+my_file.readline(8),end='')



my_file.close()