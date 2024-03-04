#6. Leer 10 numeros enteros, almacenarlos en un vector y determinar a cuanto es igual el promedio de los datos del vector.

numeros = []
for i in range(0,10):
    n = int(input('Ingrese un numero: '))
    numeros.append(n)
sum = 0
for i in range(0,10):
    sum = sum + numeros[i]
prom = sum % 10
print(f'El promedio entero de los numero es: {prom}')