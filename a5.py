punt=4.0
corecta=0.5
correcta=1.0
valorTotal=0.0
print(f"Tu puntaje que tienes ahora es: {punt}")

print("¿Cual de los siguientes pokemon es un starters?")
print("1.Metapod\n2.Pikachu\n3.Porygon\n4.Torchic")
pokemon=int(input("escoja la opcion: "))

if pokemon==1:
    print("Respuesta incorecta")
    print(f"Tu puntaje actual es: {punt}")
elif pokemon==2:
    print("Casi pero Respuesta incorrecta")
    print(f"Tu puntaje actual es: {punt+corecta}")
    valorTotal=punt+corecta
elif pokemon==3:
    print("Respuesta incorecta")
    print(f"Tu puntaje actual es: {punt}")
elif pokemon==4:
    print("Respuesta correcta")
    print(f"Tu puntaje actual es: {correcta+punt}")
    valorTotal=punt+correcta
else:
    print("Marcaste incorrecto")



print("¿Cuantas champions tiene el real madrid?")
print("1.12\n2.15\n3.13\n4.14")
cham=int(input("escoja la opcion: "))

if cham==1:
    print("Respuesta incorecta")
    print(f"Tu puntaje actual es: {punt}")
elif cham==2:
    print("Casi pero Respuesta incorrecta")
    print(f"Tu puntaje actual es: {valorTotal+corecta}")
    valorTotal=valorTotal+corecta
elif cham==3:
    print("Respuesta incorecta")
    print(f"Tu puntaje actual es: {punt}")
elif cham==4:
    print("Respuesta correcta")
    print(f"Tu puntaje actual es: {correcta+valorTotal}")
    valorTotal=valorTotal+correcta
else:
    print("Marcaste incorrecto")
          



print("¿Cual es la consola mas vendida de la historia?")
print("1.Playstation 3\n2.Nintendo DS\n3.Xbox 360\n4.Playstation 2")
cons=int(input("escoja la opcion: "))

if cons==1:
    print("Respuesta incorecta")
    print(f"Tu puntaje actual es: {punt}")
elif cons==2:
    print("Casi pero Respuesta incorrecta")
    print(f"Tu puntaje actual es: {valorTotal+corecta}")
    valorTotal=valorTotal+corecta
elif cons==3:
    print("Respuesta incorecta")
    print(f"Tu puntaje actual es: {punt}")
elif cons==4:
    print("Respuesta correcta")
    print(f"Tu puntaje actual es: {correcta+valorTotal}")
    valorTotal=valorTotal+correcta
else:
    print("Marcaste incorrecto")
          
print(f"El puntaje que obtuviste fue un: {valorTotal}")