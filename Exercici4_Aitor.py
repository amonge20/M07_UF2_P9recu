import numpy as np

# Crea una matriu amb valors aleatoris de 0 a 80
def crear_matriu():
    print("Creant la matriu original...")
    matriu_original = np.random.randint(0, 81, (4, 3))
    print("Matriu original:")
    print(matriu_original)
    return matriu_original

# Modificar la matriu original
def modificar_matriu_1(matriu_original):
    print("Modificant la matriu (1a modificació)...")
    matriu_modificada_1 = np.transpose(matriu_original)
    print("Nova matriu (1a modificació):")
    print(matriu_modificada_1)
    return matriu_modificada_1

# Modificar per segona vegada la matriu modificada anteriorment
def modificar_matriu_2(matriu_modificada_1):
    print("Modificant la matriu (2a modificació)...")
    ultim_valor = matriu_modificada_1[0][-1]
    matriu_modificada_2 = np.copy(matriu_modificada_1)
    matriu_modificada_2[:, -1] = ultim_valor
    print("Nova matriu (2a modificació):")
    print(matriu_modificada_2)
    return matriu_modificada_2

# mostra el resultat final de les funcions dins d'aquest fitxer
matriu_original = crear_matriu()
matriu_modificada_1 = modificar_matriu_1(matriu_original)
matriu_modificada_2 = modificar_matriu_2(matriu_modificada_1)
