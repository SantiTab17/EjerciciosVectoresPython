#7. Leer 10 numeros enteros, almacenarlos en un vector y determinar en que posicion esta el menor numero primo.

numeros = []
for i in range(0,10):
    n = int(input('Ingrese un numero: '))
    numeros.append(n)

x = 1
menor = 0

for i in range(0,10):
    c = 0
    j = 1
    while j <= numeros[i]:
        if numeros[i] % j == 0:
            c += 1
        j += 1
    if c == 2:
        print(f'{numeros[i]}')
        if x == 1:
            menor = numeros[i]
            z = i
            x = 0
        if numeros[i] < menor:
            menor = numeros[i]
            z = i
if x == 0:
    print(f'el menor numero primo es: {menor} y se encuentra en la posicion {z+1}')
else:
    print('Ningun numero es primo')