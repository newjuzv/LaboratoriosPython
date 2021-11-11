#! /usr/local/bin/python3

# El programa calcula el resultado de la serie de Fibonacci mediante la función
# "obtener_fibonacci()"" de forma recursiva. Se utilizó una función "main()"
# para programar la entrada de argumentos adicionales mediante la clase
# "ArgumentParser" e imprimir los resultados que se solicitaron.
# Elaborado por: Julián Zamora Villalobos
# Importante: Se corrió en macOS Monterrey debido a que me falló Virtual Box

import argparse  # Se importa biblioteca para utilizar la clase
import time  # Se importa biblioteca

inicio = time.time()  # Se obtinene tiempo de inicio


def obtener_fibonacci(n):  # Se define función recursiva que hace el cálculo
    if(n == 0):            # de Fibonacci
        return 1
    if(n == 1):
        return 1
    return obtener_fibonacci(n - 1) + obtener_fibonacci(n - 2)


fin = time.time()  # Se obtiene el tiempo de finalización


def main():  # Se define función main para el manejo de argumentos

    parser = argparse.ArgumentParser()  # Se crea un objeto de la clase

    parser.add_argument(  # Primer argumento
        'posicion',  # Parámetro de entrada
        help='Posición en la secuencia de Fibonacci que debe ser calculado',
        type=int  # Se define el tipo del argumento
        )
    parser.add_argument(
        '-t',  # Abrebiatura
        '--tiempo',
        help='Imprime el tiempo transcurrido para finalizar el cálculo',
        action='store_true'
    )
    parser.add_argument(
        '-c',
        '--completa',
        help='Imprime la secuencia completa',  # La ayuda al usuario
        action='store_true'
    )

    args = parser.parse_args()  # Se leen los argumentos

    result = obtener_fibonacci(args.posicion)  # Se accede la posición
    print('El número de Fibonacci del índice ' + ' ' +
          str(args.posicion) + ' ' + 'es:' + ' ' + str(result))

    if args.tiempo & args.completa == 1:  # Si se dan ambas condiciones

        n = args.posicion  # Se obtiene el número digitado por el usuario
        for x in range(0, n):  # se imprime cada número de la serie
            print(obtener_fibonacci(x))

        print('El tiempo total de ejecución es de:' + ' ' + str(fin - inicio) +
              ' ' + 'segundos')

    elif args.completa:
        print('Serie de Fibonacci hasta índice' + ' ' + str(args.posicion) +
              ' ' + 'es:')

        n = args.posicion
        for x in range(0, n+1):
            print(obtener_fibonacci(x))

    elif args.tiempo:  # Es un boolenao, si se cumple imprime
        print('El tiempo total de ejecución es de:' + ' ' + str(fin - inicio) +
              ' ' + 'segundos')


if __name__ == '__main__':
    main()
