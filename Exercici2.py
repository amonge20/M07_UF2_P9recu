import numpy as np

# En aquesta funcio genera la primera matriu de 4x4
def matrix1():
    print("Creant la matriu 1...")
    matrix = np.zeros((4, 4))
    # Afegeix el 2 en la tercera columna
    matrix[2, :] = 2
    # Afegeix el 3 en la quarta columna en la quarta fila
    matrix[:, 3] = 3
    return matrix

# En aquesta funcio genera la segona matriu de 5x5
def matrix2():
    print("Creant la matriu 2...")
    matrix = np.ones((5, 5))
    # Assigna el valor 0 a les posicions (1,1) fins (3,3)
    matrix[1:4, 1:4] = 0
    return matrix

# En aquesta funcio genera la tercera matriu de 3x3
def matrix3():
    print("Creant la matriu 3...")
    matrix = np.eye(3)
    # incrementa la matriu amb +3
    matrix += 3
    return matrix

# truca les 3 matrius com a resultat final
matriu1 = matrix1()
print("Matriu 1:")
print(matriu1)

matriu2 = matrix2()
print("Matriu 2:")
print(matriu2)

matriu3 = matrix3()
print("Matriu 3:")
print(matriu3)
