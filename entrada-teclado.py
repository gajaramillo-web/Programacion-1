#Ingreso dpor teclado
#Trabajo autonomo, revisar como evitar si el usuario ingresa texto no se caiga o entre en error el sistema, la respuesta es try: y except ValueError:
#strip elimina espacio en blanco
#upper() converte a mayusculas todo
#lower() convierte a mi nusculas
#capitalize() Primera en mayusculas,  title() 
nombre= input("Ingrese su nombre:").strip().title()
while True:
    try: 
        edad= int(input("Ingrese su edad:"))
        break # ← si llegó aquí, el número es válido: sale del ciclo
    except ValueError:
        print("Error: debe ingresar un número entero.")
while True:
    try:
        precio = float(input("Ingrese el precio:"))
        break
    except ValueError:
        print("Error: de ingresar un numero, por ejemplo 12.20")
#precio= float(input("Ingrese el precio:"))
#la letra f antes de las comillas permite insertar variables directamente 
#en una cadena de texto, f(cadena formateada)
print(f"Hola {nombre}, tienes {edad} años")
print(f"El precio es {precio}")

#print("Hola", nombre)
#print("Su edad es", edad)
#print("Su precio es", precio)