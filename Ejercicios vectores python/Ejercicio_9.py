#9. Leer 10 numeros enteros, almacenarlos en un vector y mostrar en pantalla todos los enteros comprendidos entre 1 y cada uno de los numeros almanecados en el vector.

numeros = []
for i in range(0,10):
    n = int(input('Ingrese un numero: '))
    numeros.append(n)
    
for i in range(0,10): 
    print(f'Los enteros comprendidos entre 1 y {numeros[i]}: ')
    for j in range(0,numeros[i]):
        print(f'{j}')
print('__________________')