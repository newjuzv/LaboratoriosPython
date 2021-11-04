#! /usr/local/bin/python3

# El código es un programa que recibe nombres completos de personas que incluye
# nombre, primer y segundo apellido. En caso de tener segundo nombre también
# funcionará pero no permite entrada de otros tamaños. Cuando usuario introduce
# los valores, el programa se los devuelve en un formato corregido, es decir,
# independientemente como se escriba su salida será escrito primera letra en
# mayúscula y demás en minúscula.
# Elaborado por: Julián Zamora Villalobos
# Importante: Se corrió en macOS Monterrey debido a que me falló Virtual Box

lista2 = []  # Se crea lista donde se guardará nombres y apellidos corregidos
y = 1  # Variable para que while sea indefinido
while y > 0:

    cadena = input('Digite el nombre, o SALIR para salir : ')  # Input usuario
    if(cadena == 'SALIR'):  # Si se recibe SALIR se imprime lista de nombres
        for xx in lista2:
            print(xx)
        break

    li = cadena.split(' ')  # Se crea lista con nombres erróneos separandos

    if(len(li) == 3):  # Si cantidad de palabras son 3 se entra a este if
        pa1 = li[0]
        pa2 = li[1]  # Se guarda el contenido de la lista en varialbes
        pa3 = li[2]
        minus1 = pa1.lower()
        minus2 = pa2.lower()  # Se aplica minúscula a todas las palabras
        minus3 = pa3.lower()
        pri = minus1.capitalize()
        seg = minus2.capitalize()  # Se aplica primera letra mayúscula
        ter = minus3.capitalize()

        nombre = pri + ' ' + seg + ' ' + ter  # Se unen palabras espaciadas

        lista2.append(nombre)  # En esta lista se gurada el string corregido

        y = y + 1  # Contador para preguntar de nuevo

    elif(len(li) == 4):  # Este código funciona igual al caso de 3
        pa1 = li[0]
        pa2 = li[1]
        pa3 = li[2]
        pa4 = li[3]
        minus1 = pa1.lower()
        minus2 = pa2.lower()
        minus3 = pa3.lower()
        minus4 = pa4.lower()
        pri = minus1.capitalize()
        seg = minus2.capitalize()
        ter = minus3.capitalize()
        cua = minus4.capitalize()

        nombre = pri + ' ' + seg + ' ' + ter + ' ' + cua

        lista2.append(nombre)

        y = y + 1

    else:  # Se solicita de nuevo el nombre
        print('ERROR: debe digitar nombres de 3 o 4 componentes')
