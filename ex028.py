import random
numero = int(input('informe o número: '))
rand = random.randint(0,5)
if numero == rand:
    print('Vc Acertou, eu pensei no numero {}'.format(rand))
else:
    print('Vc Perdeu, eu pensei no numero {}'.format(rand))