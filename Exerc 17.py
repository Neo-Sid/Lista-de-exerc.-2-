# Numeros negativos e positivos

def ordem_positvos_e_negativos(lista):
    negativos = [num for num in lista if num < 0]
    positivos = [num for num in lista if num >= 0]
    return negativos + positivos
    
lista = [2, -1, 5, -3, 1, -2, 3, -4, 4, -5]
resultado = ordem_positvos_e_negativos(lista)
print(resultado)
