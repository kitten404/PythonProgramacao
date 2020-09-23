num = int(input('informe o num: '))
u =  num // 1 % 10
d =  num // 10 % 100
c =  num // 100 % 10
m =  num // 1000 % 10
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))