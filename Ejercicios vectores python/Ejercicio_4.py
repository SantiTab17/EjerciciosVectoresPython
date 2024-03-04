#4. Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces está repetido el mayor.

numeros = []
for i in range(0,10):
    n = int(input('Ingrese un numero: '))
    numeros.append(n)
cont = 0
num_mayor = 0
for i in range(0,10):
        if i == 1 or numeros[i] > num_mayor:
            num_mayor = numeros[i]
            cont = 1
        elif numeros[i] == num_mayor:
             cont = cont + 1
print(f'El numero mayor es {num_mayor} y se repite {cont} veces')