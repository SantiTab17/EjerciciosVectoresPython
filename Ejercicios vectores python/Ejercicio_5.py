#5. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números de los almacenados allí, tienen menos de 3 dígitos.

numeros = []
for i in range(0,10):
    n = int(input('Ingrese un numero: '))
    numeros.append(n)
cont = 0
for i in range(0,10):
    if numeros[i] < 100:
        cont = cont + 1
print(f'La cantidad de numeros con menos de 3 digitos es: {cont}') 