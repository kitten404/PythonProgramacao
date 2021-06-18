numbers = [5,9,4,10,1]
maior = 0
menor = 0
posicao1 = 0
posicao2= 0
for p,v in enumerate(numbers) :

    if(p == 1):
        maior = v
        menor = v

    if(v > maior):
        maior = v
        posicao1 = p
    if(v < menor):
        menor = v
        posicao2 = p
print("O maior Numero é {0} e está na posição {1}.  O Menor numero é {2} e está na posicao {3}".format(maior,posicao1,menor,posicao2))


