import numpy as np

# Funcio on crea la matrix i la retorna
def create_matrix():
    print("Creant la matriu...")
    matrix = np.diag(np.arange(50))
    return matrix

# Funcio en que genera un fitxer que es dira exercici1.npy i guarda la la matriu generada en la funcio anterior
def save_matrix():
    matrix = create_matrix()
    print("Guardant la matriu en un fitxer exercici1.npy...")
    np.save('exercici1.npy', matrix)
    print("Matriu guardada amb èxit!")

# Quan executem el codi, executa la funcio save_matrix i afegira el fitxer exercici1.npy en el directori
save_matrix()
