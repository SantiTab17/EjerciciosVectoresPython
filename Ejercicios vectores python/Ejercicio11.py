def cargar_vector():
    vector = []
    for i in range(5):
        dato = int(input(f"Ingrese el dato {i+1} del vector: "))
        vector.append(dato)
    return vector

def son_iguales(vector1, vector2):
    # Comprueba si los vectores tienen la misma longitud
    if len(vector1) != len(vector2):
        return False
    
    # Compara los vectores elemento por elemento
    for i in range(len(vector1)):
        if vector1[i] != vector2[i]:
            return False
    
    # Si no se ha encontrado ninguna diferencia, los vectores son iguales
    return True

# Cargar los dos vectores
print("Ingrese los valores para el primer vector:")
vector1 = cargar_vector()

print("\nIngrese los valores para el segundo vector:")
vector2 = cargar_vector()

# Llamar a la función para comparar los vectores
if son_iguales(vector1, vector2):
    print("\nLos vectores son iguales en contenido y posición.")
else:
    print("\nLos vectores no son iguales en contenido y/o posición.")