import random
numeros = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10), random.randint(1,10))
c = 1
maior = 0
menor = 0
for n in numeros:
    if(c == 1):
        maior = menor = n

    if(n>maior):
        maior = n
    if(n<menor):
        menor = n
    c = c+1

print(numeros, 'O maior é :', maior,'O menor é: ', menor)