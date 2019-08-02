import json

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print("The result is a dictionary: ",y)
print(y["name"])

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y+" is a String")

f = lambda a,b=10:\
      a+20+b


print(f(5))
print(f(5,1))

mytuple = [1,10,100,2,20,200]
it = iter(mytuple)

print(it.__next__())
print(it.__next__())
print(next(it))


