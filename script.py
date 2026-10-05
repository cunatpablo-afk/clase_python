# CLASE 1 DE PYTHON

print("Hola aprendiendo Python!")

nombre:str="Pablo"
apellido:str="Cuñat"
print(f"Soy {nombre} y mi apellido es {apellido}")

edad:int=23
ciudad:str="Valencia"
tengo_carnet:bool=True

print(f"Tengo {edad} años, vivo en {ciudad} y tengo carnet de conducir: {tengo_carnet}")


print(nombre.upper())
print(len(nombre))
print(nombre[0])
print(nombre[-1])

book1={
    "nombre": "Ñat",
    "edad": 23,
    "ciudad": "Valencia",
    "soltero": True
}

x = book1.get("nombre")
          
print(x)


compra=["pan", "leche", "huevos"]

# compra.append("frutas")
# compra.insert(1, "verduras")
# compra.pop(-1)

print(compra)


culpable = True

if culpable == True:
    print("Es culpable")
else:
    print("No es culpable")