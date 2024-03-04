#8. Leer 10 numero enteros, almacenarlos en un vector y determinar si existe al menos un numero repetido.

numeros = []
for i in range(0,10):
    n = int(input('Ingrese un numero: '))
    numeros.append(n)
if len(numeros) == len(set(numeros)):
    print('No existen numero repetidos')
else:
    print('Existe al menos un numero repetido')