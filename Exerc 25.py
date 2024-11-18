# filtro de numero

numeros = list(map(int, input("Digite uma lista de numeros separados por espaços: ").split()))
def is_par(num):
    return num % 2 == 0
pares = list(filter(is_par, numeros))
print("Numeros pares:", pares)
