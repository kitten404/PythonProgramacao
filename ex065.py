sair = ""
c = 1
media = 0
soma = 0
maior = 0
menor = 0
while sair in 'Ss':
        n = int(input('Digite o numero: '))
        if(c == 1):
            maior = n
            menor  = n
        if(n < menor):
            menor = n
        if(n > maior):
            maior = n
        soma = soma + n
        print('a soma é: ', soma )
        c = c + 1
        sair = str(input('Deseja Continuar ? S ou N : ')).upper()
print('a média é: ', soma/c)
print('o número maior é: ',maior)
print('o número menor é: ',menor)