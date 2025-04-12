'''
operadores logicos
'''
a= 30
b= 40
c= 50
r = ((a<b)and(b<c))
print("respuesta 1 es",r)

r =((a<b)or(c<a))
print("respuesta 2 es",r)

r = not((a<b)or(c<a))
print("respuesta 3 es",r)