from collections import namedtuple

City=namedtuple('City','name country population coordinates')
tokyo=City('Tokyo','Japan',36.933,(35.446,139.691))
mich=City(name="Michoacan",country="Mexico",population=120000,coordinates=(12,12))
gdl=mich._replace(name='Guadalajara')

print(gdl)
print(mich)
print("Fields mich: ",mich._fields)
print(tokyo)
print("Name city: ",tokyo.name," in country: ",tokyo.country)
print("Coordinates {} = {}".format(tokyo.name,tokyo.coordinates))
print(tokyo[1])

with_class = namedtuple(
    'Person', 'name class age',
    rename=True)
print(with_class._fields)

two_ages = namedtuple(
    'Person', 'name age age',
    rename=True)
print(two_ages._fields)


delhi_data = ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi+mich)

t1=(1,2)
t2=(2,4)
tcd=t1+t2
print(tcd)