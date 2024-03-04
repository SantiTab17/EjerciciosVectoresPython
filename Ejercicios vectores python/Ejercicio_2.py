#2. Cargar un vector de 10 posiciones con los 10 primeros elementos de la serie de Fibonacci y mostrarlo en pantalla.
fib = []

a = 0
b = 1
for i in range(0,10):
    fib.append(a)
    c = a + b
    a = b
    b = c
print(fib[:])