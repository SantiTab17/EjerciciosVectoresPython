#3. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se encuentran los números terminados en 4.

numeros = []
for i in range(0,10):
    n = int(input('Ingrese un numero: '))
    numeros.append(n)

for i in range(0,10):
    if numeros[i] % 10 == 4:
        print(f'El numero {numeros[i]} termina en 4 y esta en la posicion {i+1}')