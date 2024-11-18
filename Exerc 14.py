# Verificador de polindromos


palavra = input("Digite uma palavra: ")
palavra = palavra.lower()

if palavra == palavra[::-1]:
    print(f"A palavra '{palavra}' é um polindromo")
else:
    print(f"A palavra '{palavra}' não é um polindromo.")    