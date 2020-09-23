n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
maior = 0
menor = 0
if(n1>n2 and n1>n3):
    maior = n1
else :
    if(n2>n3 and n2>n1):
        maior = n2
    else:
        if(n3>n2 and n3>n1):
            maior = n3
if(n1<n2 and n1<n3):
    menor = n1
else:
    if(n2<n3 and n2<n1):
        menor = n2
    else:
        if(n3<n1 and n3<n2):
            menor = n3

print('O maior é {}'.format(maior))
print('O menor é {}'.format(menor))