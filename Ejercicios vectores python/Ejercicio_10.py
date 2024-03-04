#10. Leer 10 numeros enteros, almacenarlos en un vector y determinar cuantos numeros terminan en digito primo.

numeros = []
for i in range(0,10):
    n = int(input('Ingrese un numero: '))
    numeros.append(n)
cont = 0
for i in range(0,10):
    UltDig = numeros[i] % 10
    if UltDig ==  2 or UltDig == 3 or UltDig == 5 or UltDig == 7:
        cont = cont + 1
print(f'La cantidad de numeros que el ultimo digito es primo son: {cont}')
