n = int(input("Digite um valor para n: "))

fibonacci = [0, 1]
if n == 1:
    fibonacci = [0]
else:
   for i in range(2, n):
       fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
       print(f"A sequencia para fibonacci com {n} primeiros numeros é: {fibonacci}")
