#! /usr/bin/python3

entero = int(input('Digite un numero entero: '))

entero2 = entero + 1

caracter = input('Digite un caracter: ')


while entero > 0:
    entero = entero - 1

while entero < entero2:
    for x  in range(entero):
        print(caracter,end='')
    print()
    entero = entero + 1
