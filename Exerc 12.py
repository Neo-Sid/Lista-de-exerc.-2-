#Num primos em intervalos

def num_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True
    
comeco = int(input("Digite o primeiro numero: ")) 
final = int(input("Digite o ultimo numero: "))
   
primos = []
if comeco > final:
    print("O numero do comeco não pode ser maior que do final.")
else:
    for numero in range(comeco, final + 1):
        if num_primo(numero):
            primos.append(numero)
            print("O elementos primos da lista: ", primos)
            
        