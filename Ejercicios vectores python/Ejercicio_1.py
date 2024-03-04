#1. Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor número par leído.

numeros = []
for i in range(0,10):
    n = int(input('Ingrese un numero: '))
    numeros.append(n)

num_mayor = 0
for i in range(0,10):
    if numeros[i] % 2 == 0:
        if numeros[i] > num_mayor:
            num_mayor = numeros[i]
            j = i
print(f'El mayor numero par leido es {num_mayor} y esta en la posicion {j+1}')
