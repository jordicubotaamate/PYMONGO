from querys import citiesQuery,loginQuery,registerQuery
import hashlib

#print(hashlib.sha512("adios").hexdigest())

#print(loginQuery("eric",hashlib.sha512("hola").hexdigest()))

#for c in citiesQuery("Sabadell"):
   # print(c.get("population", "No se encuentra"))


print(registerQuery("hoho",hashlib.sha512("adios").hexdigest()))