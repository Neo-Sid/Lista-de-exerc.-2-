def num_caracteres(frase):
    contagem = {}
    for char in frase:
      if char in contagem:
        contagem[char] += 1 
        
      else:
          contagem[char] + 1
          return contagem 
    frase = "Meu pé de laranja lima.!"
    resultado = num_caracteres(frase)
    print(resultado)
    