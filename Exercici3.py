import numpy as np

# Genera una matriu en que assignara un valor aleatori entre el 0 al 100
def generar_matriu(dimensio):
    matriu = np.random.randint(0, 101, dimensio)
    return matriu

# Mostra la matriu que hem generat nosaltres
def mostrar_matriu(matriu):
    print("La matriu indicada per l'usuari és:")
    print(matriu)

# Redimensionar la matriu a la nova dimensió indicada
def redimensionar_matriu(matriu, nova_dimensio):
    matriu_redimensionada = matriu.reshape(nova_dimensio)
    return matriu_redimensionada

# Mostrar per pantalla la nova matriu redimensionada
def mostrar_matriu_redimensionada(matriu_redimensionada):
    print("La nova matriu redimensionada és:")
    print(matriu_redimensionada)

# Trobara el valor maxim dins dela matriu
def trobar_valor_maxim(matriu):
    valor_maxim = np.max(matriu)
    return valor_maxim

# Trobara el valor minim dins dela matriu
def trobar_valor_minim(matriu):
    valor_minim = np.min(matriu)
    return valor_minim

dimensio = input("Introdueix la dimensió de la matriu (en format fila,columna): ")
dimensio = tuple(map(int, dimensio.split(",")))

matriu = generar_matriu(dimensio)
mostrar_matriu(matriu)

nova_dimensio = input("Introdueix la nova dimensió de la matriu (en format fila,columna): ")
nova_dimensio = tuple(map(int, nova_dimensio.split(",")))

matriu_redimensionada = redimensionar_matriu(matriu, nova_dimensio)
mostrar_matriu_redimensionada(matriu_redimensionada)

valor_maxim = trobar_valor_maxim(matriu)
print("El valor màxim de la matriu és:", valor_maxim)

valor_minim = trobar_valor_minim(matriu)
print("El valor mínim de la matriu és:", valor_minim)