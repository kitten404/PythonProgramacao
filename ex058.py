import random
acertou = False
n = 0
while acertou == False :
    n = int(input('DIGITE O NUMERO: '))
    computador = random.randint(1,10)
    if(n == computador):
        acertou = True
print('OBAAAA, vc adivinhou, PARABÉNS!!!!!')