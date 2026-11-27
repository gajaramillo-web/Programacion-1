#Ingreso dpor teclado
#Trabajo autonomo, revisar como evitar si el usuario ingresa texto no se caiga o entre en error el sistema
nombre= input("Ingrese su nombre:")
edad= int(input("Ingrese su edad:"))
precio= float(input("Ingrese el precio:"))
#la letra f antes de las comillas permite insertar variables directamente 
#en una cadena de texto, f(cadena formateada)
print(f"Hola {nombre}, tienes {edad} años")

#print("Hola", nombre)
#print("Su edad es", edad)
#print("Su precio es", precio)