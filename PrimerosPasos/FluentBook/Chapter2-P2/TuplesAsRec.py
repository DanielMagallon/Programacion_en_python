lax_coordinates=(33.1123,-123.3434)
latitude,longitud = lax_coordinates
print("Latitud {} and longitude {} ".format(latitude,longitud))

city,year,pop,area = ('Tokyo','2020',2342,2000)
print("City: {} year: {} poping: {} area: {}m²".format(city,year,pop,area))

travele_ids = [('USA','12000'),('MEX','13000'),('FRA','23000')]

for passport in travele_ids:
    print("%s/%s" % passport)

for country,_ in travele_ids:
    print("Country: ",country," with id=",_)

x,y=["x is 20","y is 40"]
print(x+" and "+y)
t=(80,8)
print(divmod(*t))

import os

_,filename=os.path.split("/home/daniel/Desktop/do it.txt")
print("Path: ",_)
print("File name: ",filename)

a,b,*rest = range(10)
print("a: ",a)
print("b: ",b)
print("rest: ",rest)

*a,b,c,d = range(20)
print("a: ",*a)
print("b: ",b)
print("c: ",c)
print("d: ",d)

metro_areas=[('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]

print('{:15} | {:^9} | {:^9}'.format('','lat.','long.'))
fmt='{:15} | {:9.4f} | {:9.4f}'

for name,cc,pop,(latitude,longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name,latitude,longitude))