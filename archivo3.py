nombres = input("Dime tus Nombres: ")
apellidos = input("Dime tus Apellidos: ")
edad = input("Dime tu edad: ")
carrera= input("Dime tu Carrera: ")

datos = f"Nombre: {nombres.title()}\n Apellidos: {apellidos.title()}\n Edad: {edad}\n Carrera:{carrera.title()}\n "

with open("estudiante.txt", "+a", encoding="utf-8") as archivo:
    archivo.write(datos)

print("Archivo Creado Satisfactoriamente")